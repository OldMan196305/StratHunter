# Aggragate data for backtesting 
import datetime as dt
#from token import CIRCUMFLEX
import pandas as pd
import requests

# Start and End times to gather data
# start = dt.datetime(2023,1,1)
# end = dt.datetime.now()

Function = 'TIME_SERIES_INTRADAY'
Symbol = 'QDTE'
Interval = '1min'
Month = '2024-12'
Adjusted = 'false'
#Extended_Hours = 'false'
#Extended_Hours = 'true'
DataType = 'json'

# Load data

# Alpha Vantage test area
API_KEY = '7RJR7E1925NJT0JU'

#
# https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&month=2009-01&outputsize=full&apikey=demo
#


url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=Symbol&interval=1min&month=Month&outputsize=full&datatype=json&apikey=API_KEY'

r = requests.get(url)
data = r.json()
print(r.status_code)

# print(data)

with open(".App/Hunter/ingest.dat", 'ab') as fd:
    fd.write(b'$Symbol  $Month\n')
    for chunk in r.iter_content(chunk_size=128):
        fd.write(chunk)
    fd.write(b'\n\n')
fd.close()


