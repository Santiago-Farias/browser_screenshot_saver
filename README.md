# Browser screenshot downloader

## Overview

This repository hosts an application that captures segments of the website that the user sets. The main goal is to explore tools that allow controlling a browser automatically and make screenshots of it.

## Key Features

- **Capture full screen of website**
- **Capture a segment of the website:** After the user set a element to capture and his name, this app will capture it.
- **Capture a secuencie of screenshots:** The user can set a number of captures to do, and the interval between those.
- **Capture by environment changes:** The user can autimatize captures if before needs to do a clic in some element.

## Were used Python and some of his libraries

## Development Setup

1. Clone the repository:
  ```bash
  git clone https://github.com/Santiago-Farias/browser_screenshot_saver.git
  cd browser_screenshot_saver
  ```

2. Download the Chrome Driver from: https://googlechromelabs.github.io/chrome-for-testing/
   - Unzip de file, copy his path and to the end of the path type: chromedriver.exe.
   
     Example: C:/Users/Carlos/Downloads/chromedriver-win64/chromedriver.exe
   - Paste the path in indicated section in the code of main.py file. 

3. You need a Python 3.13 or higher.

4. Create and turn up a virtual environment:
   
    Windows
    ```bash
    python -m venv env
    env\Scripts\activate
    ```
    Linux/Mac
    ```
    python -m venv env
    source env/bin/activate
    ```

5. Install dependencies:
  ```bash
  pip install -r requirements.txt
  ```

6. Set the url of the website in indicated section in the code of main.py file.
  
7. Star the app:
  ```
  python main.py
  ```

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any changes.
