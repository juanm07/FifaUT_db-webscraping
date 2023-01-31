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
driver.get('https://wefut.com/player-database/"fifa number"') #Fifa 13,14,15,...,22
next_page = driver.find_element(By.XPATH, '//*[@id="playerTable_next"]')
headers = ['Name', 'Rating', 'Position', 'Type', 'Region', 'PAC', 'SHO', 'PAS', 'DRI', 'DEF', 'PHY', 'Link']


with open('CSV file name', 'w', encoding='utf-8', newline='') as f:
    thewriter = writer(f)
    thewriter.writerow(headers)
    
    while True:
        i = next_page.get_attribute("class")
        if i == "paginate_disabled_next":
            break
        for x in range(1, 26):
            try:
                try:
                    xpath_name = '//*[@id="playerTable"]/tbody/tr[{}]/td[2]/a'.format(x)
                    xpath_rtg = '//*[@id="playerTable"]/tbody/tr[{}]/td[3]/font'.format(x)
                    xpath_pos = '//*[@id="playerTable"]/tbody/tr[{}]/td[4]/span'.format(x)
                    xpath_type = '//*[@id="playerTable"]/tbody/tr[{}]/td[3]/font'.format(x)
                    xpath_region = '//*[@id="playerTable"]/tbody/tr[{}]/td[7]'.format(x)
                    xpath_PAC = '//*[@id="playerTable"]/tbody/tr[{}]/td[8]'.format(x)
                    xpath_SHO = '//*[@id="playerTable"]/tbody/tr[{}]/td[9]'.format(x)
                    xpath_PAS = '//*[@id="playerTable"]/tbody/tr[{}]/td[10]'.format(x)
                    xpath_DRI = '//*[@id="playerTable"]/tbody/tr[{}]/td[11]'.format(x)
                    xpath_DEF = '//*[@id="playerTable"]/tbody/tr[{}]/td[12]'.format(x)
                    xpath_PHY = '//*[@id="playerTable"]/tbody/tr[{}]/td[13]'.format(x)
                    name = driver.find_element(By.XPATH, xpath_name).text
                    rtg = driver.find_element(By.XPATH, xpath_rtg).text
                    position = driver.find_element(By.XPATH, xpath_pos).text
                    card_type = (driver.find_element(By.XPATH, xpath_type)).get_attribute('class')

                    region = driver.find_element(By.XPATH, xpath_region).text
                    # Note: for FIFA22 use (driver.find_element(By.XPATH, xpath_region)).get_attribute('title')
                    
                    PAC = driver.find_element(By.XPATH, xpath_PAC).text
                    SHO = driver.find_element(By.XPATH, xpath_SHO).text
                    PAS = driver.find_element(By.XPATH, xpath_PAS).text
                    DRI = driver.find_element(By.XPATH, xpath_DRI).text
                    DEF = driver.find_element(By.XPATH, xpath_DEF).text
                    PHY = driver.find_element(By.XPATH, xpath_PHY).text
                    Link = (driver.find_element(By.XPATH, xpath_name)).get_attribute('href')
                   
                except NoSuchElementException:
                    pass

                info = [name, rtg, position, card_type, region, PAC, SHO, PAS, DRI, DEF, PHY, Link]
                thewriter.writerow(info)

            except StaleElementReferenceException:
                pass
        driver.execute_script("arguments[0].scrollIntoView();", next_page)
        driver.execute_script("arguments[0].click();", next_page)
