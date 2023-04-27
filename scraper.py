from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver as uc
import time
from selenium.webdriver import DesiredCapabilities


options = uc.ChromeOptions()
#options.add_argument("--headless=new") 
driver = uc.Chrome(use_subprocess=True, options=options)
#options.add_argument("--disable-gpu")
#options.add_argument("--disable-extensions")
#options.add_argument("--no-sandbox")
#options.add_argument('--ignore-ssl-errors=yes')
#options.add_argument('--ignore-certificate-errors')
#options.add_argument('--allow-insecure-localhost')
#driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
#driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get('https://www.plusvalia.com/inmuebles-en-venta-en-quito.html')
driver.maximize_window()
time.sleep(100)
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

#button = wait.until(EC.element_to_be_clickable(('xpath', '//a[@href="/inmuebles-en-venta-en-quito-pagina-2.html"]')))
#button.click()
driver.get('https://www.plusvalia.com/inmuebles-en-venta-en-quito-pagina-2.html')

titulos2 = driver.find_elements('xpath', '//div[@data-qa="POSTING_CARD_LOCATION"]/p')
procesamiento(titulos2)
print(list_titulos)
driver.close()
