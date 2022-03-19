from selenium import webdriver
import time

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)

driver.get('https://processual.trf1.jus.br/consultaProcessual/nomeParte.php?pg=2&secao=TRF1')

inputElement = driver.find_element_by_id("nome")
inputElement.send_keys('Joao Silva')
inputElement.submit()

flag = 0
limit = 3
for i in range(0, limit):
    time.sleep(3)
    elements = driver.find_elements_by_class_name('listar-processo')
    elements[i].click()
    time.sleep(3)
    elements = driver.find_elements_by_class_name('lista-processo')
    process = elements[i].find_element_by_tag_name('a')
    process.click()
    time.sleep(2)
    driver.execute_script("window.history.go(-1)")
    driver.refresh()