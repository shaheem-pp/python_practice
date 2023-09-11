from moneyed import Money, list_all_currencies
from moneyed.l10n import format_money

sale_price_today = Money(amount="99.99", currency="USD")
formatedsale_price_today = format_money(Money(99.99, "USD"), locale="en_US")
print(formatedsale_price_today)
all_currencies = list_all_currencies()
print(len(all_currencies))


from currency_converter import CurrencyConverter
c = CurrencyConverter()
print("c.convert(1, 'CAD', 'INR')")
print(c.convert(1, 'CAD', 'INR'))