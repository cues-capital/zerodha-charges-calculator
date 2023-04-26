# ZerodhaCharges

A Python class to calculate charges for trades executed on the Zerodha platform. It supports equity, currency, and commodity markets. The class contains three methods: equity_charges, currency_charges, and commodity_charges, which calculate the charges for the respective markets.

## Features

- Calculate charges for equity trades
- Calculate charges for currency trades
- Calculate charges for commodity trades

## Usage

To use the `ZerodhaCharges` class, simply import it and create an instance:

```python
from brokerage_calculator import ZerodhaCharges

zerodha = ZerodhaCharges()
```

Use the appropriate method to calculate charges for the specific market:

```python
equity_charges = zerodha.equity_charges(market_type, order_type, buy_value, sell_value, quantity, options_premium=None)
currency_charges = zerodha.currency_charges(order_type, buy_value, sell_value, options_premium=None)
commodity_charges = zerodha.commodity_charges(order_type, buy_value, sell_value, agri, options_premium=None)
```

## Requirements

- Python 3.6+

## Installation

To use `ZerodhaCharges` in your project, copy the `brokerage_calculator.py` file to your project directory and import it as shown in the Usage section.

## Examples

A complete example demonstrating how to use `ZerodhaCharges`:

```python
from brokerage_calculator import ZerodhaCharges

zerodha = ZerodhaCharges()

equity_charges = zerodha.equity_charges("nse", "delivery", 10000, 11000, 100)
currency_charges = zerodha.currency_charges("futures", 5000, 5500)
commodity_charges = zerodha.commodity_charges("futures", 2000, 2200, False)

print(f"Equity charges: {equity_charges}")
print(f"Currency charges: {currency_charges}")
print(f"Commodity charges: {commodity_charges}")
```

In this example, we first create an instance of the `ZerodhaCharges` class. Then, we calculate the charges for equity, currency, and commodity trades using the appropriate methods. Finally, we print the calculated charges.

## Contributing

Contributions to `ZerodhaCharges` are welcome! If you find a bug or would like to propose a new feature, feel free to open an issue or submit a pull request.

## License

`ZerodhaCharges` is released under the [MIT License](https://opensource.org/licenses/MIT).