import time
import pandas as pd
import requests

def getTime(timestamp):
    timeTemp = time.gmtime(timestamp / 1000)
    return time.strftime("%Y-%m-%d %H:%M:%S", timeTemp)

class BinanceAPI():
    def __init__(self):
        self.SpotAPIDomain = "https://www.binance.com/api/v3"
        self.FuturesAPIDomain = "https://www.binance.com/fapi/v1"
        
    def spotSymbols(self):
        response = requests.get(f"{self.SpotAPIDomain}/ticker/price")
        return pd.DataFrame(response.json())[["symbol"]]
    
    def spotHistory(self, symbol, interval):
        response = requests.get(f'{self.SpotAPIDomain}/klines?limit=1000&symbol={symbol}&interval={interval}')
        dataTemp = response.json()
        lastTime = pd.DataFrame(dataTemp).head(1)[0].values[0]
        data = dataTemp

        while len(dataTemp) == 1000:
            print(f"{symbol} {getTime(lastTime)} \t\t\t\t\t\t\t\t\t\t", end='\r', flush=True)
            response = requests.get(f'{self.SpotAPIDomain}/klines?endTime={lastTime - 1}&limit=1000&symbol={symbol}&interval={interval}')
            dataTemp = response.json()
            lastTime = pd.DataFrame(dataTemp).head(1)[0].values[0]
            data += dataTemp
            time.sleep(0.1)

        kbars = pd.DataFrame(data)[[0, 1, 2, 3, 4, 5]]
        kbars = kbars.rename(columns={0: 'time', 1: 'open', 2: 'high', 3: 'low', 4: 'close', 5: 'volume'})
        kbars = kbars.drop_duplicates(subset=['time'], keep='first')
        kbars = kbars.sort_values(by='time').reset_index(drop=True)
        kbars.time = pd.to_datetime(kbars.time / 1000, unit='s')
        kbars['time'] = kbars['time'].dt.strftime('%Y-%m-%d %H:%m:%s')
        return kbars


BinanceAPI = BinanceAPI()