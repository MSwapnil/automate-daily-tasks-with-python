from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager

import yaml

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

login(url,usernameId, myEmail, passwordId, myPassword, submit_buttonId)





