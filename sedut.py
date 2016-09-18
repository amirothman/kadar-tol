from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.common.keys import Keys

def extract_content(driver):
    tbody = driver.find_element_by_tag_name("tbody")
    return tbody.text

def iterate_combo_box(driver,id_name):
    box = driver.find_element_by_id(id_name)
    options = [(option.get_attribute("value"),option.text) for option in box.find_elements_by_tag_name("option")]

    for option,label in options:
        box = driver.find_element_by_id(id_name)
        select_box = Select(box)
        select_box.select_by_value(option)
        yield (label,extract_content(driver))

try:
    driver = webdriver.Chrome('./chromedriver')
    driver.get("http://kadartol.llm.gov.my/Default.aspx")
    box = driver.find_element_by_id("MainContent_ASPxComboBox1")
    options = [(option.get_attribute("value"),option.text) for option in box.find_elements_by_tag_name("option")]
    # labels = []
    for option,label in options:
        try:
            # print(option,label)
            box = driver.find_element_by_id("MainContent_ASPxComboBox1")
            selected_box = Select(box)
            selected_box.select_by_value(option)
            try:
                for second_label,_ in iterate_combo_box(driver,"MainContent_ASPxComboBox2"):
                    for third_label,content in iterate_combo_box(driver,"MainContent_ASPxComboBox3"):
                        print(label,second_label,third_label,content)
            except EC.NoSuchElementException:
                try:
                    for second_label,content in iterate_combo_box(driver,"MainContent_ASPxComboBox2"):
                        print(label,second_label,content)
                except EC.NoSuchElementException:
                    pass
        except EC.NoSuchElementException:
            try:
                for second_label,content in iterate_combo_box(driver,"MainContent_ASPxComboBox2"):
                    print(label,second_label,content)
                kembali = driver.find_element_by_id("MainContent_Button2")
                kembali.click()
            except EC.NoSuchElementException:
                for second_label,content in iterate_combo_box(driver,"MainContent_ASPxComboBox2"):
                    print(label,second_label,content)
                kembali = driver.find_element_by_id("MainContent_Button1")
                kembali.click()
finally:
    driver.quit()
