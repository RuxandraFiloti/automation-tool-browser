from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os 
#selenium is python library for browser automation
#credentials for demoqa.com -> username:adda02, pass:Python2025!

class WebAutomation:
    def __init__(self):
        #Define driver options and service
        chrome_options = Options()
        chrome_options.add_argument("--disable-search-engine-choice-screen")
        #Define the path to download the image
        download_path = os.getcwd()
        prefs = {'download.default_directory': download_path }
        chrome_options.add_experimental_option('prefs', prefs)
        service = Service("chromedriver-win64/chromedriver.exe")
        self.driver = webdriver.Chrome(options=chrome_options, service=service)

    def login(self, username, password):
        #Load the web page
        self.driver.get("https://demoqa.com/login")
        #Locate username, password and login button
        username_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'userName')))
        password_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'password')))
        login_button = self.driver.find_element(By.ID, 'login')
        #Fill in username and pass and click the button
        username_field.send_keys(username)
        password_field.send_keys(password)
        self.driver.execute_script("arguments[0].click();", login_button) 


    def fill_form(self, fullname, email, current_address, permanent_address):
        #Locate the Elements dropdown and text box
        elements = (WebDriverWait(self.driver, 10).
                    until(EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div/div/div/div[1]/div/div/div[1]/span/div'))))
        elements.click()    

        text_box = self.driver.find_element(By.ID, 'item-0')
        self.driver.execute_script("arguments[0].click();", text_box) 


        #Locate the form fields and submit button
        full_name_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'userName')))
        email_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'userEmail')))
        current_adress_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'currentAddress')))
        permanent_adress_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'permanentAddress')))
        submit_button = self.driver.find_element(By.ID, 'submit')

        #Fill in the form fields
        full_name_field.send_keys(fullname)
        email_field.send_keys(email)
        current_adress_field.send_keys(current_address)
        permanent_adress_field.send_keys(permanent_address)
        self.driver.execute_script("arguments[0].click();", submit_button)

    def download(self):
        
#Locate the Upload & Download section and the Download button

        upload_download =  (WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "item-7"))))
        upload_download.click()
        download_button = self.driver.find_element(By.ID, 'downloadButton')
        self.driver.execute_script("arguments[0].click();", download_button)

    def close(self):
        self.driver.quit()


if __name__ == "__main__":
    webautomation = WebAutomation()
    webautomation.login('adda02', 'Python2025!')
    webautomation.fill_form("John Smith", "john@gmail.com", "Street 100 NY", "Street 100 NY")
    webautomation.download()
    webautomation.close()