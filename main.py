from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.by import By 
options = webdriver.ChromeOptions()
options.add_extension('MetaMask.crx')

driver = webdriver.Chrome(ChromeDriverManager().install(),options=options)
driver.get("https://opensea.io/login")
sleep(10)
metamask_window_id = ""
open_area_id = ""
for handle in driver.window_handles:
    driver.switch_to.window(handle)
    title = driver.title
    if title =="MetaMask":
        metamask_window_id = handle
    if "Login" in title:
        open_area_id = handle
    if title == "":
        driver.close()

if not metamask_window_id:
    raise ValueError("No meta mask tab found :)")
if not open_area_id:
    raise ValueError("No OpenSea tab found :)")


def switch_to_meta_tab():
    driver.switch_to.window(metamask_window_id)
    for handle in driver.window_handles:
        driver.switch_to.window(handle)
        title = driver.title
        if "MetaMask" in title:
            return driver
    
def switch_to_open_tab():
    driver.switch_to.window(open_area_id)
def wait(path):
    element = WebDriverWait(driver,20).until( 
 EC.visibility_of_element_located((By.XPATH,path)) 
) 



switch_to_meta_tab()
driver.find_element_by_xpath('//button[text()="Get Started"]').click()
driver.find_element_by_xpath('//button[text()="Import wallet"]').click()
driver.find_element_by_xpath('//button[text()="No Thanks"]').click()
wait("//input")
inputs = driver.find_elements_by_xpath('//input')
inputs[0].send_keys("account exhaust scout device pigeon chase raccoon learn coin daughter blind edit")
inputs[1].send_keys("Test123MetaMask")
inputs[2].send_keys("Test123MetaMask")
driver.find_element_by_css_selector('.first-time-flow__terms').click()
driver.find_element_by_xpath('//button[text()="Import"]').click()

wait('//button[text()="All Done"]')
driver.find_element_by_xpath('//button[text()="All Done"]').click()
driver.find_element(By.XPATH, '//button[@title="Close"]').click()
driver.close()
switch_to_open_tab()
print(driver.title)
wait("//span[text()='MetaMask']")
driver.find_element(By.XPATH, "//span[text()='MetaMask']").click()
sleep(2)
driver = switch_to_meta_tab()
print(driver.window_handles)
sleep(20)

driver.close()
