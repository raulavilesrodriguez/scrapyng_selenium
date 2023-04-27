from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.common.exceptions import NoSuchElementException
import pandas as pd
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
        options=options,
    )
    return driver

list_titulos = []
def procesamiento(titulos):
    for i in range(len(titulos)):
        list_titulos.append(titulos[i].text)

page_id = 0
while True:    
    try:
        page_id +=1
        urlg = f'https://www.plusvalia.com/inmuebles-en-venta-en-quito-pagina-{page_id}.html'
        print(urlg)
        driver = configuracion_ini()
        driver.get(urlg)
        driver.maximize_window()
        titulos = driver.find_elements('xpath', '//div[@data-qa="POSTING_CARD_LOCATION"]/p')
        procesamiento(titulos)
        driver.close()

        driver = configuracion_ini()
        driver.get('https://www.google.com/')
        driver.maximize_window()
        time.sleep(1)
        driver.close()
        df = pd.DataFrame({'Location': list_titulos})
        df.to_excel('list_titulos.xlsx', index=False)
    except NoSuchElementException:
        print(f'Last page: {page_id}')
        break

df = pd.DataFrame({'Location': list_titulos})
df.to_excel('list_titulos.xlsx', index=False)


