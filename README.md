# Questionnaire for Coronavirus by Selenium

## Install

#### Download python and selenium

```bash
pip install selenium
```

#### Config Chrome Driver in PC

## Configure

Config your username and password in info.json

```bash
{"username": 123456,"password":"123456"}
```

## Run

```bash
python clockin.py
```

## More

Running code in Linux Server, add

```bash
from selenium.webdriver.chrome.options import Options
from pyvirtualdisplay import Display

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-dev-shm-usage')

display = Display(visible=0, size=(800, 800))
display.start()
driver = webdriver.Chrome(options=chrome_options) # modify original code
```

