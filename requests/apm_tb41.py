from selenium import webdriver
from time import sleep
import sqlite3



driver = webdriver.Chrome()
driver.get('https://stud.sssu.ru/WebApp/#/Rasp/Group/23163')
sleep(7)


#name_group = driver.find_element_by_xpath('//*[@id="inspire"]/div/main/div/div[4]/div/div/div[4]/div/div[1]/a/div/div[2]/span')
#name_week = driver.find_element_by_xpath('//*[@id="inspire"]/div/main/div/div[4]/div/div/div[4]/div/div[4]/div/div/div[2]')
base = sqlite3.connect('rasp.db')
cur = base.cursor()

base.execute('CREATE TABLE IF NOT EXISTS {}(name)'.format('apm_tb41'))
base.commit()

try:
    name_week = driver.find_element_by_xpath('//*[@id="input-176"]"]').text
    cur.execute('INSERT INTO apm_tb41 VALUES(?);', (name_week,))
    base.commit()
except:
    print ("Значений не найдено, пропускаю")


##Понедельник
try:
    monday = driver.find_element_by_xpath('//*[@id="page-main"]/div/div/div[6]/div/div/div[1]/div/header/div/div[1]').text
    cur.execute('INSERT INTO apm_tb41 VALUES(?);', (monday,))
    base.commit()
except:
    print ("Значений не найдено, пропускаю")

##1 пара (начало)
try:
    monday_time_1 = driver.find_element_by_xpath('//*[@id="page-main"]/div/div/div[6]/div/div/div[1]/div/div/div[1]/div/div[1]').text
    cur.execute('INSERT INTO apm_tb41 VALUES(?);', (monday_time_1,))
    base.commit()
except:
    print ("Значений не найдено, пропускаю")


try:
    monday_name_1 = driver.find_element_by_xpath('//*[@id="page-main"]/div/div/div[6]/div/div/div[1]/div/div/div[1]/div/div[2]/div/div/span[1]').text
    cur.execute('INSERT INTO apm_tb41 VALUES(?);', (monday_name_1,))
    base.commit()
except:
    print ("Значений не найдено, пропускаю")


try:
    monday_teacher_1 = driver.find_element_by_xpath('//*[@id="page-main"]/div/div/div[6]/div/div/div[1]/div/div/div[1]/div/div[2]/div/span[1]').text
    cur.execute('INSERT INTO apm_tb41 VALUES(?);', (monday_teacher_1,))
    base.commit()
except:
    print ("Значений не найдено, пропускаю")


try:
    monday_aud_1 = driver.find_element_by_xpath('//*[@id="page-main"]/div/div/div[6]/div/div/div[1]/div/div/div[1]/div/div[2]/div/span[2]').text
    cur.execute('INSERT INTO apm_tb41 VALUES(?);', (monday_aud_1,))
    base.commit()
except:
    print ("Значений не найдено, пропускаю")
##1 пара (конец)

##2 пара (начало)
try:
    monday_time_2 = driver.find_element_by_xpath('//*[@id="page-main"]/div/div/div[6]/div/div/div[1]/div/div/div[2]/div/div[1]').text
    cur.execute('INSERT INTO apm_tb41 VALUES(?);', (monday_time_2,))
    base.commit()
except:
    print("Значений не найдено, пропускаю")

try:
    monday_name_2 = driver.find_element_by_xpath('//*[@id="page-main"]/div/div/div[6]/div/div/div[1]/div/div/div[2]/div/div[2]/div/div[2]/span[1]').text
    cur.execute('INSERT INTO apm_tb41 VALUES(?);', (monday_name_2,))
    base.commit()
except:
    print("Значений не найдено, пропускаю")

try:
    monday_teacher_2 = driver.find_element_by_xpath('//*[@id="page-main"]/div/div/div[6]/div/div/div[1]/div/div/div[2]/div/div[2]/div/span[1]').text
    cur.execute('INSERT INTO apm_tb41 VALUES(?);', (monday_teacher_2,))
    base.commit()
except:
    print("Значений не найдено, пропускаю")

try:
    monday_aud_2 = driver.find_element_by_xpath('//*[@id="page-main"]/div/div/div[6]/div/div/div[1]/div/div/div[2]/div/div[2]/div/span[2]').text
    cur.execute('INSERT INTO apm_tb41 VALUES(?);', (monday_aud_2,))
    base.commit()
except:
    print("Значений не найдено, пропускаю")
##2 пара (конец)


##3 пара (начало)
try:
    monday_time_3 = driver.find_element_by_xpath('//*[@id="page-main"]/div/div/div[6]/div/div/div[1]/div/div/div[3]/div/div[1]').text
    cur.execute('INSERT INTO apm_tb41 VALUES(?);', (monday_time_3,))
    base.commit()
except:
    print("Значений не найдено, пропускаю")

try:
    monday_name_3 = driver.find_element_by_xpath('//*[@id="page-main"]/div/div/div[6]/div/div/div[1]/div/div/div[3]/div/div[2]/div/div[2]/span[1]').text
    cur.execute('INSERT INTO apm_tb41 VALUES(?);', (monday_name_3,))
    base.commit()
except:
    print("Значений не найдено, пропускаю")

try:
    monday_teacher_3 = driver.find_element_by_xpath('//*[@id="page-main"]/div/div/div[6]/div/div/div[1]/div/div/div[3]/div/div[2]/div/span[1]').text
    cur.execute('INSERT INTO apm_tb41 VALUES(?);', (monday_teacher_3,))
    base.commit()
except:
    print("Значений не найдено, пропускаю")

try:
    monday_aud_3 = driver.find_element_by_xpath('//*[@id="page-main"]/div/div/div[6]/div/div/div[1]/div/div/div[3]/div/div[2]/div/span[2]').text
    cur.execute('INSERT INTO apm_tb41 VALUES(?);', (monday_aud_3,))
    base.commit()
except:
    print("Значений не найдено, пропускаю")
##3 пара (конец)


##4 пара (начало)
try:
    monday_time_4 = driver.find_element_by_xpath('//*[@id="page-main"]/div/div/div[6]/div/div/div[1]/div/div/div[4]/div/div[1]').text
    cur.execute('INSERT INTO apm_tb41 VALUES(?);', (monday_time_4,))
    base.commit()
except:
    print("Значений не найдено, пропускаю")

try:
    monday_name_4 = driver.find_element_by_xpath('//*[@id="page-main"]/div/div/div[6]/div/div/div[1]/div/div/div[4]/div/div[2]/div/div[2]/span[1]').text
    cur.execute('INSERT INTO apm_tb41 VALUES(?);', (monday_name_4,))
    base.commit()
