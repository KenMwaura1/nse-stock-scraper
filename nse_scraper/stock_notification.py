from typing import List, Any

from models import StockData, db_connect
from sqlalchemy.orm import sessionmaker
from sqlalchemy import desc
import africastalking as at
import os
from dotenv import load_dotenv

load_dotenv()
at_username = os.getenv("at_username")
at_api_key = os.getenv("at_api_key")
mobile_number = os.getenv("mobile_number")
# print(at_username, at_api_key)
# Initialize the Africas sdk py passing the api key and username from the .env file
at.initialize(at_username, at_api_key)
sms = at.SMS
account = at.Application

engine = db_connect()
Session = sessionmaker(bind=engine)
session = Session()
ticker_data = []


# TODO: Add a function to notify client once the price changes
def stock_query():
    sq = session.query(StockData.id, StockData.stock_ticker, StockData.stock_name,
                       StockData.stock_price).filter(StockData.stock_ticker == "SCOM")

    for id, ticker, name, price in sq.order_by(desc(StockData.id)).limit(1):
        # print(id, name, ticker, price)
        new_data = {'stock_id': id, 'stock_name': name, 'stock_ticker': ticker, 'stock_price': price}
        return new_data


# Create a function to send a message containing the stock ticker and price
def stock_notification(message: str, number: int):
    try:
        response = sms.send(message, [number])
        print(account.fetch_application_data())
        print(response)
    except Exception as e:
        print(f" Houston we have a problem: {e}")


message = f'{stock_query()["stock_name"]}, is now Kes {stock_query()["stock_price"]} per share'
# check if Safaricom share price is more than Kes 39 and send a notification.
if stock_query().get("stock_price") >= 38:
    # Call the function passing the message  and mobile_number as a arguments
    print(message)
    stock_notification(message, mobile_number)
