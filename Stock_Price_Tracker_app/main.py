import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
ALPHA_API_KEY = "T9IGSDB8F3V2JX1E"
NEWS_API_KEY = "42cae77c8c584c299a8d781d8006c587"
TWILIO_API_KEY = "" #Enter your key here
TWILIO_SID = "" #Enter your key here
TWILIO_AUTH_TOKEN = "" #Enter your key here


stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": ALPHA_API_KEY
}


response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
#print(data_list)
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]
print(yesterday_closing_price)

day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]
print(day_before_yesterday_closing_price)

difference = abs(float(yesterday_closing_price) - (float(day_before_yesterday_closing_price)))
print(difference)

diff_percent = (difference / float(yesterday_closing_price)) * 100
print(diff_percent)


if diff_percent > 5:

    news_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME
    }

    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = (news_response.json()["articles"])

three_articles = articles[:3]
print(three_articles)

formatted_articles_list = [f"Headline: {article['title']}. \n Brief: {article['description']}" for article in three_articles]
print(formatted_articles_list)
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    for article in formatted_articles_list:
        message = client.messages.create(
            body=article,
            from_=VIRTUAL_TWILIO_NUMBER,
            to=VERIFIED_NUMBER
        )

