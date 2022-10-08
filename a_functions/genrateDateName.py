from datetime import datetime
from num2words import num2words
def nowEncryption(spcStr):
    encp = ''
    encp+=spcStr
    today = datetime.now()
    date = today.strftime("%d")
    month = today.strftime("%m")
    year = today.strftime("%Y")
    hours = today.strftime("%H")
    minutes = today.strftime("%M")
    seconds = today.strftime("%S")
    encp+= num2words(date,lang='es')
    encp+= num2words(month,lang='es')
    encp+= num2words(year,lang='es')
    encp+= num2words(hours,lang='es')
    encp+= num2words(minutes,lang='es')
    encp+= num2words(seconds,lang='es')
    encp = encp.replace(" ", "")
    return encp
    

