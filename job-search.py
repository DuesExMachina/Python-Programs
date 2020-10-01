from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver= webdriver.Chrome(executable_path='D:\\Softwares\\chromedriver.exe')
driver.maximize_window() # it will maximize the window size

driver.get('https://www.indgovtjobs.in/2014/04/it-fresher-jobs.html')
driver.execute_script("window.open('https://www.fresherscamp.com/');") #it will be change the new tab
driver.execute_script("window.open('https://www.indgovtjobs.in/2013/09/government-jobs-for-engineers-2013-2014.html');")
driver.execute_script("window.open('https://www.sabhijobs.com/qualification/b-e-b-tech/');")
driver.execute_script("window.open('https://www.indgovtjobs.in/2015/03/data-entry-computer-jobs.html');")
driver.execute_script("window.open('https://jobs4fresher.com/');")
#driver.execute_script("window.open('https://https://www.way2fresher.com/jobs/');")
driver.execute_script("window.open('https://offcampusdrive.com/');")
driver.execute_script("windows.open('https://www.offcampusjobs4u.com/');")
option =input('want to close the browser y/n >')
if option=='y':
    driver.quit()
