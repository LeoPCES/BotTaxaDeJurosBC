from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import pyautogui
obj = webdriver.Chrome()

obj.get('https://www.bcb.gov.br')

sleep(3)
#fechando cookies
obj.find_element(By.XPATH, '/html/body/app-root/bcb-cookies/div/div/div/div/button[2]').click()

obj.find_element(By.XPATH, '//*[@id="fixed-areas"]/header/div[1]/div[2]/button[2]/span').click()
obj.find_element(By.XPATH, '//*[@id="fixed-areas"]/div[1]/app-busca/div/div/div/form/div/div[1]/input').send_keys("taxas de juros")
pyautogui.press('enter')

try:
    obj.find_element(By.XPATH, '/html/body/app-root/app-root/main/dynamic-comp/div/bcb-pagina-tipo0/div/bcb-pagina-tipo4/div[3]/div/dynamic-comp/bcb-resultadobusca/div/div[2]/div/div[2]/div/div[1]/h5/a').click()
except:
    obj.get('https://www.bcb.gov.br/estatisticas/txjuros')

obj.find_element(By.XPATH, '/html/body/app-root/app-root/main/dynamic-comp/div/div/div[1]/div/p/a[2]').click()

