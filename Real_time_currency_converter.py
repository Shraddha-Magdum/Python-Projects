
# from forex_python.converter import CurrencyRates
# from forex_python.converter import CurrencyCodes
import forex_python.converter

k = forex_python.converter.CurrencyRates()
c = forex_python.converter.CurrencyCodes()


while True:
    amount = input("Enter the amount you want to convert : ")
    print()
    try:
        amount = int(amount)
        break
    except ValueError:
        try:
            amount = float(amount)
            break
        except ValueError:
            print("Invalid Input !")
            print()

print()

while True:
    try:
        from_currency = input("From Currency: ").upper()
        to_currency = input("To Currency: ").upper()
        print()
        result = k.convert(from_currency, to_currency, amount)
        print(f"{from_currency} to {to_currency} of {c.get_symbol(from_currency)}{amount} is {c.get_symbol(to_currency)}{result}")
        break
    except forex_python.converter.RatesNotAvailableError:
        print('Invalid Input ! Enter again...')
        print()
