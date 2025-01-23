from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
url = "https://en.wikipedia.org/wiki/Main_Page"
driver.get(url)

# #article_count = driver.find_element(By.CSS_SELECTOR, value="#articlecount a")
# article_count = driver.find_element(By.XPATH, value='//*[@id="articlecount"]/ul/li[2]/a[1]')
# article_count.click()

# # Find element by Link Text
# content_portals = driver.find_element(By.LINK_TEXT, value="Content portals")
# content_portals.click()



search_button = driver.find_element(By.XPATH, value='//*[@id="p-search"]/a')
search_button.click()
# Find the "Search" <input> by Name
search = driver.find_element(By.NAME, value="search")
search.send_keys("cats")
search.send_keys(Keys.ENTER)
# driver.close()