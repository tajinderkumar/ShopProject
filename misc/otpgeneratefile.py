import random
import datetime as dt

def genrateotp():
    rn=random.randint(100000,10000000)
    time=str(dt.datetime.now())
    return rn,time