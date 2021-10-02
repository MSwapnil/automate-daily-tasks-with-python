from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import yaml
import time

# Opening and loading the YAML file with the credentials
conf = yaml.load(open('credentials.yaml'))

# myEmail and myPassword are the credentials for Salesforce
myEmailSF = conf['user']['email']
myPasswordSF = conf ['user']['password']
urlSF = "https://nutanix.okta.com/login/login.htm?fromURI=%2Fhome%2Fsalesforce%2F0oa3nogxa2RMTWZPZEUU%2F46%3FfromPlugin%3Dtrue"


# email8x8 and password8x8 are the credentials to login to 8x8
email8x8 = conf['8x8']['email']
password8x8 = conf['8x8']['password']
url8x8 = "https://vcc-na7.8x8.com/AGUI/login.php"

# Element ID for username, password and submit button on salesforce page
usernameIdSF = "okta-signin-username"
passwordIdSF = "okta-signin-password"
submit_buttonIdSF = "okta-signin-submit"

# Element ID for username, password and submit button on 8x8 -
usernameId8x8 = "user"
passwordId8x8 = "pass"
submit_buttonId8x8 = "login_b"

# URL of TODO Google sheet
urlTODO = "https://docs.google.com/spreadsheets/d/1RvrsAlk824gViSW8tanxLxHDGy13J6KN_ghsKQygN0o/edit#gid=0"

#Initiating Selenium Webdriver, and specifying Chrome Work profile
options = webdriver.ChromeOptions()
options.add_argument(r"--user-data-dir=/Users/swapnil.mohaniraj/Library/Application Support/Google/Chrome/")
options.add_argument(r'--profile-directory=Profile 6')
driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)


# Function to open Salesforce, enter username/password and click on submit
def loginSF(url,usernameId, username, passwordId, password, submit_buttonId):
    driver.get(url)
    driver.find_element_by_id(usernameId).send_keys(username)
    driver.find_element_by_id(passwordId).send_keys(password)
    driver.find_element_by_id(submit_buttonId).click()


# Function to open a new tab, switch to new tab, open 8x8, enter username/password and click on login, and switch back to SF browser window
def login8x8(url,usernameField8x8,username,passwordField8x8,password, submit_buttonId8x8):
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[1])
    driver.get(url)
    driver.find_element_by_id(usernameField8x8).send_keys(username)
    driver.find_element_by_id(passwordField8x8).send_keys(password)
    driver.find_element_by_id(submit_buttonId8x8).click()
    driver.switch_to.window(driver.window_handles[0])



# Function to open TODO google sheet in a new tab, and switch back to SF tab
def TODOsheets(urlSheets):
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[2])
    driver.get(urlSheets)
    time.sleep(5)
    driver.switch_to.window(driver.window_handles[0])


# calling loginSF, login8x8 and TODOsheets functions
loginSF(urlSF,usernameIdSF, myEmailSF, passwordIdSF, myPasswordSF, submit_buttonIdSF)
login8x8(url8x8,usernameId8x8, email8x8, passwordId8x8, password8x8, submit_buttonId8x8)
TODOsheets(urlTODO)






