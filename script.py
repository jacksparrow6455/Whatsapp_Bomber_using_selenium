#Importing Selenium
from selenium import webdriver

#Adding Chrome Drivers to automate Chrome 
driver=webdriver.Chrome("./chromedriver")
driver.get("https://web.whatsapp.com/")

#Adding Wait time
input("Press a key after the Whatsapp page is loaded")

#Edit the Contact Name
user = driver.find_element_by_xpath('//span[@title = "Your Contact Name"]')
user.click()
msg=input("Enter message")
msg_box = driver.find_element_by_class_name('_2S1VP')
for i in range(100):
    msg_box.send_keys(msg)
    button = driver.find_element_by_class_name('_35EW6')
    print("Sent",i)
    button.click() 