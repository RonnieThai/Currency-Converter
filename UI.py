#Ronnie Thai
#25-01-16

from tkinter import *
from tkinter import ttk
import tkinter as tk

# Class for the UI of the converter
class ConverterUI(tk.Tk):
    def __init__(self, converter):
        tk.Tk.__init__(self)
        self.title("Currency Converter")
        self.converter = converter

        # Details of the UI
        self.geometry("500x250")  # Fixed geometry
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
        self.result_label.pack(pady=20)

    #Call in the different method in the code for converter to work 
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