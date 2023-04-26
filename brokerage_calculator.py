class ZerodhaCharges:
    def __init__(self):
        self.gst_rate = 0.18
        self.sebi_rate = 10 / (10**7)

    def equity_charges(self, market_type, order_type, buy_value, sell_value, quantity, options_premium=None):
        """
        Calculate charges for equity trades.

        :param market_type: str - Market type ('nse' or 'bse').
        :param order_type: str - Order type ('delivery', 'intraday', 'futures', or 'options').
        :param buy_value: float - Total value of the buy transaction.
        :param sell_value: float - Total value of the sell transaction.
        :param quantity: int - Number of shares or contracts.
        :param options_premium: float - Premium per share or contract for options trades (required for 'options' order_type).
        :return: float - Total charges for the equity trade.
        """
        if order_type not in ["delivery", "intraday", "futures", "options"]:
            raise ValueError("Invalid order type.")
        
        if market_type not in ["nse", "bse"]:
            raise ValueError("Invalid market type.")

        brokerage = 0.0
        stt_ctt = 0.0
        transaction_charges = 0.0

        if order_type == "delivery":
            brokerage = 0
            stt_ctt = 0.001 * (buy_value + sell_value)
            transaction_charges = (0.00325 if market_type == "nse" else 0.00375) * (buy_value + sell_value)
        elif order_type == "intraday":
            brokerage = min(0.0003 * sell_value, 20)
            stt_ctt = 0.00025 * sell_value
            transaction_charges = (0.00325 if market_type == "nse" else 0.00375) * sell_value
        elif order_type == "futures":
            brokerage = min(0.0003 * sell_value, 20)
            stt_ctt = 0.000125 * sell_value
            transaction_charges = 0.0019 * sell_value
        elif order_type == "options":
            if options_premium is None:
                raise ValueError("Options premium is required for options trades.")
            brokerage = 20
            stt_ctt = 0.000625 * options_premium * quantity
            transaction_charges = 0.05 * options_premium * quantity

        sebi_charges = (buy_value + sell_value) * self.sebi_rate
        stamp_charges = (0.00015 if order_type == "delivery" else 0.00003) * buy_value
        gst = self.gst_rate * (brokerage + sebi_charges + transaction_charges)

        total_charges = brokerage + stt_ctt + transaction_charges + sebi_charges + stamp_charges + gst
        return total_charges
    
    def currency_charges(self, order_type, buy_value, sell_value, options_premium=None):
        """
        Calculate charges for currency trades.

        :param order_type: str - Order type ('futures' or 'options').
        :param buy_value: float - Total value of the buy transaction.
        :param sell_value: float - Total value of the sell transaction.
        :param options_premium: float - Premium per contract for options trades (required for 'options' order_type).
        :return: float - Total charges for the currency trade.
        """
        
        if order_type not in ["futures", "options"]:
            raise ValueError("Invalid order type.")

        brokerage = 0.0
        transaction_charges = 0.0

        if order_type == "futures":
            brokerage = min(0.0003 * sell_value, 20)
            transaction_charges = 0.0009 * sell_value
        elif order_type == "options":
            if options_premium is None:
                raise ValueError("Options premium is required for options trades.")
            brokerage = 20
            transaction_charges = 0.035 * options_premium

        sebi_charges = (buy_value + sell_value) * self.sebi_rate
        stamp_charges = 0.00001 * buy_value
        gst = self.gst_rate * (brokerage + sebi_charges + transaction_charges)

        total_charges = brokerage + transaction_charges + sebi_charges + stamp_charges + gst
        return total_charges

    def commodity_charges(self, order_type, buy_value, sell_value, agri, options_premium=None):
        """
        Calculate charges for commodity trades.

        :param order_type: str - Order type ('futures' or 'options').
        :param buy_value: float - Total value of the buy transaction.
        :param sell_value: float - Total value of the sell transaction.
        :param agri: bool - True if the commodity is agricultural, False otherwise.
        :param options_premium: float - Premium per contract for options trades (required for 'options' order_type).
        :return: float - Total charges for the commodity trade.
        """
        if order_type not in ["futures", "options"]:
            raise ValueError("Invalid order type.")

        brokerage = 0.0
        stt_ctt = 0.0
        transaction_charges = 0.0

        if order_type == "futures":
            brokerage = min(0.0003 * sell_value, 20)
            stt_ctt = 0.0001 * sell_value if not agri else 0
            transaction_charges = 0.0026 * sell_value
        elif order_type == "options":
            if options_premium is None:
                raise ValueError("Options premium is required for options trades.")
            brokerage = 20
            stt_ctt = 0.0005 * options_premium
            transaction_charges = 0.05 * options_premium

        sebi_charges = (buy_value + sell_value) * (0.000001 if agri else self.sebi_rate)
        stamp_charges = (0.00002 if order_type == "futures" else 0.00003) * buy_value
        gst = self.gst_rate * (brokerage + sebi_charges + transaction_charges)

        total_charges = brokerage + stt_ctt + transaction_charges + sebi_charges + stamp_charges + gst
        return total_charges