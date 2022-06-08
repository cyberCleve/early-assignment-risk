#!/usr/bin/env python3

import requests
import json
import portfolio


def get_put_spreads() -> list:
    account_id = open("account_id", 'r').readline().strip()
    token = open("token", 'r').readline().strip()

    endpoint = f"https://api.tdameritrade.com/v1/accounts/{account_id}?fields=positions"
    headers = {"Authorization": f"Bearer {token}"}

    # query API
    resp = json.loads(requests.get(endpoint, headers=headers).text)

    # extract PUT spreads from open positions
    put_spreads = []
    positions = resp['securitiesAccount']['positions']
    for pos in positions:
        if pos['instrument']['assetType'] == 'OPTION':
            if pos['instrument']['putCall'] == 'PUT':
                if pos['shortQuantity'] != 0:
                    strike = pos['instrument']['symbol'].split('P')[-1]
                    qty = pos['shortQuantity']
                    put_spreads.append([strike, qty])
    return put_spreads

put_spreads= get_put_spreads()
portfolio = portfolio.Portfolio()
for spread in put_spreads:
    portfolio.add_spread(strike=float(spread[0]), qty=int(spread[1]))

portfolio.get_margin_risk()



