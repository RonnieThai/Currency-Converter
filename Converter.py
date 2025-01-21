# Ronnie Thai
# 25/01/16
import requests

# Constructor class that uses the methods
class CurrencyConverter:

    # Create a method that grabs the URL of the conversion website
    def __init__(self, api_key):
        self.api_key = api_key
        self.url = f"https://api.exchangeratesapi.io/latest?access_key={self.api_key}"
        self.data = requests.get(self.url).json()
        self.rates = self.data.get("rates", {})

    # Create a method to convert the currency
    def convert(self, from_currency, to_currency, amount):
        initial_amount = amount
        # The base currency is Canada
        if from_currency != 'CAD':
            amount = amount / self.rates.get(from_currency, 1)

        # Convert to the target currency
        converted_amount = amount * self.rates.get(to_currency, 1)
        converted_amount = round(converted_amount, 4)
        return converted_amount
