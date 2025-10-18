from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://www.python.org")


years = driver.find_elements(By.CSS_SELECTOR, ".event-widget .menu span")
times = driver.find_elements(By.CSS_SELECTOR, ".event-widget .menu time")
dates=[]
for i in range(0, len(years)):
    dates.append(years[i].get_attribute("innerHTML")+times[i].text)
    
title = driver.find_elements(By.CSS_SELECTOR, '.event-widget .menu a')

    
dict={}
for i in range(0, len(dates)):
    dict[i]={'time':dates[i], 'name':title[i].text}
    
print(dict)
driver.quit()