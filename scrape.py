"""
The Webscraping part of this application
"""

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
from time import sleep


def open_Letto_page(webdriver,url):
    webdriver.get(url)

def close_Letto_page(webdriver):
    webdriver.close()

def on_login_screen(webdriver):
    try:
        webdriver.find_element_by_id("j_idt17:username")
    except NoSuchElementException:
        return False
    else:
        return True

def autologin_to_Letto(webdriver, login_details):
    username_field = webdriver.find_element_by_id("j_idt17:username")
    password_field = webdriver.find_element_by_id("j_idt17:pwd")
    username_field.send_keys(login_details["username"])
    password_field.send_keys(login_details["password"])
    password_field.send_keys(Keys.RETURN)


def scrape_image_url(webdriver,image_src_url):
    try:
        answer_div = webdriver.find_element_by_id("answer")
        image = answer_div.find_element_by_tag_name("img")
        image_src_url = image.get_attribute("src")
    except NoSuchElementException:
        pass

    return image_src_url



def scrape_task_data(webdriver): #using the url of the image of a task to tetermine, if a new task is rendered.

    answer_div = webdriver.find_element_by_id("answer")    

    task_data_paragraph = answer_div.find_elements_by_tag_name("p")[1]

    task_data = []

    for mjx_math_element in task_data_paragraph.find_elements_by_class_name("mjx-math"):
        data_string = ""

        for mjx_char in mjx_math_element.find_elements_by_class_name("mjx-char"):
            data_string += mjx_char.get_attribute("innerHTML")

        task_data.append(data_string)


    return task_data


def write_to_input_fields(webdriver,solutions):

    answer = webdriver.find_element_by_id("answer")
    input_fields = answer.find_elements_by_class_name("ui-inputfield")

    counter = 0
    for input_field in input_fields:
        input_field.clear()
        input_field.send_keys(solutions[counter])
        counter += 1

def next_task(webdriver):
    form_div = webdriver.find_element_by_id("questionForm:rm")
    for button in form_div.find_elements_by_class_name("ui-button-text"):
        if button.get_attribute("innerHTML") == "Nächste Frage":
            button.click()
    
