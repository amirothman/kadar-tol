from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.common.keys import Keys

import time

def extract_content(driver):
    tbody = driver.find_element_by_tag_name("tbody")
    return tbody.text

def iterate_combo_box(id_name="MainContent_ASPxComboBox3"):
    third_box = driver.find_element_by_id(id_name)
    third_options = [(third_option.get_attribute("value"),third_option.text) for third_option in third_box.find_elements_by_tag_name("option")]

    for third_option,third_label in third_options:
        third_box = driver.find_element_by_id(id_name)
        select_third_box = Select(third_box)
        select_third_box.select_by_value(third_option)
        print(third_label,extract_content(driver))

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
                third_box = driver.find_element_by_id("MainContent_ASPxComboBox3")
                second_box = driver.find_element_by_id("MainContent_ASPxComboBox2")
                second_options = [(second_option.get_attribute("value"),second_option.text) for second_option in second_box.find_elements_by_tag_name("option")]
                for second_option,second_label in second_options:
                    # print(second_option,second_label)
                    second_box = driver.find_element_by_id("MainContent_ASPxComboBox2")
                    select_second_box = Select(second_box)
                    select_second_box.select_by_value(second_option)
                    # third_box = driver.find_element_by_id("MainContent_ASPxComboBox3")
                    # third_options = [(third_option.get_attribute("value"),third_option.text) for third_option in third_box.find_elements_by_tag_name("option")]
                    #
                    # for third_option,third_label in third_options:
                    #     third_box = driver.find_element_by_id("MainContent_ASPxComboBox3")
                    #     select_third_box = Select(third_box)
                    #     select_third_box.select_by_value(third_option)
                    #     print(label,second_label,third_label)
                    #     print(extract_content(driver))
            except EC.NoSuchElementException:
                try:
                    second_box = driver.find_element_by_id("MainContent_ASPxComboBox2")
                    second_options = [(second_option.get_attribute("value"),second_option.text) for second_option in second_box.find_elements_by_tag_name("option")]
                    for second_option,second_label in second_options:
                        second_box = driver.find_element_by_id("MainContent_ASPxComboBox2")
                        select_second_box = Select(second_box)
                        select_second_box.select_by_value(second_option)
                        print(label,second_label)
                        print(extract_content(driver))
                except EC.NoSuchElementException:
                    pass
        except EC.NoSuchElementException:
            try:
                second_box = driver.find_element_by_id("MainContent_ASPxComboBox2")
                second_options = [(second_option.get_attribute("value"),second_option.text) for second_option in second_box.find_elements_by_tag_name("option")]
                for second_option,second_label in second_options:
                    second_box = driver.find_element_by_id("MainContent_ASPxComboBox2")
                    select_second_box = Select(second_box)
                    select_second_box.select_by_value(second_option)
                    print(label,second_label)
                    print(extract_content(driver))
                kembali = driver.find_element_by_id("MainContent_Button2")
                kembali.click()
            except EC.NoSuchElementException:
                second_box = driver.find_element_by_id("MainContent_ASPxComboBox2")
                second_options = [(second_option.get_attribute("value"),second_option.text) for second_option in second_box.find_elements_by_tag_name("option")]
                for second_option,second_label in second_options:
                    second_box = driver.find_element_by_id("MainContent_ASPxComboBox2")
                    select_second_box = Select(second_box)
                    select_second_box.select_by_value(second_option)
                    print(label,second_label)
                    print(extract_content(driver))
                kembali = driver.find_element_by_id("MainContent_Button1")
                kembali.click()
finally:
    driver.quit()
