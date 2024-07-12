from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
import time

driver = webdriver.Chrome()
driver.get('https://accounts.spotify.com/tr/login?continue=https%3A%2F%2Fopen.spotify.com%2Fuser%2F31bv4hwlp3xnaumn5laycpkglioy')

# Oturum açma bilgileri
email = "gmail"
password = "password"    

# Fill in the email field
email_field = driver.find_element(By.XPATH,'//*[@id="login-username"]')
email_field.send_keys(email)

# Fill in the password field
password_field = driver.find_element(By.XPATH,'//*[@id="login-password"]')
password_field.send_keys(password)

# Click the login button
login_button = driver.find_element(By.XPATH,'//*[@id="login-button"]/span[1]')
login_button.click()

time.sleep(5)

# Click the "Takip Edilenler" link
takip_edilenler_link = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="main"]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/section/div/div[1]/div[5]/div/span[3]/a')))
takip_edilenler_link.click()
time.sleep(2)

# Find all the profile links
# Profil sayısı
num_profiles = 400

# Her bir profil için döngü oluştur
for i in range(150, num_profiles + 1):    
    # XPath ifadesini oluştur
    profile_xpath = driver.find_elements(By.XPATH,'//*[@id="main"]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/section/section/div[2]/div[{}]/div/div[3]'.format(i))

    for profile_xpath in profile_xpath:
        # Go to the profile page
        profile_xpath.click()

        # Check if already following
        follow_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="main"]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/section/div/div[3]/div[4]/div/div/div/div/button[1]')))
        follow_button_text = follow_button.text.strip()

        if follow_button_text.lower() == "takip ediliyor":
            profile_name = driver.find_element(By.XPATH, '//*[@id="main"]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/section/div/div[1]/div[5]/span[2]/h1').text.strip()
            print("Zaten takip ediliyor: " + profile_name)
        else:
            # Click the follow button
            follow_button.click()
            profile_name = driver.find_element(By.XPATH, '//*[@id="main"]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/section/div/div[1]/div[5]/span[2]/h1').text.strip()
            print("Takip Edildi: " + profile_name)
            time.sleep(1)

        # Go back to the "Takip Edilenler" page
        driver.back()
        time.sleep(1)


# Close the browser
driver.quit()
