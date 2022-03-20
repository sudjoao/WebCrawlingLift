from bs4 import BeautifulSoup
from selenium import webdriver
import time
import csv
import constants

def get_initial_data(driver):
    driver.get(constants.SEARCH_URL)
    inputElement = driver.find_element_by_id("nome")
    inputElement.send_keys('Joao Silva')
    inputElement.submit()

def get_current_process(driver, index):
    time.sleep(3)
    process_list_elements = driver.find_elements_by_class_name('listar-processo')
    process_list_elements[index].click()
    time.sleep(3)
    elements = driver.find_elements_by_class_name('lista-processo')
    process = elements[index].find_element_by_tag_name('a')
    process.click()
    time.sleep(2)

def get_process_tabs(driver):
    elements = driver.find_elements_by_class_name('ui-tabs-anchor')
    for element in elements:
        element.click()
        time.sleep(2)


def get_process_rows(driver):
    element = driver.find_element_by_id('aba-processo')
    table = element.find_element_by_tag_name('table')
    rows = table.find_elements_by_tag_name('tr')
    return rows

def print_row_info(row):
    header = row.find_element_by_tag_name('th')
    header_html = BeautifulSoup(header.get_attribute("innerHTML"), "html.parser")
    content = row.find_element_by_tag_name('td')
    content_html = BeautifulSoup(content.get_attribute("innerHTML"), "html.parser")
    print(header_html.text, (content_html.text or "-").strip())

def back_to_process_list_screen(driver):
    driver.execute_script("window.history.go(-1)")
    driver.refresh()

def print_process_rows(rows):
    for row in rows:
        print_row_info(row)
    print("\n")

def create_columns(rows, writer):
    columns = []

    for row in rows:
        header = row.find_element_by_tag_name('th')
        header_html = BeautifulSoup(header.get_attribute("innerHTML"), "html.parser")
        columns.append(header_html.text.replace(":", "").strip())
    
    writer.writerow(columns)

def create_rows(rows, writer):
    contents = []

    for row in rows:
        content = row.find_element_by_tag_name('td')
        content_html = BeautifulSoup(content.get_attribute("innerHTML"), "html.parser")
        contents.append((content_html.text or "-").strip())

    writer.writerow(contents)

if __name__ == "__main__":
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=options)
    get_initial_data(driver)
    limit = 2
    first_process = True
    process_csv_file = open('csvs/process_csv_file.csv', 'w', encoding='utf-8', newline='')
    writer = csv.writer(process_csv_file, delimiter = '\t')

    for i in range(0, limit):
        get_current_process(driver, i)
        rows = get_process_rows(driver)

        if first_process:
            create_columns(rows, writer)
            first_process = False
        get_process_tabs(driver)
        print_process_rows(rows)
        create_rows(rows, writer)
        if i != limit -1:
            back_to_process_list_screen(driver)
    
    driver.close()
