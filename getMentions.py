import time
from bs4 import BeautifulSoup
import re
import nltk
import requests

import pandas as pd
from tickList import tickList


# Read in news dataframe
newsdf = pd.read_csv("mentions.csv")

for i in range(300,len(newsdf)-1):

    # Get link
    link = newsdf["Link"][i]
    print("Link #{}: {}".format(i, link))
    time.sleep(1)
    
    try:
        # Get page source
        r = requests.get(link, timeout=10)
        print("Status: ", r.status_code)

        # Retry if status code is not 200
        tryCount = 0
        while r.status_code != 200 and tryCount < 5:
            print("Retrying...", tryCount)
            r = requests.get(link, timeout=10)
            time.sleep(1)
            tryCount += 1

    except:
        # If error, skip link
        print("Error")
        continue


    

    #Get page source and tokenizes data
    html = r.content

    # Create BeautifulSoup object
    soup = BeautifulSoup(html, "html.parser")

    # Get all text from page
    pageSource = " ".join(soup.strings)
    pageSource = re.sub(r"\s+", " ", pageSource)

    # Tokenize page source
    tokens = nltk.word_tokenize(pageSource)

    # Return all mentions of tickers in page source
    tickMentioned = []
    for token in tokens:
        if token in tickList:
            tickMentioned.append(token)

    # Remove duplicates
    tickMentioned = list(set(tickMentioned))
    print(tickMentioned)
    
    # Add tickers mentioned to newsdf
    newsdf["Tickers Mentioned"][i] = tickMentioned

    # Save dataframe to csv
    newsdf.to_csv("mentions.csv", index=False)