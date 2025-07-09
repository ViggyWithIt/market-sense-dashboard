# Market-Sense Dashboard

**A data-driven web application that visualizes daily stock prices against financial news sentiment to provide clearer market context.**

![Market-Sense Screenshot](images/screenshot.png)

## Project Description

In a world where financial stability can feel unpredictable, understanding the forces that drive market movements is a form of empowerment. This project was born from a desire to cut through the noise of financial reporting and create a clear, data-driven view of market sentiment.

Market-Sense is a full-stack web application that fetches real-time stock prices and financial news from the Alpha Vantage API. It then calculates an average daily sentiment score from the news headlines and plots this score against the stock's price on a single, interactive chart. By visualizing quantitative price data alongside qualitative sentiment data, this tool aims to provide a more nuanced perspective for students and new investors.

## Features

-   **Dynamic Data Fetching:** Pulls the latest daily stock prices and news from the Alpha Vantage API
-   **Sentiment Analysis:** Calculates an average sentiment score for each day based on financial news headlines
-   **Interactive Visualization:** Renders a responsive line chart using Chart.js with dual Y-axes to clearly compare price and sentiment
-   **Full-Stack Architecture:** Built with a Python/Flask backend that processes data and a JavaScript/HTML frontend that displays it

## Tech Stack

-   **Backend:** Python, Flask
-   **Frontend:** HTML, CSS, JavaScript, Chart.js
-   **APIs:** Alpha Vantage API
-   **Libraries:** Requests

## Local Setup and Installation

Follow these steps to run the project on your local machine.

**1. Clone the Repository**
```bash
git clone https://github.com/your-username/market-sense-project.git
cd market-sense-project
```

**2. Create and Activate a Virtual Environment**
```bash
# Create the virtual environment
python -m venv venv

# Activate on macOS/Linux
source venv/bin/activate

# Activate on Windows
.\venv\Scripts\activate
```

**3. Install Dependencies**
This project's dependencies are listed in the `requirements.txt` file.
```bash
pip install -r requirements.txt
```

**4. Add Your API Key**
This project requires a free API key from Alpha Vantage.

> **Important:** Get your free key at [https://www.alphavantage.co/support/#api-key](https://www.alphavantage.co/support/#api-key)

Open the `app.py` file and replace `'YOUR_API_KEY'` with your actual key.

**5. Run the Application**
```bash
python app.py
```
Open your web browser and navigate to `http://127.0.0.1:5000` to see the application running. 