except:
    print("Значений не найдено, пропускаю")

try:
    monday_teacher_4 = driver.find_element_by_xpath('//*[@id="page-main"]/div/div/div[6]/div/div/div[1]/div/div/div[4]/div/div[2]/div/span[1]').text
    cur.execute('INSERT INTO apm_tb41 VALUES(?);', (monday_teacher_4,))
    base.commit()
except:
    print("Значений не найдено, пропускаю")

try:
    monday_aud_4 = driver.find_element_by_xpath('//*[@id="page-main"]/div/div/div[6]/div/div/div[1]/div/div/div[4]/div/div[2]/div/span[2]').text
    cur.execute('INSERT INTO apm_tb41 VALUES(?);', (monday_aud_4,))
    base.commit()
except:
    print("Значений не найдено, пропускаю")
##4 пара (конец)


##5 пара (начало)
try:
    monday_time_5 = driver.find_element_by_xpath('//*[@id="page-main"]/div/div/div[6]/div/div/div[1]/div/div/div[5]/div/div[1]').text
    cur.execute('INSERT INTO apm_tb41 VALUES(?);', (monday_time_5,))
    base.commit()
except:
    print("Значений не найдено, пропускаю")

try:
    monday_name_5 = driver.find_element_by_xpath('//*[@id="page-main"]/div/div/div[6]/div/div/div[1]/div/div/div[5]/div/div[2]/div/div[2]/span[1]').text
    cur.execute('INSERT INTO apm_tb41 VALUES(?);', (monday_name_5,))
    base.commit()
except:
    print("Значений не найдено, пропускаю")

try:
    monday_teacher_5 = driver.find_element_by_xpath('//*[@id="page-main"]/div/div/div[6]/div/div/div[1]/div/div/div[5]/div/div[2]/div/span[1]]').text
    cur.execute('INSERT INTO apm_tb41 VALUES(?);', (monday_teacher_5,))
    base.commit()
except:
    print("Значений не найдено, пропускаю")

try:
    monday_aud_5 = driver.find_element_by_xpath('//*[@id="page-main"]/div/div/div[6]/div/div/div[1]/div/div/div[5]/div/div[2]/div/span[2]').text
    cur.execute('INSERT INTO apm_tb41 VALUES(?);', (monday_aud_5,))
    base.commit()
except:
    print("Значений не найдено, пропускаю")
##5 пара (конец)


##Вторник
try:
    tuesday = driver.find_element_by_xpath('//*[@id="page-main"]/div/div/div[6]/div/div/div[2]/div/header/div/div[1]').text
    cur.execute('INSERT INTO apm_tb41 VALUES(?);', (tuesday,))
    base.commit()
except:
    print ("Значений не найдено, пропускаю")

##1 пара (начало)
try:
    tuesday_time_1 = driver.find_element_by_xpath('//*[@id="page-main"]/div/div/div[6]/div/div/div[2]/div/div/div[1]/div/div[1]').text
    cur.execute('INSERT INTO apm_tb41 VALUES(?);', (tuesday_time_1,))
    base.commit()
except:
    print ("Значений не найдено, пропускаю")

try:
    tuesday_name_1 = driver.find_element_by_xpath('//*[@id="page-main"]/div/div/div[6]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/span[1]').text
    cur.execute('INSERT INTO apm_tb41 VALUES(?);', (tuesday_name_1,))
    base.commit()
except:
    print ("Значений не найдено, пропускаю")

try:
    tuesday_teacher_1 = driver.find_element_by_xpath('//*[@id="page-main"]/div/div/div[6]/div/div/div[2]/div/div/div[1]/div/div[2]/div/span[1]').text
    cur.execute('INSERT INTO apm_tb41 VALUES(?);', (tuesday_teacher_1,))
    base.commit()
except:
    print ("Значений не найдено, пропускаю")

try:
    tuesday_aud_1 = driver.find_element_by_xpath('//*[@id="page-main"]/div/div/div[6]/div/div/div[2]/div/div/div[1]/div/div[2]/div/span[2]').text
    cur.execute('INSERT INTO apm_tb41 VALUES(?);', (tuesday_aud_1,))
    base.commit()
except:
    print ("Значений не найдено, пропускаю")
##1 пара (конец)

##2 пара (начало)
try:
    tuesday_time_2 = driver.find_element_by_xpath('//*[@id="page-main"]/div/div/div[6]/div/div/div[2]/div/div/div[2]/div/div[1]').text
    cur.execute('INSERT INTO apm_tb41 VALUES(?);', (tuesday_time_2,))
    base.commit()
except:
    print("Значений не найдено, пропускаю")

try:
    tuesday_name_2 = driver.find_element_by_xpath('//*[@id="page-main"]/div/div/div[6]/div/div/div[2]/div/div/div[2]/div/div[2]/div/div[2]/span[1]').text
    cur.execute('INSERT INTO apm_tb41 VALUES(?);', (tuesday_name_2,))
    base.commit()
except:
    print("Значений не найдено, пропускаю")

try:
    tuesday_teacher_2 = driver.find_element_by_xpath('//*[@id="page-main"]/div/div/div[6]/div/div/div[2]/div/div/div[2]/div/div[2]/div/span[1]').text
    cur.execute('INSERT INTO apm_tb41 VALUES(?);', (tuesday_teacher_2,))
    base.commit()
except:
    print("Значений не найдено, пропускаю")

try:
    tuesday_aud_2 = driver.find_element_by_xpath('//*[@id="page-main"]/div/div/div[6]/div/div/div[2]/div/div/div[2]/div/div[2]/div/span[2]').text
    cur.execute('INSERT INTO apm_tb41 VALUES(?);', (tuesday_aud_2,))
    base.commit()
except:
    print("Значений не найдено, пропускаю")
##2 пара (конец)

##3 пара (начало)
try:
    tuesday_time_3 = driver.find_element_by_xpath('//*[@id="page-main"]/div/div/div[6]/div/div/div[2]/div/div/div[3]/div/div[1]').text
    cur.execute('INSERT INTO apm_tb41 VALUES(?);', (tuesday_time_3,))
    base.commit()
except:
    print("Значений не найдено, пропускаю")

try:
    tuesday_name_3 = driver.find_element_by_xpath('//*[@id="page-main"]/div/div/div[6]/div/div/div[2]/div/div/div[3]/div/div[2]/div/div[2]/span[1]').text
    cur.execute('INSERT INTO apm_tb41 VALUES(?);', (tuesday_name_3,))
    base.commit()
