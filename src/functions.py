from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import os
import time

def set_capture_date(format: str):
    current_date = time.localtime()
    hour = current_date[3]
    minute = current_date[4]
    second = current_date[5]

    capture_name = f"{hour}_{minute}_{second}.{format}"

    return capture_name

def create_daily_output_folder():
    current_date = time.localtime()
    year = current_date[0]
    month = current_date[1]
    day = current_date[2]

    daily_output_folder = f"{day}_{month}_{year}"

    daily_output_path = f'.\screenshots\{daily_output_folder}'
    if not os.path.exists(daily_output_path):
        print("Creatin daily output path....")
        os.makedirs(daily_output_path)
        print("!Daily output path created¡")
    else:
        print("Output already exist.")
    return daily_output_path

def take_screenshot(element, filename):
    element.screenshot(filename)

def int_input_check(input_message: str):
    int_input = input(input_message)
    while int_input.isdigit() != True:
        print("¡Invalid entry!")
        int_input = input(input_message)
    int_input = int(int_input)
    return int_input

def get_fullscreen_screenshot(output_folder: str, driver):
    capture_name = f"full_screenshot_{set_capture_date("png")}"
    fullscreen_screenshot_path = os.path.join(output_folder, capture_name)
    fullscreen_shot = driver.get_screenshot_as_file(fullscreen_screenshot_path)

def get_element_screenshot_cyclic(cycles: int, element_capture, output_folder: str, driver, secs_interval: int, element_type: str, element_name: str):
    for i in range(cycles):
        element = element_capture # content
        capture_name = f"{element_type}_{element_name}_pt{i+1}_{set_capture_date("png")}"
        screenshot_path = os.path.join(output_folder, capture_name)
        take_screenshot(element, screenshot_path)

        next_button = driver.find_element(By.ID, 'next') # next
        next_button.click()
        time.sleep(secs_interval)

def get_element_screenshot(element_capture, output_folder: str, element_type: str, element_name: str):
    element = element_capture # content
    capture_name = f"{element_type}_{element_name}_{set_capture_date("png")}"
    screenshot_path = os.path.join(output_folder, f'{capture_name}')
    take_screenshot(element, screenshot_path)

def element_to_capture(elements: list, driver, element_type: str, element_name: str):
    element_type_name = 0
    geraut = False
    # element_type = input("Enter the type of element to capture: ")
    while True:
        for i in range(0, len(elements)):
            if element_type == elements[i]:
                geraut = True
                break
        if geraut == True:
            break
        if i+1 == len(elements) and geraut == False:
            element_type_name = f"ERROR: {element_type} is a non-existent element."
        break

    print(len(elements))
    if type(element_type_name) != str:
        # element_name = input(f"Enter the name of ({element_type}) element: ")

        element_type_name = ""
        if element_type.lower() == 'id':
            try:
                element_type_name = driver.find_element(By.ID, element_name) # type: ignore
            except:
                element_type_name = f"ERROR: the name {element_name} of element {element_type} does not exist"
        elif element_type.lower() == 'class':
            try:
                element_type_name = driver.find_element(By.CLASS_NAME, element_name) # type: ignore
            except:
                element_type_name = f"ERROR: the name {element_name} of element {element_type} does not exist"
        elif element_type.lower() == 'name':
            try:
                element_type_name = driver.find_element(By.NAME, element_name) # type: ignore
            except:
                element_type_name = f"ERROR: the name {element_name} of element {element_type} does not exist"
        elif element_type.lower() == 'tag name':
            try:
                element_type_name = driver.find_element(By.TAG_NAME, element_name) # type: ignore
            except:
                element_type_name = f"ERROR: the name {element_name} of element {element_type} does not exist"
        elif element_type.lower() == 'link text':
            try:
                element_type_name = driver.find_element(By.LINK_TEXT, element_name) # type: ignore
            except:
                element_type_name = f"ERROR: the name {element_name} of element {element_type} does not exist"
    else:
        element_type_name = f"'{element_type}' is a non-existent element in URL."
    return element_type_name