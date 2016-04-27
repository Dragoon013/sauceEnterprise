from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support import expected_conditions as EC

import random
# This is the only code you need to edit in your existing scripts.
# The command_executor tells the test to run on Sauce, while the desired_capabilities
# parameter tells us which browsers and OS to spin up.
desired_cap = {
    'platform': "Mac OS X 10.9",
    'browserName': "chrome",
    'version': "31",
}
driver = webdriver.Remote(
   command_executor='http://dragoon013:b89b7205-3aca-4af2-a618-9bab4c7bdebd@ondemand.saucelabs.com:80/wd/hub',
   desired_capabilities=desired_cap)

# This is your test logic. You can add multiple tests here.
driver.get("localhost:8082")
#driver.implicitly_wait(100)
try:
    elem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "game_area")))
    #elem = driver.find_element_by_id("game_area")

    #    for index in range(25):
    #      cool = random.random() * 4
    #       if cool % 4 == 0:
    elem.click()
    elem.send_keys(Keys.ARROW_DOWN)
    #     elif cool % 4 == 1:
    elem.send_keys(Keys.ARROW_RIGHT)
    #    elif cool % 4 == 2:
    elem.send_keys(Keys.ARROW_LEFT)
    #   elif cool % 4 == 3:
    elem.send_keys(Keys.ARROW_UP)
    elem.submit()
finally:
    driver.quit()
    #if not "" in driver.title:
 #   raise Exception("Unable to load google page!")

#print driver.title

# This is where you tell Sauce Labs to stop running tests on your behalf.
# It's important so that you aren't billed after your test finishes.
#driver.quit()
