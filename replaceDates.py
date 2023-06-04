import pandas as pd
from datetime import datetime
import nltk
from datetime import timedelta


data = pd.read_csv('mentions.csv')

# print(data.head())

print(datetime.today())

for i in range(0, len(data)):
    today = datetime.today()
    curDate = data['Date'][i]
    

    tok = nltk.word_tokenize(curDate)
    mult = tok[0]

    if mult.isnumeric():
        mult = int(mult)
        if tok[1] == "month" or tok[1] == "months":
            newDate = today-timedelta(days=mult*30)
        elif tok[1] == "week" or tok[1] == "weeks":
            newDate = today-timedelta(days=mult*7)
        elif tok[1] == "day" or tok[1] == "days":
            newDate = today-timedelta(days=mult*1)
        else:
            newDate = today
    else:
        # Convert Mar 26, 2023 to datetime
        newDate = datetime.strptime(curDate, "%b %d, %Y")
    
    # Round current datetime to nearest day
    newDate = newDate.replace(hour=0, minute=0, second=0, microsecond=0)
    data['Date'][i] = newDate
    

data.to_csv('mentions.csv', index=False)