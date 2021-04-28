import os
from time import sleep
from subprocess import call

print("Удаляем предыдущую базу с раписанием")
path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'rasp.db')
os.remove(path)
print("База удалена")
sleep(2)


print("Начало сбора данных - ИСТ-Тb11")
sleep(2)
call(["python", "ist_tb11.py"])
print("Конец сбора данных - ИСТ-Тb11")
#sleep(14)

print("Начало сбора данных - АПМ-Тb11")
sleep(2)
call(["python", "apm_tb11.py"])
print("Конец сбора данных - АПМ-Тb11")

print("")
print("========================================")
print("Успешное заверешение сбора данных групп")
print("========================================")