import selenium
from selenium import webdriver
from getpass import getpass
from time import sleep 
  

print("Enter EmailID")
usr=input()
pwd=getpass("Enter the Password")

driver = webdriver.Chrome(executable_path=r"C:\Users\Lenovo\Downloads")
driver.get('https://www.facebook.com/') 
print ("Opened facebook") 
sleep(1) 
  
username_box = driver.find_element_by_id('email') 
username_box.send_keys(usr) 
print ("Email Id entered") 
sleep(1) 
  
password_box = driver.find_element_by_id('pass') 
password_box.send_keys(pwd) 
print ("Password entered") 
  
login_box = driver.find_element_by_id('loginbutton') 
login_box.click() 
  
print ("Done") 
input('Press anything to quit') 
driver.quit() 
print("Finished")
