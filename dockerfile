# 以Python3.5.10-slim 執行環境作為Docker Image基礎
# 如果沒有先載好image，會在後期build的時候pull
FROM python:3.9-alpine
# 在container環境內，創建一個stock並移動到stock file裡
WORKDIR /app
# 將當前目錄資料加入到container內的stock資料夾
ADD ./app /app
# pip 安裝requirements.txt內的套件
# RUN python3 -m pip install -r requirements.txt
RUN pip install --upgrade pip
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt
## 最後執行main這個程式，但是我想用另一種方法執行，所以略過
CMD python main.py