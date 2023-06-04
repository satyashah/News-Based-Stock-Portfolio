import pandas as pd
import alpaca_trade_api as tradeapi

api = tradeapi.REST(
    'PKQ0KTYFV13T0I4QT8LR',
    'AwdeCjje9cn9fC0UQIvTXBL9broWEQqFcXN9obRn',
    'https://paper-api.alpaca.markets', api_version='v2'
)











data = pd.read_csv('picks.csv', index_col=0)
print(data)

totalCount = sum(data['count'])
totalEquity = 100000

for i in range(0, len(data)):
    print("Submitted {} order for {}$".format(data['tick'][i],  round(data['count'][i]/totalCount * totalEquity,2)))
    api.submit_order(
        symbol= data['tick'][i],
        notional = round(data['count'][i]/totalCount * totalEquity,2),
        side = 'buy',
        type = 'market',
        time_in_force = 'day',
    )