except:
    print("Значений не найдено, пропускаю")

try:
    tuesday_teacher_3 = driver.find_element_by_xpath('//*[@id="page-main"]/div/div/div[6]/div/div/div[2]/div/div/div[3]/div/div[2]/div/span[1]').text
    cur.execute('INSERT INTO apm_tb41 VALUES(?);', (tuesday_teacher_3,))
    base.commit()
except:
    print("Значений не найдено, пропускаю")

try:
    tuesday_aud_3 = driver.find_element_by_xpath('//*[@id="page-main"]/div/div/div[6]/div/div/div[2]/div/div/div[3]/div/div[2]/div/span[2]').text
    cur.execute('INSERT INTO apm_tb41 VALUES(?);', (tuesday_aud_3,))
    base.commit()
except:
    print("Значений не найдено, пропускаю")
##3 пара (конец)


##4 пара (начало)
try:
    tuesday_time_4 = driver.find_element_by_xpath('//*[@id="page-main"]/div/div/div[6]/div/div/div[2]/div/div/div[4]/div/div[1]').text
    cur.execute('INSERT INTO apm_tb41 VALUES(?);', (tuesday_time_4,))
    base.commit()
except:
    print("Значений не найдено, пропускаю")

try:
    tuesday_name_4 = driver.find_element_by_xpath('//*[@id="page-main"]/div/div/div[6]/div/div/div[2]/div/div/div[4]/div/div[2]/div/div[2]/span[1]').text
    cur.execute('INSERT INTO apm_tb41 VALUES(?);', (tuesday_name_4,))
    base.commit()
except:
    print("Значений не найдено, пропускаю")

try:
    tuesday_teacher_4 = driver.find_element_by_xpath('//*[@id="page-main"]/div/div/div[6]/div/div/div[2]/div/div/div[4]/div/div[2]/div/span[1]').text
    cur.execute('INSERT INTO apm_tb41 VALUES(?);', (tuesday_teacher_4,))
    base.commit()
except:
    print("Значений не найдено, пропускаю")

try:
    tuesday_aud_4 = driver.find_element_by_xpath('//*[@id="page-main"]/div/div/div[6]/div/div/div[2]/div/div/div[4]/div/div[2]/div/span[2]').text
    cur.execute('INSERT INTO apm_tb41 VALUES(?);', (tuesday_aud_4,))
    base.commit()
except:
    print("Значений не найдено, пропускаю")
##4 пара (конец)

##5 пара (начало)
try:
    tuesday_time_5 = driver.find_element_by_xpath('//*[@id="page-main"]/div/div/div[6]/div/div/div[2]/div/div/div[5]/div/div[1]').text
    cur.execute('INSERT INTO apm_tb41 VALUES(?);', (tuesday_time_5,))
    base.commit()
except:
    print("Значений не найдено, пропускаю")

try:
    tuesday_name_5 = driver.find_element_by_xpath('//*[@id="page-main"]/div/div/div[6]/div/div/div[2]/div/div/div[5]/div/div[2]/div/div[2]/span[1]').text
    cur.execute('INSERT INTO apm_tb41 VALUES(?);', (tuesday_name_5,))
    base.commit()
except:
    print("Значений не найдено, пропускаю")

try:
    tuesday_teacher_5 = driver.find_element_by_xpath('//*[@id="page-main"]/div/div/div[6]/div/div/div[2]/div/div/div[5]/div/div[2]/div/span[1]').text
    cur.execute('INSERT INTO apm_tb41 VALUES(?);', (tuesday_teacher_5,))
    base.commit()
except:
    print("Значений не найдено, пропускаю")

try:
    tuesday_aud_5 = driver.find_element_by_xpath('//*[@id="page-main"]/div/div/div[6]/div/div/div[2]/div/div/div[5]/div/div[2]/div/span[2]').text
    cur.execute('INSERT INTO apm_tb41 VALUES(?);', (tuesday_aud_5,))
    base.commit()
except:
    print("Значений не найдено, пропускаю")
##5 пара (конец)


##Среда
try:
    wednesday = driver.find_element_by_xpath('//*[@id="page-main"]/div/div/div[6]/div/div/div[3]/div/header/div/div[1]').text
    cur.execute('INSERT INTO apm_tb41 VALUES(?);', (wednesday,))
    base.commit()
except:
    print ("Значений не найдено, пропускаю")

##1 пара (начало)
try:
    wednesday_time_1 = driver.find_element_by_xpath('//*[@id="page-main"]/div/div/div[6]/div/div/div[3]/div/div/div[1]/div/div[1]').text
    cur.execute('INSERT INTO apm_tb41 VALUES(?);', (wednesday_time_1,))
    base.commit()
except:
    print ("Значений не найдено, пропускаю")

try:
    wednesday_name_1 = driver.find_element_by_xpath('//*[@id="page-main"]/div/div/div[6]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/span[1]').text
    cur.execute('INSERT INTO apm_tb41 VALUES(?);', (wednesday_name_1,))
    base.commit()
except:
    print ("Значений не найдено, пропускаю")

try:
    wednesday_teacher_1 = driver.find_element_by_xpath('//*[@id="page-main"]/div/div/div[6]/div/div/div[3]/div/div/div[1]/div/div[2]/div/span[1]').text
    cur.execute('INSERT INTO apm_tb41 VALUES(?);', (wednesday_teacher_1,))
    base.commit()
except:
    print ("Значений не найдено, пропускаю")

try:
    wednesday_aud_1 = driver.find_element_by_xpath('//*[@id="page-main"]/div/div/div[6]/div/div/div[3]/div/div/div[1]/div/div[2]/div/span[2]').text
    cur.execute('INSERT INTO apm_tb41 VALUES(?);', (wednesday_aud_1,))
    base.commit()
except:
    print ("Значений не найдено, пропускаю")
##1 пара (конец)

##2 пара (начало)
try:
    wednesday_time_2 = driver.find_element_by_xpath('//*[@id="page-main"]/div/div/div[6]/div/div/div[3]/div/div/div[2]/div/div[1]').text
    cur.execute('INSERT INTO apm_tb41 VALUES(?);', (wednesday_time_2,))
    base.commit()
except:
    print("Значений не найдено, пропускаю")

