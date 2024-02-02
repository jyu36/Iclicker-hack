from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import datetime
import pytz

# Define the target time (in this case 8:59 AM EST)
target_time = datetime.time(8, 58)

# Get the current time zone
est_timezone = pytz.timezone('US/Eastern')

while True:
    current_time = datetime.datetime.now(est_timezone).time()
    if current_time >= target_time:
        print("It is 8:59 AM EST.")
        break
    else:
        time.sleep(10)

chrome_options = Options()
driver = webdriver.Chrome(options=chrome_options)

service = Service(executable_path="./chromedriver")
driver = webdriver.Chrome(service=service)

# Set geolocation (input your own lattitude and longitude)
coordinates = {
    "latitude": 39.3271792,
    "longitude": -76.619946,
    "accuracy": 100
}

driver.execute_cdp_cmd("Emulation.setGeolocationOverride", coordinates)
driver.get("https://student.iclicker.com/#/login")

# Login (input your own username and password)
time.sleep(2)
login_email_input = driver.find_element(By.ID, "userEmail")
login_email_input.clear()
login_email_input.send_keys("jyu164@jh.edu" + Keys.ENTER)

time.sleep(2)
login_password_input = driver.find_element(By.ID, "userPassword")
login_password_input.clear()
login_password_input.send_keys("Yujiaqiyujia36" + Keys.ENTER)


# Input your class name here
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Mathematical Foundations"))
)

link = driver.find_element(By.PARTIAL_LINK_TEXT, "Mathematical Foundations")
link.click()


WebDriverWait(driver, 3600).until(
    EC.presence_of_element_located((By.CLASS_NAME,"join-title"))
)

while True:
    span_element = driver.find_element(By.CLASS_NAME, "join-title")
    text_content = span_element.text    
    if text_content == "Your instructor started class.":
        break
    else:
        time.sleep(5)
        

time.sleep(2)
join = driver.find_element(By.ID, "btnJoin")
join.click()

lastelement = ""

# Choose your multple choice answer here
while True:
    h1_element = driver.find_element(By.CLASS_NAME, "ng-binding")
    question_text = h1_element.text
    
    print(f"questiontext | {question_text}  lastelement | {lastelement}")
    if question_text != lastelement:
        try:
            WebDriverWait(driver, 60).until(
                EC.presence_of_element_located((By.CLASS_NAME,"multiple-choice-buttons"))
            )

            time.sleep(15)
            answer = driver.find_element(By.ID, "multiple-choice-a")
            answer.click()
            lastelement = question_text
        except Exception as e:
            print(f"An exception occurred {e}")
    else:
        time.sleep(10)



# Quit the WebDriver
driver.quit()
