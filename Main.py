#Ronnie Thai
#25-01-16
#Website for converter: https://exchangeratesapi.io/  (Have to reset once maximum use has been reached)

from Converter import CurrencyConverter
from UI import ConverterUI

#Initialize the UI and converter 
#Utilize the API key for the converter 
if __name__ == "__main__":
    API_KEY = "d32351236c47e3f49dd688fcab2a4597"
    converter = CurrencyConverter(API_KEY)
    ConverterUI(converter).mainloop()