#!/usr/bin/env python3
from dataclasses import dataclass, field
from typing import List
import sys


@dataclass
class Portfolio:
    spreads: list = field(default_factory=lambda: [])
    rate: float = 0.085

    def add_spread(self, strike: float, qty: int):
        self.spreads.append({"strike": strike, "qty": qty})

    def get_margin_risk(self) -> float:
        borrow = sum(map(lambda x: x["strike"] * x["qty"] * 100, self.spreads))

        # There are considered to be 360 days in a year while calculating margin interest
        interest = (((borrow * self.rate) / 360) * 4)
        print(round(interest, 2))


if __name__ == 'main':
    portfolio = Portfolio(rate=0.085)
    print("Enter any number of spreads. Enter ^c when finished.")
    while True:
        try:
            strike = float(input("Short strike: "))
            qty = int(input("Qty: "))
            portfolio.add_spread(strike, qty)
        except KeyboardInterrupt:
            portfolio.get_margin_risk()
            sys.exit()
