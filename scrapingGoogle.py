import time
from selenium import webdriver
from selenium.webdriver.common.by import By

import pandas as pd

# Create driver
driver = webdriver.Chrome()

# URL of the webpage to scrape
url = "https://www.google.com/search?q=top+growth+stocks+to+invest&rlz=1C1ONGR_enUS1037US1037&tbm=nws&ei=SMp4ZIh6wJ7k2g_I2q3QCA&start=0&sa=N&ved=2ahUKEwiIvsXkwaL_AhVAD1kFHUhtC4o4FBDy0wN6BAgEEAQ&biw=1849&bih=1009&dpr=1"  # Replace with the desired webpage URL

# Create dataframe
newsDf = pd.DataFrame(columns=["Organization", "Link", "Title", "Date"])

# Call driver to get webpage
driver.get(url)

for i in range(31):
    print("Page: " + str(i - 1))
    # Lets Webpage load
    time.sleep(4)

    div_xpath = """//*[@id="rso"]/div/div"""  # Replace with the actual XPath of the desired <div> element
    div_element = driver.find_element(By.XPATH, div_xpath)

    # Get all the links from specific div
    org = driver.find_elements(By.CLASS_NAME, 'NUnG9d')
    links = div_element.find_elements(By.TAG_NAME, "a")
    titles = driver.find_elements(By.CLASS_NAME, 'nDgy9d')
    dates = driver.find_elements(By.CLASS_NAME, 'LfVVr')


    # Add each row to dataframe
    for containerNum in range(len(links)):
        newsDf.loc[len(newsDf)] = [org[containerNum].text, links[containerNum].get_attribute("href"), titles[containerNum].text, dates[containerNum].text]

    # Update csv in case of error
    newsDf.to_csv("news.csv")

    # Gets the URL of the next google page
    next_xpath = """//*[@id="botstuff"]/div/div[2]"""
    next_element = driver.find_element(By.XPATH, next_xpath)
    links = next_element.find_elements(By.TAG_NAME, "a")
    next_link = links[-1].get_attribute("href")

    # Go to next page
    driver.get(next_link)

# Save Dataframe to CSV
print(newsDf)
newsDf.to_csv("news.csv")

driver.quit()
