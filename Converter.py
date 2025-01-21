# Ronnie Thai
# 25/01/16

from tkinter import *
from tkinter import ttk
import tkinter as tk
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


# Class for the UI of the converter
class ConverterUI(tk.Tk):
    def __init__(self, converter):
        tk.Tk.__init__(self)
        self.title("Currency Converter")
        self.converter = converter

        # Details of the UI
        self.geometry("500x200")  # Fixed geometry
        self.intro_label = Label(self, text="Currency Converter", fg="blue", font=("Arial", 16))
        self.intro_label.pack()

        self.amount_label = Label(self, text="Enter Amount: ", font=("Arial", 12))
        self.amount_label.pack()
        self.amount_entry = Entry(self)
        self.amount_entry.pack()

        # UI for base currency
        self.from_currency_label = Label(self, text="From Currency:")
        self.from_currency_label.pack()
        # Dropdown list for currencies
        self.from_currency_combo = ttk.Combobox(self, values=list(converter.rates.keys()), state='readonly')
        self.from_currency_combo.set('CAD')  # Base currency
        self.from_currency_combo.pack()

        # UI for target currency
        self.to_currency_label = Label(self, text="To Currency:")
        self.to_currency_label.pack()
        # Dropdown list for currencies
        self.to_currency_combo = ttk.Combobox(self, values=list(converter.rates.keys()), state='readonly')
        self.to_currency_combo.set('USD')
        self.to_currency_combo.pack()

        # UI for the convert button
        self.convert_button = Button(self, text="Convert", command=self.perform_conversion)
        self.convert_button.pack()

        self.result_label = Label(self, text="", font=("Arial", 14))
        self.result_label.pack()

    def perform_conversion(self):
        try:
            amount = float(self.amount_entry.get())
            from_currency = self.from_currency_combo.get()
            to_currency = self.to_currency_combo.get()

            converted_amount = self.converter.convert(from_currency, to_currency, amount)
            self.result_label.config(text=f"Converted Amount: {converted_amount} {to_currency}")
        except ValueError:
            self.result_label.config(text="Please enter a valid amount!")
        except KeyError:
            self.result_label.config(text="Invalid currency code or API error!")


if __name__ == "__main__":
    API_KEY = "d32351236c47e3f49dd688fcab2a4597"
    converter = CurrencyConverter(API_KEY)
    ConverterUI(converter).mainloop()

