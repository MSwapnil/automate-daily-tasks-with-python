from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager

import yaml
import time

conf = yaml.load(open('credentials.yaml'))
myEmail = conf['user']['email']
myPassword = conf ['user']['password']
url = "https://nutanix.okta.com/login/login.htm?fromURI=%2Fhome%2Fsalesforce%2F0oa3nogxa2RMTWZPZEUU%2F46%3FfromPlugin%3Dtrue"

options = webdriver.ChromeOptions()
options.add_argument(r"--user-data-dir=/Users/swapnil.mohaniraj/Library/Application Support/Google/Chrome/")
options.add_argument(r'--profile-directory=Profile 6')
driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)

usernameId = "okta-signin-username"
passwordId = "okta-signin-password"
submit_buttonId = "okta-signin-submit"

def login(url,usernameId, username, passwordId, password, submit_buttonId):
    driver.get(url)
    driver.find_element_by_id(usernameId).send_keys(username)
    driver.find_element_by_id(passwordId).send_keys(password)
    driver.find_element_by_id(submit_buttonId).click()
    time.sleep(30)
    print ("15 seconds over")
#return driver.find_element_by_id("00B0e000007H6tM_refresh")


url2 = "https://nutanix.my.salesforce.com/console"
#refresh_button = "00B0e000007H6tM_refresh"

login(url,usernameId, myEmail, passwordId, myPassword, submit_buttonId)

def refresh (url2):
    driver.get(url)
    driver.find_element_by_css_selector("[title='Refresh']").click()

def reload():
    while True:
        refresh(url)
        time.sleep(10)
        print("10 seconds over")

reload()



