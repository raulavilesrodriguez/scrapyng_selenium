from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.common.exceptions import NoSuchElementException
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait
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

urlg = f'https://www.plusvalia.com/inmuebles-en-venta-en-quito-pagina-1.html'
driver = configuracion_ini()
driver.get(urlg)
driver.maximize_window()
titulos = driver.find_elements('xpath', '//div[@data-qa="POSTING_CARD_LOCATION"]/p')
procesamiento(titulos)
df = pd.DataFrame({'Location': list_titulos})
df.to_excel('list_titulos.xlsx', index=False)

page_id = 1
while True:    
    try:
        numeral = f'//div/a[@data-qa="PAGING_{page_id}"]'
        print(numeral)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(('xpath', f'//div/a[@data-qa="PAGING_{page_id}"]')))
        time.sleep(0.25)
        boton = driver.find_element('xpath', f'//div/a[@data-qa="PAGING_{page_id}"]')
        time.sleep(1)
        boton.click()
        #driver.execute_script("arguments[0].click();", boton)
        titulos = driver.find_elements('xpath', '//div[@data-qa="POSTING_CARD_LOCATION"]/p')
        procesamiento(titulos)
        df = pd.DataFrame({'Location': list_titulos})
        df.to_excel('list_titulos.xlsx', index=False)
        page_id += 1

    except NoSuchElementException:
        print(f'Last page: {page_id}')
        driver.close()
        break

df = pd.DataFrame({'Location': list_titulos})
df.to_excel('list_titulos.xlsx', index=False)


