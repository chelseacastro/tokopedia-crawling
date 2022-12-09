from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd

try:
    driver = webdriver.Chrome("C:/ChromeDriver/chromedriver.exe") # opening chrome
    driver.maximize_window() # maximizing windows page
    driver.get("https://www.tokopedia.com/search?navsource=&page=1&q=xiaomi&srp_component_id=02.01.00.00&srp_page_id=&srp_page_title=&st=product") # input url in address bar

    driver.execute_script("window.scrollTo(0,1000);") # scroll driver/website
    names = driver.find_elements(By.CLASS_NAME, "prd_link-product-name")
    prices = driver.find_elements(By.CLASS_NAME, "prd_link-product-price")

    # for x in range(len(names)):
    #     print(names[x].text)
    #     print(prices[x].text)

    product_name = []
    product_price = []

    for x in range(len(names)):
        product_name.append(names[x].text)
        product_price.append(prices[x].text)

    df = pd.DataFrame()
    df['Product Name'] = product_name
    df['Product Price'] = product_price

    print(df)

finally:
    time.sleep(10)
    driver.quit()
