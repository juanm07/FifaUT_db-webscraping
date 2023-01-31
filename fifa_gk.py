from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException,NoSuchElementException
from csv import writer
options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")
chrome_executable = Service(executable_path='chromedriver.exe', log_path='NUL')
driver = webdriver.Chrome(service=chrome_executable)
driver.get('https://wefut.com/player-database/"fifa number"') #13,14,...,22
next_page = driver.find_element(By.XPATH, '//*[@id="playerTable_next"]')
change_to_GK = driver.find_element(By.XPATH, '//*[@id="playerTable_wrapper"]/div[1]/div/div[1]/div/div[2]/div/label/div/div[1]/span')
headers = ['Name', 'Rating', 'Type', 'Region', 'DIV', 'HAN', 'KIC', 'REF', 'SPE', 'POS', 'Link']

i = 0
with open('csv file name', 'w', encoding='utf-8', newline='') as f:
    thewriter = writer(f)
    thewriter.writerow(headers)
    driver.execute_script("arguments[0].click();", change_to_GK)
    while True:
        i = next_page.get_attribute("class")
        if i == "paginate_disabled_next":
            break
        for x in range(1, 26):
            try:
                try:
                    xpath_name = '//*[@id="playerTable"]/tbody/tr[{}]/td[2]/a'.format(x)
                    xpath_rtg = '//*[@id="playerTable"]/tbody/tr[{}]/td[3]/font'.format(x)
                    xpath_type = '//*[@id="playerTable"]/tbody/tr[{}]/td[3]/font'.format(x)
                    xpath_region = '//*[@id="playerTable"]/tbody/tr[{}]/td[7]'.format(x)
                    xpath_DIV = '//*[@id="playerTable"]/tbody/tr[{}]/td[8]'.format(x)
                    xpath_HAN = '//*[@id="playerTable"]/tbody/tr[{}]/td[9]'.format(x)
                    xpath_KIC = '//*[@id="playerTable"]/tbody/tr[{}]/td[10]'.format(x)
                    xpath_REF = '//*[@id="playerTable"]/tbody/tr[{}]/td[11]'.format(x)
                    xpath_SPE = '//*[@id="playerTable"]/tbody/tr[{}]/td[12]'.format(x)
                    xpath_POS = '//*[@id="playerTable"]/tbody/tr[{}]/td[13]'.format(x)
                    name = driver.find_element(By.XPATH, xpath_name).text
                    rtg = driver.find_element(By.XPATH, xpath_rtg).text
                    card_type = (driver.find_element(By.XPATH, xpath_type)).get_attribute('class')
                    
                    region = driver.find_element(By.XPATH, xpath_region).text
                    # Note: for FIFA22 use (driver.find_element(By.XPATH, xpath_region)).get_attribute('title')
                    
                    DIV = driver.find_element(By.XPATH, xpath_DIV).text
                    HAN = driver.find_element(By.XPATH, xpath_HAN).text
                    KIC = driver.find_element(By.XPATH, xpath_KIC).text
                    REF = driver.find_element(By.XPATH, xpath_REF).text
                    SPE = driver.find_element(By.XPATH, xpath_SPE).text
                    POS = driver.find_element(By.XPATH, xpath_POS).text
                    Link = (driver.find_element(By.XPATH, xpath_name)).get_attribute('href')

                except NoSuchElementException:
                    pass
                info = [name, rtg, card_type, region, DIV, HAN, KIC, REF, SPE, POS, Link]
                thewriter.writerow(info)
            except StaleElementReferenceException:
                pass
        driver.execute_script("arguments[0].scrollIntoView();", next_page)
        driver.execute_script("arguments[0].click();", next_page)
