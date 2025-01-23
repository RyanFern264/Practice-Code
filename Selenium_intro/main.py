from selenium import webdriver
from selenium.webdriver.common.by import By

#Keep Chrome open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://python.org")

#finding element by class name
# price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole")
# price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
# print(f"The price is {price_dollar.text}.{price_cents.text}")

#finding element by name
search_bar = driver.find_element(By.NAME, value="q")
#finding element by ID
button = driver.find_element(By.ID, value="submit")
#finding element by CSS selector (inside documentation widget class, get attribute a)
documentation_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
#finding element by XPATH, when all else fails. Inspect element, right click element, then do copy> copy xpath
bug_link = driver.find_element(By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')


# events = {
#     0:{
#         "time":driver.find_element(By.XPATH, value='//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[1]/time').text,
#         "name":driver.find_element(By.XPATH, value='//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[1]/a').text
#     },
#     1:{
#         "time":"",
#         "name":""
#     },
#     2:{
#         "time":"",
#         "name":""
#     },
#     3:{
#         "time":"",
#         "name":""
#     },
#     4:{
#         "time":"",
#         "name":""
#     },
# }
#
# print(events)


#Here's a smarter way, use CSS selectors to drill down into it
events = {}
#here im getting a unique class called event widget, and within all event widget items, getting time items
event_times = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")


event_names = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")

for n in range(len(event_times)):
    events[n] = {
        "time":event_times[n].text,
        "name":event_names[n].text
    }
print(events)
driver.close()






