# 幣安API套件
當前版本：1.1 \n
最後更新：2022/10/11

## 使用方式

請在專案下同一個目錄建立檔案

```python
from BinanceAPI import BinanceAPI
```

### 取得現貨所有幣種
```python
BinanceAPI.spotSymbols()
```

### 取得現貨歷史資料
```python
# symbol 幣種
# interval 時間間格 (1m、3m、5m、30m、1h、2h、6h、8h、12h、1d、3d、1w、1M)
BinanceAPI.spotHistory(symbol="BTCUSDT", interval="4h")
```

### 取得合約歷史資料
```python
# symbol 幣種
# interval 時間間格 (1m、3m、5m、30m、1h、2h、6h、8h、12h、1d、3d、1w、1M)
BinanceAPI.futureHistory(symbol="BTCUSDT", interval="4h")
```