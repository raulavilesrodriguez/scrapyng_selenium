from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument('--disable-blink-features=AutomationControlled')

def configuracion_ini():
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()),
        #executable_path=r"webdriver\chromedriver.exe",
        options=options,
    )
    return driver

driver = configuracion_ini()
driver.get('https://www.plusvalia.com/inmuebles-en-venta-en-quito-pagina-1.html')
driver.maximize_window()

list_titulos = []
def procesamiento(titulos):
    for i in range(len(titulos)):
        list_titulos.append(titulos[i].text)

titulos = driver.find_elements('xpath', '//div[@data-qa="POSTING_CARD_LOCATION"]/p')
procesamiento(titulos)
#while True:    
    #try:
        #next_page_button = driver.find_element('xpath', '//a[@data-qa="PAGING_NEXT"]')
        #next_page_button.click()
    #except NoSuchElementException:
        #break

#button = (driver.find_element(('xpath', '//a[@href="/inmuebles-en-venta-en-quito-pagina-2.html"]')))
#button.click()
#https://scrapingclub.com
driver.get('https://www.google.com/')
driver.maximize_window()
time.sleep(1)
driver.close()
page_id = 2
driver = configuracion_ini()
driver.get(f'https://www.plusvalia.com/inmuebles-en-venta-en-quito-pagina-id{page_id}.html')

titulos2 = driver.find_elements('xpath', '//div[@data-qa="POSTING_CARD_LOCATION"]/p')
procesamiento(titulos2)
print(list_titulos)



