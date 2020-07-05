from selenium                           import webdriver
from selenium.webdriver.common.keys     import Keys
from selenium.webdriver.firefox.options import Options
import re

port = 5000
host = 'localhost'
url  = f"http://{host}:{port}"

options = Options()
options.add_argument('-headless')
driver = webdriver.Firefox(options=options)
driver.get(url)
elem = driver.find_element_by_class_name("button")
#
# This part should be fixed
#
try:
    accordion = [line for line in driver.page_source.split('\n') if re.match(r'.*accordion.*display.*', line)]
    elem.click()
    elem.click() # TODO: this is not nice... gotta do something with it.
    accordion = [line for line in driver.page_source.split('\n') if re.match(r'.*accordion.*display.*', line)]
    assert(len(accordion) == 1)
except:
    raise Exception('UI is not loaded correctly.')
finally:
    driver.close()