try:
    wednesday_name_2 = driver.find_element_by_xpath('//*[@id="page-main"]/div/div/div[6]/div/div/div[3]/div/div/div[2]/div/div[2]/div/div[2]/span[1]').text
    cur.execute('INSERT INTO apm_tb41 VALUES(?);', (wednesday_name_2,))
    base.commit()
except:
    print("Значений не найдено, пропускаю")

try:
    wednesday_teacher_2 = driver.find_element_by_xpath('//*[@id="page-main"]/div/div/div[6]/div/div/div[3]/div/div/div[2]/div/div[2]/div/span[1]').text
    cur.execute('INSERT INTO apm_tb41 VALUES(?);', (wednesday_teacher_2,))
    base.commit()
except:
    print("Значений не найдено, пропускаю")

try:
    wednesday_aud_2 = driver.find_element_by_xpath('//*[@id="page-main"]/div/div/div[6]/div/div/div[3]/div/div/div[2]/div/div[2]/div/span[2]').text
    cur.execute('INSERT INTO apm_tb41 VALUES(?);', (wednesday_aud_2,))
    base.commit()
except:
    print("Значений не найдено, пропускаю")
##2 пара (конец)

##3 пара (начало)
try:
    wednesday_time_3 = driver.find_element_by_xpath('//*[@id="page-main"]/div/div/div[6]/div/div/div[3]/div/div/div[3]/div/div[1]').text
    cur.execute('INSERT INTO apm_tb41 VALUES(?);', (wednesday_time_3,))
    base.commit()
except:
    print("Значений не найдено, пропускаю")

try:
    wednesday_name_3 = driver.find_element_by_xpath('//*[@id="page-main"]/div/div/div[6]/div/div/div[3]/div/div/div[3]/div/div[2]/div/div[2]/span[1]').text
    cur.execute('INSERT INTO apm_tb41 VALUES(?);', (wednesday_name_3,))
    base.commit()
except:
    print("Значений не найдено, пропускаю")

try:
    wednesday_teacher_3 = driver.find_element_by_xpath('//*[@id="page-main"]/div/div/div[6]/div/div/div[3]/div/div/div[3]/div/div[2]/div/span[1]').text
    cur.execute('INSERT INTO apm_tb41 VALUES(?);', (wednesday_teacher_3,))
    base.commit()
except:
    print("Значений не найдено, пропускаю")

try:
    wednesday_aud_3 = driver.find_element_by_xpath('//*[@id="page-main"]/div/div/div[6]/div/div/div[3]/div/div/div[3]/div/div[2]/div/span[2]').text
    cur.execute('INSERT INTO apm_tb41 VALUES(?);', (wednesday_aud_3,))
    base.commit()
except:
    print("Значений не найдено, пропускаю")
##3 пара (конец)


##4 пара (начало)
try:
    wednesday_time_4 = driver.find_element_by_xpath('//*[@id="page-main"]/div/div/div[6]/div/div/div[3]/div/div/div[4]/div/div[1]').text
    cur.execute('INSERT INTO apm_tb41 VALUES(?);', (wednesday_time_4,))
    base.commit()
except:
    print("Значений не найдено, пропускаю")

try:
    wednesday_name_4 = driver.find_element_by_xpath('//*[@id="page-main"]/div/div/div[6]/div/div/div[3]/div/div/div[4]/div/div[2]/div/div[2]/span[1]').text
    cur.execute('INSERT INTO apm_tb41 VALUES(?);', (wednesday_name_4,))
    base.commit()
except:
    print("Значений не найдено, пропускаю")

try:
    wednesday_teacher_4 = driver.find_element_by_xpath('//*[@id="page-main"]/div/div/div[6]/div/div/div[3]/div/div/div[4]/div/div[2]/div/span[1]').text
    cur.execute('INSERT INTO apm_tb41 VALUES(?);', (wednesday_teacher_4,))
    base.commit()
except:
    print("Значений не найдено, пропускаю")

try:
    wednesday_aud_4 = driver.find_element_by_xpath('//*[@id="page-main"]/div/div/div[6]/div/div/div[3]/div/div/div[4]/div/div[2]/div/span[2]').text
    cur.execute('INSERT INTO apm_tb41 VALUES(?);', (wednesday_aud_4,))
    base.commit()
except:
    print("Значений не найдено, пропускаю")
##4 пара (конец)

##5 пара (начало)
try:
    wednesday_time_5 = driver.find_element_by_xpath('//*[@id="page-main"]/div/div/div[6]/div/div/div[3]/div/div/div[5]/div/div[1]').text
    cur.execute('INSERT INTO apm_tb41 VALUES(?);', (wednesday_time_5,))
    base.commit()
except:
    print("Значений не найдено, пропускаю")

try:
    wednesday_name_5 = driver.find_element_by_xpath('//*[@id="page-main"]/div/div/div[6]/div/div/div[3]/div/div/div[5]/div/div[2]/div/div[2]/span[1]').text
    cur.execute('INSERT INTO apm_tb41 VALUES(?);', (wednesday_name_5,))
    base.commit()
except:
    print("Значений не найдено, пропускаю")

try:
    wednesday_teacher_5 = driver.find_element_by_xpath('//*[@id="page-main"]/div/div/div[6]/div/div/div[3]/div/div/div[5]/div/div[2]/div/span[1]').text
    cur.execute('INSERT INTO apm_tb41 VALUES(?);', (wednesday_teacher_5,))
    base.commit()
except:
    print("Значений не найдено, пропускаю")

try:
    wednesday_aud_5 = driver.find_element_by_xpath('//*[@id="page-main"]/div/div/div[6]/div/div/div[3]/div/div/div[5]/div/div[2]/div/span[2]').text
    cur.execute('INSERT INTO apm_tb41 VALUES(?);', (wednesday_aud_5,))
    base.commit()
except:
    print("Значений не найдено, пропускаю")
##5 пара (конец)


##Четверг
try:
    thursday = driver.find_element_by_xpath('//*[@id="page-main"]/div/div/div[6]/div/div/div[4]/div/header/div/div[1]').text
    cur.execute('INSERT INTO apm_tb41 VALUES(?);', (thursday,))
    base.commit()
except:
    print ("Значений не найдено, пропускаю")

##1 пара (начало)
try:
    thursday_time_1 = driver.find_element_by_xpath('//*[@id="page-main"]/div/div/div[6]/div/div/div[4]/div/div/div[1]/div/div[1]').text
    cur.execute('INSERT INTO apm_tb41 VALUES(?);', (thursday_time_1,))
    base.commit()
except:
    print ("Значений не найдено, пропускаю")

