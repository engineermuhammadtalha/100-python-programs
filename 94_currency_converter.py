# Currency Converter (Fixed Rates)

rates = {
    "USD": 1.0,
    "EUR": 0.92,
    "GBP": 0.79,
    "PKR": 278.50,
    "INR": 83.12,
    "AED": 3.67,
    "SAR": 3.75,
    "JPY": 149.50,
    "CAD": 1.36,
    "AUD": 1.53
}

print("Available currencies:", ", ".join(rates.keys()))

from_currency = input("Convert from (e.g. USD): ").upper()
to_currency = input("Convert to (e.g. PKR): ").upper()
amount = float(input("Enter amount: "))

if from_currency not in rates or to_currency not in rates:
    print("Invalid currency code.")
else:
    result = amount / rates[from_currency] * rates[to_currency]
    print(f"\n{amount:.2f} {from_currency} = {result:.2f} {to_currency}")
    print("(Note: Rates are approximate and fixed)")
