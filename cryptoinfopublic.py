import requests
import json


def ethereum_info():
    api_key = "YOUR API KEY FOR ETHERSCAN"
    gas = (requests.get(
        "https://api.etherscan.io/api?module=gastracker&action=gasoracle&apikey=" + api_key))
    # I had to break the line-up. It was too long.
    data = gas.text
    parse_json = json.loads(data)
    safe_gas = parse_json['result']['SafeGasPrice']
    fast_gas = parse_json['result']['FastGasPrice']
    print("Ethereum safe gas price is " + safe_gas + ". Fast gas price is " + fast_gas + ".")


def coin_price_info():
    coin_data = (requests.get(
        "https://api.coingecko.com/api/v3/simple/"
        "price?ids=bitcoin%2Cdogecoin%2Cethereum&vs_currencies=usd&include_24hr_change=true"))
    coin_data_text = coin_data.text
    coin_data_json = json.loads(coin_data_text)
    bitcoin_price = coin_data_json["bitcoin"]["usd"]
    bitcoin_change = coin_data_json["bitcoin"]["usd_24h_change"]
    print("The price of bitcoin is " + str(bitcoin_price)
          + ". The 24 hour change is " + str(bitcoin_change)[:5] + "%. ")
    dogecoin_price = coin_data_json["dogecoin"]["usd"]
    dogecoin_change = coin_data_json["dogecoin"]["usd_24h_change"]
    print(
        "The price of dogecoin is " +
        str(dogecoin_price)[:6] + ". The 24 hour change is " + str(dogecoin_change)[:5] + "%. ")
    ethereum_price = coin_data_json["ethereum"]["usd"]
    ethereum_change = coin_data_json["ethereum"]["usd_24h_change"]
    print(
        "The price of ethereum is " + str(ethereum_price)
        + ". The 24 hour change is " + str(ethereum_change)[:5] + "%. ")


print()
coin_price_info()
print()
ethereum_info()