try:
    thursday_name_1 = driver.find_element_by_xpath('//*[@id="page-main"]/div/div/div[6]/div/div/div[4]/div/div/div[1]/div/div[2]/div/div/span[1]').text
    cur.execute('INSERT INTO apm_tb41 VALUES(?);', (thursday_name_1,))
    base.commit()
except:
    print ("Значений не найдено, пропускаю")

try:
    thursday_teacher_1 = driver.find_element_by_xpath('//*[@id="page-main"]/div/div/div[6]/div/div/div[4]/div/div/div[1]/div/div[2]/div/span[1]').text
    cur.execute('INSERT INTO apm_tb41 VALUES(?);', (thursday_teacher_1,))
    base.commit()
except:
    print ("Значений не найдено, пропускаю")

try:
    thursday_aud_1 = driver.find_element_by_xpath('//*[@id="page-main"]/div/div/div[6]/div/div/div[4]/div/div/div[1]/div/div[2]/div/span[2]').text
    cur.execute('INSERT INTO apm_tb41 VALUES(?);', (thursday_aud_1,))
    base.commit()
except:
    print ("Значений не найдено, пропускаю")
##1 пара (конец)

##2 пара (начало)
try:
    thursday_time_2 = driver.find_element_by_xpath('//*[@id="page-main"]/div/div/div[6]/div/div/div[4]/div/div/div[2]/div/div[1]').text
    cur.execute('INSERT INTO apm_tb41 VALUES(?);', (thursday_time_2,))
    base.commit()
except:
    print("Значений не найдено, пропускаю")

try:
    thursday_name_2 = driver.find_element_by_xpath('//*[@id="page-main"]/div/div/div[6]/div/div/div[4]/div/div/div[2]/div/div[2]/div/div[2]/span[1]').text
    cur.execute('INSERT INTO apm_tb41 VALUES(?);', (thursday_name_2,))
    base.commit()
except:
    print("Значений не найдено, пропускаю")

try:
    thursday_teacher_2 = driver.find_element_by_xpath('//*[@id="page-main"]/div/div/div[6]/div/div/div[4]/div/div/div[2]/div/div[2]/div/span[1]').text
    cur.execute('INSERT INTO apm_tb41 VALUES(?);', (thursday_teacher_2,))
    base.commit()
except:
    print("Значений не найдено, пропускаю")

try:
    thursday_aud_2 = driver.find_element_by_xpath('//*[@id="page-main"]/div/div/div[6]/div/div/div[4]/div/div/div[2]/div/div[2]/div/span[2]').text
    cur.execute('INSERT INTO apm_tb41 VALUES(?);', (thursday_aud_2,))
    base.commit()
except:
    print("Значений не найдено, пропускаю")
##2 пара (конец)

##3 пара (начало)
try:
    thursday_time_3 = driver.find_element_by_xpath('//*[@id="page-main"]/div/div/div[6]/div/div/div[4]/div/div/div[3]/div/div[1]').text
    cur.execute('INSERT INTO apm_tb41 VALUES(?);', (thursday_time_3,))
    base.commit()
except:
    print("Значений не найдено, пропускаю")

try:
    thursday_name_3 = driver.find_element_by_xpath('//*[@id="page-main"]/div/div/div[6]/div/div/div[4]/div/div/div[3]/div/div[2]/div/div[2]/span[1]').text
    cur.execute('INSERT INTO apm_tb41 VALUES(?);', (thursday_name_3,))
    base.commit()
except:
    print("Значений не найдено, пропускаю")

try:
    thursday_teacher_3 = driver.find_element_by_xpath('//*[@id="page-main"]/div/div/div[6]/div/div/div[4]/div/div/div[3]/div/div[2]/div/span[1]').text
    cur.execute('INSERT INTO apm_tb41 VALUES(?);', (thursday_teacher_3,))
    base.commit()
except:
    print("Значений не найдено, пропускаю")

try:
    thursday_aud_3 = driver.find_element_by_xpath('//*[@id="page-main"]/div/div/div[6]/div/div/div[4]/div/div/div[3]/div/div[2]/div/span[2]').text
    cur.execute('INSERT INTO apm_tb41 VALUES(?);', (thursday_aud_3,))
    base.commit()
except:
    print("Значений не найдено, пропускаю")
##3 пара (конец)


##4 пара (начало)
try:
    thursday_time_4 = driver.find_element_by_xpath('//*[@id="page-main"]/div/div/div[6]/div/div/div[4]/div/div/div[4]/div/div[1]').text
    cur.execute('INSERT INTO apm_tb41 VALUES(?);', (thursday_time_4,))
    base.commit()
except:
    print("Значений не найдено, пропускаю")

try:
    thursday_name_4 = driver.find_element_by_xpath('//*[@id="page-main"]/div/div/div[6]/div/div/div[4]/div/div/div[4]/div/div[2]/div/div[2]/span[1]').text
    cur.execute('INSERT INTO apm_tb41 VALUES(?);', (thursday_name_4,))
    base.commit()
except:
    print("Значений не найдено, пропускаю")

try:
    thursday_teacher_4 = driver.find_element_by_xpath('//*[@id="page-main"]/div/div/div[6]/div/div/div[4]/div/div/div[4]/div/div[2]/div/span[1]').text
    cur.execute('INSERT INTO apm_tb41 VALUES(?);', (thursday_teacher_4,))
    base.commit()
except:
    print("Значений не найдено, пропускаю")

try:
    thursday_aud_4 = driver.find_element_by_xpath('//*[@id="page-main"]/div/div/div[6]/div/div/div[4]/div/div/div[4]/div/div[2]/div/span[2]').text
    cur.execute('INSERT INTO apm_tb41 VALUES(?);', (thursday_aud_4,))
    base.commit()
except:
    print("Значений не найдено, пропускаю")
##4 пара (конец)

##5 пара (начало)
try:
    thursday_time_5 = driver.find_element_by_xpath('//*[@id="page-main"]/div/div/div[6]/div/div/div[4]/div/div/div[5]/div/div[1]').text
    cur.execute('INSERT INTO apm_tb41 VALUES(?);', (thursday_time_5,))
    base.commit()
except:
    print("Значений не найдено, пропускаю")

try:
    thursday_name_5 = driver.find_element_by_xpath('//*[@id="page-main"]/div/div/div[6]/div/div/div[4]/div/div/div[5]/div/div[2]/div/div[2]/span[1]').text
    cur.execute('INSERT INTO apm_tb41 VALUES(?);', (thursday_name_5,))
    base.commit()
