#By: Almog Shtaigmann

#Make sure that Python is installed on your system!!

#To install selenium:
#open cmd\terminal - pip install selenium

#To download chromedriver - https://sites.google.com/chromium.org/driver/
#Choose the version that matches your broswer
#Save and extract the file, then move to any place you want and copy the path of the file


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#The OpenU login URL
WEBSEITE_URL = "https://sso.apps.openu.ac.il/login?T_PLACE=https://sheilta.apps.openu.ac.il/pls/dmyopt2/sheilta.main"

#Path for chromedrive.exe file
#For Mac users remove the '.exe'
PATH_FOR_DRIVER = "PATH\chromedriver.exe"

#Student information, replace with your login information:
USER_NAME = "user_name"
PASSWORD = "password"
ID = "id"

#Set the driver
driver = webdriver.Chrome(PATH_FOR_DRIVER)

#Open the OpenU login page
driver.get(WEBSEITE_URL)

# Get element with tag name 'p_user' -> student name
element = driver.find_element(By.ID, 'p_user')
#Send the student name
element.send_keys(USER_NAME)

# Get element with tag name 'p_sisma' -> student password
element = driver.find_element(By.ID, 'p_sisma')
#Send the student password
element.send_keys(PASSWORD)

# Get element with tag name 'p_mis_student' -> student ID
element = driver.find_element(By.ID, 'p_mis_student')
#Send the student ID
element.send_keys(ID)

#Press enter to log in
element.send_keys(Keys.ENTER)



