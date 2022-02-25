# 幣安API套件
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
# interval 時間間格
BinanceAPI.spotHistory(symbol="", interval="")
```