except:
    print("Значений не найдено, пропускаю")

try:
    thursday_teacher_5 = driver.find_element_by_xpath('//*[@id="page-main"]/div/div/div[6]/div/div/div[4]/div/div/div[5]/div/div[2]/div/span[1]').text
    cur.execute('INSERT INTO apm_tb41 VALUES(?);', (thursday_teacher_5,))
    base.commit()
except:
    print("Значений не найдено, пропускаю")

try:
    thursday_aud_5 = driver.find_element_by_xpath('//*[@id="page-main"]/div/div/div[6]/div/div/div[4]/div/div/div[5]/div/div[2]/div/span[2]').text
    cur.execute('INSERT INTO apm_tb41 VALUES(?);', (thursday_aud_5,))
    base.commit()
except:
    print("Значений не найдено, пропускаю")
##5 пара (конец)


##Пятница
try:
    friday = driver.find_element_by_xpath('//*[@id="page-main"]/div/div/div[6]/div/div/div[4]/div/header/div/div[1]').text
    cur.execute('INSERT INTO apm_tb41 VALUES(?);', (friday,))
    base.commit()
except:
    print ("Значений не найдено, пропускаю")

##1 пара (начало)
try:
    friday_time_1 = driver.find_element_by_xpath('//*[@id="page-main"]/div/div/div[6]/div/div/div[4]/div/div/div[1]/div/div[1]').text
    cur.execute('INSERT INTO apm_tb41 VALUES(?);', (friday_time_1,))
    base.commit()
except:
    print ("Значений не найдено, пропускаю")

try:
    friday_name_1 = driver.find_element_by_xpath('//*[@id="page-main"]/div/div/div[6]/div/div/div[4]/div/div/div[1]/div/div[2]/div/div/span[1]').text
    cur.execute('INSERT INTO apm_tb41 VALUES(?);', (friday_name_1,))
    base.commit()
except:
    print ("Значений не найдено, пропускаю")

try:
    friday_teacher_1 = driver.find_element_by_xpath('//*[@id="page-main"]/div/div/div[6]/div/div/div[4]/div/div/div[1]/div/div[2]/div/span[1]').text
    cur.execute('INSERT INTO apm_tb41 VALUES(?);', (friday_teacher_1,))
    base.commit()
except:
    print ("Значений не найдено, пропускаю")

try:
    friday_aud_1 = driver.find_element_by_xpath('//*[@id="page-main"]/div/div/div[6]/div/div/div[4]/div/div/div[1]/div/div[2]/div/span[2]').text
    cur.execute('INSERT INTO apm_tb41 VALUES(?);', (friday_aud_1,))
    base.commit()
except:
    print ("Значений не найдено, пропускаю")
##1 пара (конец)

##2 пара (начало)
try:
    friday_time_2 = driver.find_element_by_xpath('//*[@id="page-main"]/div/div/div[6]/div/div/div[4]/div/div/div[2]/div/div[1]').text
    cur.execute('INSERT INTO apm_tb41 VALUES(?);', (friday_time_2,))
    base.commit()
except:
    print("Значений не найдено, пропускаю")

try:
    friday_name_2 = driver.find_element_by_xpath('//*[@id="page-main"]/div/div/div[6]/div/div/div[4]/div/div/div[2]/div/div[2]/div/div[2]/span[1]').text
    cur.execute('INSERT INTO apm_tb41 VALUES(?);', (friday_name_2,))
    base.commit()
except:
    print("Значений не найдено, пропускаю")

try:
    friday_teacher_2 = driver.find_element_by_xpath('//*[@id="page-main"]/div/div/div[6]/div/div/div[4]/div/div/div[2]/div/div[2]/div/span[1]').text
    cur.execute('INSERT INTO apm_tb41 VALUES(?);', (friday_teacher_2,))
    base.commit()
except:
    print("Значений не найдено, пропускаю")

try:
    friday_aud_2 = driver.find_element_by_xpath('//*[@id="page-main"]/div/div/div[6]/div/div/div[4]/div/div/div[2]/div/div[2]/div/span[2]').text
    cur.execute('INSERT INTO apm_tb41 VALUES(?);', (friday_aud_2,))
    base.commit()
except:
    print("Значений не найдено, пропускаю")
##2 пара (конец)

##3 пара (начало)
try:
    friday_time_3 = driver.find_element_by_xpath('//*[@id="page-main"]/div/div/div[6]/div/div/div[4]/div/div/div[3]/div/div[1]').text
    cur.execute('INSERT INTO apm_tb41 VALUES(?);', (friday_time_3,))
    base.commit()
except:
    print("Значений не найдено, пропускаю")

try:
    friday_name_3 = driver.find_element_by_xpath('//*[@id="page-main"]/div/div/div[6]/div/div/div[4]/div/div/div[3]/div/div[2]/div/div[2]/span[1]').text
    cur.execute('INSERT INTO apm_tb41 VALUES(?);', (friday_name_3,))
    base.commit()
except:
    print("Значений не найдено, пропускаю")

try:
    friday_teacher_3 = driver.find_element_by_xpath('//*[@id="page-main"]/div/div/div[6]/div/div/div[4]/div/div/div[3]/div/div[2]/div/span[1]').text
    cur.execute('INSERT INTO apm_tb41 VALUES(?);', (friday_teacher_3,))
    base.commit()
except:
    print("Значений не найдено, пропускаю")

try:
    friday_aud_3 = driver.find_element_by_xpath('//*[@id="page-main"]/div/div/div[6]/div/div/div[4]/div/div/div[3]/div/div[2]/div/span[2]').text
    cur.execute('INSERT INTO apm_tb41 VALUES(?);', (friday_aud_3,))
    base.commit()
except:
    print("Значений не найдено, пропускаю")
##3 пара (конец)


##4 пара (начало)
try:
    friday_time_4 = driver.find_element_by_xpath('//*[@id="page-main"]/div/div/div[6]/div/div/div[4]/div/div/div[4]/div/div[1]').text
    cur.execute('INSERT INTO apm_tb41 VALUES(?);', (friday_time_4,))
    base.commit()
except:
    print("Значений не найдено, пропускаю")

try:
    friday_name_4 = driver.find_element_by_xpath('//*[@id="page-main"]/div/div/div[6]/div/div/div[4]/div/div/div[4]/div/div[2]/div/div[2]/span[1]').text
    cur.execute('INSERT INTO apm_tb41 VALUES(?);', (friday_name_4,))
    base.commit()
except:
    print("Значений не найдено, пропускаю")

