from selenium import webdriver
from time import sleep


GOOGLE_FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLScboTXmBHG4qoEg80DPHhkFzXfh9Fn9hsuVyoe9G4fOIQmCog/viewform?usp=sf_link"
CHROME_DRIVER_PATH = "chromedriver.exe"
ZILLOW_SEARCH_URL = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%3A-122.30389632177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D"

driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
driver.get(ZILLOW_SEARCH_URL)
prices = driver.find_elements_by_class_name('list-card-price')
addresses = driver.find_elements_by_class_name('list-card-addr')
links = driver.find_elements_by_css_selector('div.list-card-info > a')
data = []
for i in range(len(prices)):
    print(f"Price {i}: {prices[i].text}")
    print(f"Address {i}: {addresses[i].text}")
    print(f"Link {i}: {links[i].get_attribute('href')}")
    print("  ----- \n")
    data.append((prices[i].text, addresses[i].text, links[i].get_attribute('href')))

body = driver.find_element_by_tag_name("body")


driver.get(GOOGLE_FORM_URL)
sleep(1)
for i in range(len(prices)):
    input_addr = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    input_addr.send_keys(data[i][0])
    input_price = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    input_price.send_keys(data[i][1])
    input_link = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    input_link.send_keys(data[i][2])
    btn_submit = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span/span')
    btn_submit.click()
    btn_next_response = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    btn_next_response.click()

driver.quit()

