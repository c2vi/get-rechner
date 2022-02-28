"""
Main Python file for the app to automate GET-Lettos
"""
from selenium import webdriver
from scrape import *
from calculate import *
from time import sleep

AUTO_NEXT_TASK = True
PATH_TO_WEBDRIVER = "./webdriver/geckodriver"
URL = "https://letto.htlinn.ac.at/letto/main.jsf"

def main():

#----------------------------------------------------------------

    #initiate the selenium Webdriver
    selenium_driver = webdriver.Firefox(executable_path=PATH_TO_WEBDRIVER)
    open_Letto_page(selenium_driver,URL)

    #autologin
    try:
        if on_login_screen(selenium_driver):
            login_details = read_login_details_file()
            autologin_to_Letto(selenium_driver, login_details)
        print(f'Logged in automatically as {login_details["name"]}')
#        input("Navigate to the task, that should be done and press enter:")

    except FileNotFoundError:
        print("No file called login-details.txt found. proceeding to manual login")
        print("Login to Letto, and go to the task, that should be done.")
#        input("Then press enter:") 

    #using the url of the image of a task to tetermine, if a new task is rendered.
    image_src_url = "nothing"
    while True:
        
        print("waiting for a Task to be opened")
        while scrape_image_url(selenium_driver,image_src_url) == image_src_url:
            sleep(0.2)
            
        image_src_url = scrape_image_url(selenium_driver,image_src_url)

        #scraping from the task
        task_data = scrape_task_data(selenium_driver)

        solutions = calculate(task_data)
        write_to_input_fields(selenium_driver,solutions)
        if AUTO_NEXT_TASK:
            next_task(selenium_driver)
        print("task finished....")

    #closing the Browser

    close_Letto_page(selenium_driver)

#----------------------------------------------------------------




def read_login_details_file():
    with open("login-details.txt") as login_details_file:
        details_array = login_details_file.read().split("\n")
    return {
        "name":details_array[0],
        "username":details_array[1],
        "password":details_array[2]
    }


if __name__ == '__main__':
    main()