try:
    friday_teacher_4 = driver.find_element_by_xpath('//*[@id="page-main"]/div/div/div[6]/div/div/div[4]/div/div/div[4]/div/div[2]/div/span[1]').text
    cur.execute('INSERT INTO apm_tb41 VALUES(?);', (friday_teacher_4,))
    base.commit()
except:
    print("Значений не найдено, пропускаю")

try:
    friday_aud_4 = driver.find_element_by_xpath('//*[@id="page-main"]/div/div/div[6]/div/div/div[4]/div/div/div[4]/div/div[2]/div/span[2]').text
    cur.execute('INSERT INTO apm_tb41 VALUES(?);', (friday_aud_4,))
    base.commit()
except:
    print("Значений не найдено, пропускаю")
##4 пара (конец)

##5 пара (начало)
try:
    friday_time_5 = driver.find_element_by_xpath('//*[@id="page-main"]/div/div/div[6]/div/div/div[4]/div/div/div[5]/div/div[1]').text
    cur.execute('INSERT INTO apm_tb41 VALUES(?);', (friday_time_5,))
    base.commit()
except:
    print("Значений не найдено, пропускаю")

try:
    friday_name_5 = driver.find_element_by_xpath('//*[@id="page-main"]/div/div/div[6]/div/div/div[4]/div/div/div[5]/div/div[2]/div/div[2]/span[1]').text
    cur.execute('INSERT INTO apm_tb41 VALUES(?);', (friday_name_5,))
    base.commit()
except:
    print("Значений не найдено, пропускаю")

try:
    friday_teacher_5 = driver.find_element_by_xpath('//*[@id="page-main"]/div/div/div[6]/div/div/div[4]/div/div/div[5]/div/div[2]/div/span[1]').text
    cur.execute('INSERT INTO apm_tb41 VALUES(?);', (friday_teacher_5,))
    base.commit()
except:
    print("Значений не найдено, пропускаю")

try:
    friday_aud_5 = driver.find_element_by_xpath('//*[@id="page-main"]/div/div/div[6]/div/div/div[4]/div/div/div[5]/div/div[2]/div/span[2]').text
    cur.execute('INSERT INTO apm_tb41 VALUES(?);', (friday_aud_5,))
    base.commit()
except:
    print("Значений не найдено, пропускаю")
##5 пара (конец)


##Суббота
try:
    saturday = driver.find_element_by_xpath('//*[@id="page-main"]/div/div/div[7]/div/div/div/div/header/div/div[1]').text
    cur.execute('INSERT INTO apm_tb41 VALUES(?);', (saturday,))
    base.commit()
except:
    print ("Значений не найдено, пропускаю")

##1 пара (начало)
try:
    saturday_time_1 = driver.find_element_by_xpath('//*[@id="page-main"]/div/div/div[7]/div/div/div/div/div/div/div/div[1]').text
    cur.execute('INSERT INTO apm_tb41 VALUES(?);', (saturday_time_1,))
    base.commit()
except:
    print ("Значений не найдено, пропускаю")

try:
    saturday_name_1 = driver.find_element_by_xpath('//*[@id="page-main"]/div/div/div[7]/div/div/div/div/div/div/div/div[2]/div/div/span[1]').text
    cur.execute('INSERT INTO apm_tb41 VALUES(?);', (saturday_name_1,))
    base.commit()
except:
    print ("Значений не найдено, пропускаю")

try:
    saturday_teacher_1 = driver.find_element_by_xpath('//*[@id="page-main"]/div/div/div[7]/div/div/div/div/div/div/div/div[2]/div/span[1]').text
    cur.execute('INSERT INTO apm_tb41 VALUES(?);', (saturday_teacher_1,))
    base.commit()
except:
    print ("Значений не найдено, пропускаю")

try:
    saturday_aud_1 = driver.find_element_by_xpath('//*[@id="page-main"]/div/div/div[7]/div/div/div/div/div/div/div/div[2]/div/span[2]').text
    cur.execute('INSERT INTO apm_tb41 VALUES(?);', (saturday_aud_1,))
    base.commit()
except:
    print ("Значений не найдено, пропускаю")
##1 пара (конец)

##2 пара (начало)
try:
    saturday_time_2 = driver.find_element_by_xpath('//*[@id="page-main"]/div/div/div[7]/div/div/div/div/div/div[1]/div/div[1]').text
    cur.execute('INSERT INTO apm_tb41 VALUES(?);', (saturday_time_2,))
    base.commit()
except:
    print("Значений не найдено, пропускаю")

try:
    saturday_name_2 = driver.find_element_by_xpath('//*[@id="page-main"]/div/div/div[7]/div/div/div/div/div/div[1]/div/div[2]/div/div/span[1]').text
    cur.execute('INSERT INTO apm_tb41 VALUES(?);', (saturday_name_2,))
    base.commit()
except:
    print("Значений не найдено, пропускаю")

try:
    saturday_teacher_2 = driver.find_element_by_xpath('//*[@id="page-main"]/div/div/div[7]/div/div/div/div/div/div[1]/div/div[2]/div/span[1]').text
    cur.execute('INSERT INTO apm_tb41 VALUES(?);', (saturday_teacher_2,))
    base.commit()
except:
    print("Значений не найдено, пропускаю")

try:
    saturday_aud_2 = driver.find_element_by_xpath('//*[@id="page-main"]/div/div/div[7]/div/div/div/div/div/div[1]/div/div[2]/div/span[2]').text
    cur.execute('INSERT INTO apm_tb41 VALUES(?);', (saturday_aud_2,))
    base.commit()
except:
    print("Значений не найдено, пропускаю")
##2 пара (конец)

##3 пара (начало)
try:
    saturday_time_3 = driver.find_element_by_xpath('//*[@id="page-main"]/div/div/div[7]/div/div/div/div/div/div[2]/div/div[1]').text
    cur.execute('INSERT INTO apm_tb41 VALUES(?);', (saturday_time_3,))
    base.commit()
except:
    print("Значений не найдено, пропускаю")

try:
    saturday_name_3 = driver.find_element_by_xpath('//*[@id="page-main"]/div/div/div[7]/div/div/div/div/div/div[2]/div/div[2]/div/div[2]/span[1]').text
    cur.execute('INSERT INTO apm_tb41 VALUES(?);', (saturday_name_3,))
    base.commit()
except:
    print("Значений не найдено, пропускаю")

