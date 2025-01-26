from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time
from PIL import Image
import os
from functions import *
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--log-level=1")
driver = webdriver.Chrome(options=options)

service = Service('-') # Set you ChromeDriver Path using '/' separator
driver = webdriver.Chrome(service=service)
driver.get('https://browser-screenshot-saver.vercel.app/') # Set website, 'https://browser-screenshot-saver.vercel.app/' by default
elements = ['id', 'class', 'name', 'tag name', 'link text']
menu_option_input = 0
cycles = int

daily_output_folder_path = create_daily_output_folder()

while True:
    print("1. Capture an element and continue capturing after clicking")
    print("2. Capture an element")
    print("3. Capture a full screen of current screen")
    print("4. Exit")

    menu_option_input = int_input_check("Enter a option: ")

    if menu_option_input == 1:
        element_type = input("Enter the type of element to capture: ")
        element_name = input(f"Enter the name of ({element_type}) element: ")
        element_capture = element_to_capture(elements, driver, element_type, element_name)
        if type(element_capture) != str:
            cycles = int_input_check("Enter the number of captures do you want to do of a element: ")
            if cycles > 1:
                secs_interval = int_input_check("Enter the seconds interval between captures: ")
            else:
                secs_interval = 0
            print("Capturing elemnt...")
            get_element_screenshot_cyclic(cycles, element_capture, daily_output_folder_path, driver, secs_interval, element_type, element_name)
            print("¡Element captured!")
        else:
            print(element_capture)
    elif menu_option_input == 2:
        element_type = input("Enter the type of element to capture: ")
        element_name = input(f"Enter the name of ({element_type}) element: ")
        element_capture = element_to_capture(elements, driver, element_type, element_name)
        if type(element_capture) != str:
            print("Capturing elemnt...")
            get_element_screenshot(element_capture, daily_output_folder_path, element_type, element_name)
            print("¡Element captured!")
        else:
            print(element_capture)
    elif menu_option_input == 3:
        print("Capturing the full screen...")
        get_fullscreen_screenshot(daily_output_folder_path, driver)
        print("¡Screen captured!")
    elif menu_option_input == 4:
        print("Leaving please wait..")
        driver.quit()
        break
    else:
        print("Numeber of option doesn't exist")

driver.quit()