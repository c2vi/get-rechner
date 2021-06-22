"""
Main Python file for the app to automate GET-Lettos
"""
import time

from calculate import *
from scrape import *
from selenium import webdriver
from image import is_equal, get_img

PATH_TO_WEBDRIVER = r"webdriver/geckodriver"
URL = "https://letto.htlinn.ac.at/letto/main.jsf"


# ----------------------------------------------------------------


def main():
    # initiate the selenium Webdriver
    selenium_driver = webdriver.Firefox()
    open_Letto_page(selenium_driver, URL)
    login_details = read_login_details_file()
    # autologin
    try:
        if on_login_screen(selenium_driver):
            autologin_to_Letto(selenium_driver, login_details)
        print(f'Logged in automatically as {login_details["name"]}')
        input("Navigate to the task, that should be done and press enter:")

    except FileNotFoundError:
        print("No file called login-details.txt found. proceeding to manual login")
        print("Login to Letto, and go to the task, that should be done.")
        input("Then press enter:")
    x = 0
    while True:
        # scraping from the task
        task_data = scrape_task_data(selenium_driver)

        # TODO: scraping the image
        image = scrape_image(selenium_driver)
        try:
            get_img(selenium_driver)
        except NoSuchElementException:
            input("Element not found?")
            continue
        num = is_equal("filename.png")

        solutions = calculate(task_data, int(num))

        write_to_input_fields(selenium_driver, solutions)

        inp = input("stop[everything] or next[enter]")
        if inp == "":
            # next_(selenium_driver)
            # input("loaded?")
            continue
        else:
            break

    # closing the Browser
    close_Letto_page(selenium_driver)


def read_login_details_file():
    with open("login-details.txt") as login_details_file:
        details_array = login_details_file.read().split("\n")
    return {
        "name": details_array[0],
        "username": details_array[1],
        "password": details_array[2]
    }


# ----------------------------------------------------------------

if __name__ == '__main__':
    main()