try:
    saturday_teacher_3 = driver.find_element_by_xpath('//*[@id="page-main"]/div/div/div[7]/div/div/div/div/div/div[2]/div/div[2]/div/span[1]').text
    cur.execute('INSERT INTO apm_tb41 VALUES(?);', (saturday_teacher_3,))
    base.commit()
except:
    print("Значений не найдено, пропускаю")

try:
    saturday_aud_3 = driver.find_element_by_xpath('//*[@id="page-main"]/div/div/div[7]/div/div/div/div/div/div[2]/div/div[2]/div/span[2]').text
    cur.execute('INSERT INTO apm_tb41 VALUES(?);', (saturday_aud_3,))
    base.commit()
except:
    print("Значений не найдено, пропускаю")
##3 пара (конец)


##4 пара (начало)
try:
    saturday_time_4 = driver.find_element_by_xpath('//*[@id="page-main"]/div/div/div[7]/div/div/div/div/div/div[3]/div/div[1]').text
    cur.execute('INSERT INTO apm_tb41 VALUES(?);', (saturday_time_4,))
    base.commit()
except:
    print("Значений не найдено, пропускаю")

try:
    saturday_name_4 = driver.find_element_by_xpath('//*[@id="page-main"]/div/div/div[7]/div/div/div/div/div/div[3]/div/div[2]/div/div[2]/span[1]').text
    cur.execute('INSERT INTO apm_tb41 VALUES(?);', (saturday_name_4,))
    base.commit()
except:
    print("Значений не найдено, пропускаю")

try:
    saturday_teacher_4 = driver.find_element_by_xpath('//*[@id="page-main"]/div/div/div[7]/div/div/div/div/div/div[3]/div/div[2]/div/span[1]').text
    cur.execute('INSERT INTO apm_tb41 VALUES(?);', (saturday_teacher_4,))
    base.commit()
except:
    print("Значений не найдено, пропускаю")

try:
    saturday_aud_4 = driver.find_element_by_xpath('//*[@id="page-main"]/div/div/div[7]/div/div/div/div/div/div[3]/div/div[2]/div/span[2]').text
    cur.execute('INSERT INTO apm_tb41 VALUES(?);', (saturday_aud_4,))
    base.commit()
except:
    print("Значений не найдено, пропускаю")
##4 пара (конец)

##5 пара (начало)
try:
    saturday_time_5 = driver.find_element_by_xpath('//*[@id="page-main"]/div/div/div[7]/div/div/div/div/div/div[4]/div/div[1]').text
    cur.execute('INSERT INTO apm_tb41 VALUES(?);', (saturday_time_5,))
    base.commit()
except:
    print("Значений не найдено, пропускаю")

try:
    saturday_name_5 = driver.find_element_by_xpath('//*[@id="page-main"]/div/div/div[7]/div/div/div/div/div/div[4]/div/div[2]/div/div[2]/span[1]').text
    cur.execute('INSERT INTO apm_tb41 VALUES(?);', (saturday_name_5,))
    base.commit()
except:
    print("Значений не найдено, пропускаю")

try:
    saturday_teacher_5 = driver.find_element_by_xpath('//*[@id="page-main"]/div/div/div[7]/div/div/div/div/div/div[4]/div/div[2]/div/span[1]').text
    cur.execute('INSERT INTO apm_tb41 VALUES(?);', (saturday_teacher_5,))
    base.commit()
except:
    print("Значений не найдено, пропускаю")

try:
    saturday_aud_5 = driver.find_element_by_xpath('//*[@id="page-main"]/div/div/div[7]/div/div/div/div/div/div[4]/div/div[2]/div/span[2]').text
    cur.execute('INSERT INTO apm_tb41 VALUES(?);', (saturday_aud_5,))
    base.commit()
except:
    print("Значений не найдено, пропускаю")
##5 пара (конец)



driver.quit()

print("Отправлено в базу")
cur.execute('UPDATE apm_tb41 SET name = REPLACE (name, "Понедельник", "📌 Понедельник 📌")')
cur.execute('UPDATE apm_tb41 SET name = REPLACE (name, "Вторник", "📌 Вторник 📌")')
cur.execute('UPDATE apm_tb41 SET name = REPLACE (name, "Среда", "📌 Среда 📌")')
cur.execute('UPDATE apm_tb41 SET name = REPLACE (name, "Четверг", "📌 Четверг 📌")')
cur.execute('UPDATE apm_tb41 SET name = REPLACE (name, "Пятница", "📌 Пятница 📌")')
cur.execute('UPDATE apm_tb41 SET name = REPLACE (name, "Суббота", "📌 Суббота 📌")')
cur.execute('UPDATE apm_tb41 SET name = REPLACE (name, "08:30", "🕗 08:30")')
cur.execute('UPDATE apm_tb41 SET name = REPLACE (name, "10:05", "🕙 10:05")')

cur.execute('UPDATE apm_tb41 SET name = REPLACE (name, "10:20", "🕙 10:20")')
cur.execute('UPDATE apm_tb41 SET name = REPLACE (name, "11:55", "🕛 11:55")')

cur.execute('UPDATE apm_tb41 SET name = REPLACE (name, "12:30", "🕛 12:30")')
cur.execute('UPDATE apm_tb41 SET name = REPLACE (name, "14:05", "🕑 14:05")')

cur.execute('UPDATE apm_tb41 SET name = REPLACE (name, "14:20", "🕑 14:20")')
cur.execute('UPDATE apm_tb41 SET name = REPLACE (name, "15:55", "🕓 15:55")')

cur.execute('UPDATE apm_tb41 SET name = REPLACE (name, "16:10", "🕔 16:10")')
cur.execute('UPDATE apm_tb41 SET name = REPLACE (name, "17:45", "🕡 17:45")')

#cur.execute('UPDATE apm_tb41 SET name = REPLACE (name, "Аудитория:", "🏢 Аудитория:")')
cur.execute('UPDATE apm_tb41 SET name = REPLACE (name, "пр.", "📝 пр.")')
cur.execute('UPDATE apm_tb41 SET name = REPLACE (name, "лек", "📖 лек")')
cur.execute('UPDATE apm_tb41 SET name = REPLACE (name, "лаб", "🔬 лаб")')

#Проверка на пустую строку в БД
noname = cur.execute('SELECT name FROM apm_tb41').fetchall()
print(noname)

if noname == ([]):
    print("База пуста")
    cur.execute('INSERT INTO apm_tb41 VALUES(?);', ('Занятий не найдено',))
else:
    print("База не пуста")
#Проверка на пустую строку в БД

base.commit()

