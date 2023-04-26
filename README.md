# ZerodhaCharges Class Documentation

This class, **ZerodhaCharges**, is designed to calculate the charges for trades executed on the Zerodha platform. It supports equity, currency, and commodity markets. The class contains three methods: **equity_charges**, **currency_charges**, and **commodity_charges**. These methods calculate the charges for the respective markets.

Attributes:

- **gst_rate**: The Goods and Services Tax (GST) rate applied to charges. Default value is 0.18 (18%).
- **sebi_rate**: The Securities and Exchange Board of India (SEBI) charges rate. Default value is 10 / (10\*\*7).

Methods:

**equity_charges(market_type, order_type, buy_value, sell_value, quantity, options_premium=None) -> float**

Calculates charges for equity trades.

Parameters:

- **market_type** (str): The market type, either 'nse' or 'bse'.
- **order_type** (str): The order type, either 'delivery', 'intraday', 'futures', or 'options'.
- **buy_value** (float): The total value of the buy transaction.
- **sell_value** (float): The total value of the sell transaction.
- **quantity** (int): The number of shares or contracts.
- **options_premium** (float, optional): The premium per share or contract for options trades. Required for 'options' order type.
- (float): The total charges for the equity trade.

**currency_charges(order_type, buy_value, sell_value, options_premium=None) -> float**

Calculates charges for currency trades.

Parameters:

- **order_type** (str): The order type, either 'futures' or 'options'.
- **buy_value** (float): The total value of the buy transaction.
- **sell_value** (float): The total value of the sell transaction.
- **options_premium** (float, optional): The premium per contract for options trades. Required for 'options' order type.
- (float): The total charges for the currency trade.

**commodity_charges(order_type, buy_value, sell_value, agri, options_premium=None) -> float**

Calculates charges for commodity trades.

Parameters:

- **order_type** (str): The order type, either 'futures' or 'options'.
- **buy_value** (float): The total value of the buy transaction.
- **sell_value** (float): The total value of the sell transaction.
- **agri** (bool): True if the commodity is agricultural, False otherwise.
- **options_premium** (float, optional): The premium per contract for options trades. Required for 'options' order type.
- (float): The total charges for the commodity trade.

Usage Example:

```
print(f"Equity charges: {equity_charges}")
print(f"Currency charges: {currency_charges}")
print(f"Commodity charges: {commodity_charges}")
```

In this usage example, we first create an instance of the **ZerodhaCharges** class. Then, we calculate the charges for equity, currency, and commodity trades using the appropriate methods. Finally, we print the calculated charges.
