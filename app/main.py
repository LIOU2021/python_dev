import time
import pandas as pd
from module1.echo import echoFunc
from module1 import echo
import module1.echo as md1

while True :
    print("Hello, World!")
    print(pd.DataFrame({'A': [1, 2, 3]}))
    echoFunc("my module")
    echo.echoFunc("my test echo")
    md1.myFunc1("my func1")
    md1.echoFunc("echo 1 ")
    
    time.sleep(1)
    