

import africastalking as at
import os
from dotenv import load_dotenv
import pymongo

load_dotenv()

at_username = os.getenv("at_username")
at_api_key = os.getenv("at_api_key")
mobile_number = os.getenv("mobile_number")
mongo_uri = os.getenv("MONGODB_URI")
# print(at_username, at_api_key)
# Initialize the Africas sdk py passing the api key and username from the .env file
at.initialize(at_username, at_api_key)
sms = at.SMS
account = at.Application


ticker_data = []

# Create a function to send a message containing the stock ticker and price
def stock_notification(message: str, number: int):
    try:
        response = sms.send(message, [number])
        print(account.fetch_application_data())
        print(response)
    except Exception as e:
        print(f" Houston we have a problem: {e}")


# TODO: Add a function to notify client once the price changes
# create a function to query mongodb for the stock price of Safaricom
def stock_query():
    client = pymongo.MongoClient(mongo_uri)
    db = client["nse_data"]
    collection = db["stock_data"]
    # print(collection.find_one())
    ticker_data = collection.find_one({"ticker": "BAT"})
    print(ticker_data)
    stock_name = ticker_data["name"]
    stock_price = ticker_data["price"]
    sms_data = { "stock_name": stock_name, "stock_price": stock_price }
    print(sms_data)

    message = f"Hello the current stock price of {stock_name} is {stock_price}"
    # check if Safaricom share price is more than Kes 39 and send a notification.
    if int(float(stock_price)) >= 38:
        # Call the function passing the message  and mobile_number as a arguments
        print(message)
        stock_notification(message, mobile_number)
    else:
        print("No notification sent")
    
    client.close()

    return sms_data

stock_query()

