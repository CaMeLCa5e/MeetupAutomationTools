"""
Meetup login and join
"""

from selenium import webdriver

driver = webdriver.Firefox()
driver.get("https://secure.meetup.com/login/")

username = driver.find_element_by_id('email')
username.send_keys('XXX@gmail.com')

password = driver.find_element_by_id('password')
password.send_keys('XXX')
password.submit()

driver.get('http://www.meetup.com/nycpython/')
driver.get('http://www.meetup.com/nycpython/join/')


# driver.find_element_by_id('pickNoPhoto').click
# join.submit()
# driver.close()