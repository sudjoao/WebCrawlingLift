from selenium import webdriver
import time

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)

driver.get('https://processual.trf1.jus.br/consultaProcessual/nomeParte.php?pg=2&secao=TRF1')

inputElement = driver.find_element_by_id("nome")
inputElement.send_keys('Joao Silva')
inputElement.submit() 

elements = driver.find_elements_by_class_name('listar-processo')

flag = 0

for element in elements:

    element.click()

    time.sleep(0.05)
    flag += 1
    if flag >= 5:
        break


processos = driver.find_elements_by_class_name('lista-processo')

for processo in processos:

    proc = processo.find_element_by_tag_name('a')

    proc.click()