import requests
import os
from dotenv import load_dotenv

load_dotenv()

def get_wallet_data():
    wallet_address = os.getenv("WALLET_ADDRESS")
    etherscan_api_key = os.getenv("ETHERSCAN_API_KEY")

    # ETH Balance (in Wei)
    eth_balance_url = f"https://api.etherscan.io/api?module=account&action=balance&address={wallet_address}&tag=latest&apikey={etherscan_api_key}"
    eth_balance_response = requests.get(eth_balance_url).json()
    balance_eth = int(eth_balance_response['result']) / 1e18

    # Prices from CoinGecko
    prices = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=ethereum,bitcoin&vs_currencies=usd").json()
    eth_price = prices.get('ethereum', {}).get('usd', 0)
    btc_price = prices.get('bitcoin', {}).get('usd', 0)

    return [
        {
            'wallet': wallet_address,
            'token': 'ETH',
            'balance': round(balance_eth, 4),
            'usd_value': round(balance_eth * eth_price, 2)
        },
        {
            'wallet': wallet_address,
            'token': 'BTC',
            'balance': 'N/A (BTC not tracked by wallet)',
            'usd_value': btc_price
        }
    ]
