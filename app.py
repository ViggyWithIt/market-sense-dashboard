from flask import Flask, render_template
import requests
from datetime import datetime

# --- Initialize the Flask Application ---
app = Flask(__name__)

# --- Your Data Fetching and Merging Logic ---
def get_market_data(symbol='IBM'):
    # IMPORTANT: Replace with your actual API key
    API_KEY = 'H30O5AJRVNKSKAGQ'
    
    # 1. Fetch Price Data
    price_url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&outputsize=full&apikey={API_KEY}'
    print(f"Fetching daily price data for {symbol}...")
    try:
        response = requests.get(price_url)
        response.raise_for_status()
        price_data = response.json().get('Time Series (Daily)', {})
        print("Price data fetched successfully.")
    except Exception as e:
        print(f"Error fetching price data: {e}")
        price_data = {}

    # 2. Fetch News Sentiment Data
    news_url = f'https://www.alphavantage.co/query?function=NEWS_SENTIMENT&tickers={symbol}&limit=200&apikey={API_KEY}'
    print(f"Fetching news sentiment data for {symbol}...")
    try:
        response = requests.get(news_url)
        response.raise_for_status()
        news_data = response.json().get('feed', [])
        print("News data fetched successfully.")
    except Exception as e:
        print(f"Error fetching news data: {e}")
        news_data = []

    # 3. Merge the Data
    print("\nMerging price and sentiment data...")
    combined_data = {}
    for date_str, daily_data in price_data.items():
        combined_data[date_str] = {
            'close_price': float(daily_data['4. close']),
            'sentiment_scores': [],
            'avg_sentiment': 0.0
        }

    for article in news_data:
        time_published_str = article.get('time_published')
        ticker_sentiment_info = next((item for item in article.get('ticker_sentiment', []) if item["ticker"] == symbol), None)
        
        if time_published_str and ticker_sentiment_info:
            publication_date = datetime.strptime(time_published_str, '%Y%m%dT%H%M%S').strftime('%Y-%m-%d')
            if publication_date in combined_data:
                sentiment_score = float(ticker_sentiment_info.get('ticker_sentiment_score', 0.0))
                combined_data[publication_date]['sentiment_scores'].append(sentiment_score)

    # 4. Calculate Average Sentiment
    for date_str, data in combined_data.items():
        scores = data['sentiment_scores']
        if scores:
            data['avg_sentiment'] = sum(scores) / len(scores)
            
    return combined_data

# --- Define the Main Route (Homepage) ---
@app.route('/')
def index():
    print("Rendering the homepage with data...")
    # Call our function to get the data
    market_data = get_market_data()
    
    # Sort the dates to pass them to the template in order
    sorted_dates = sorted(market_data.keys(), reverse=True)
    
    # Pass the data to the template file
    # The variable name on the left ('market_data') is what we'll use in the HTML
    return render_template('index.html', market_data=market_data, sorted_dates=sorted_dates)

# --- Run the Application ---
if __name__ == '__main__':
    app.run(debug=True)