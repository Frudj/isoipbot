import os
from time import sleep
from subprocess import call

print("Удаляем предыдущую базу с раписанием")
path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'rasp.db')
os.remove(path)
print("База удалена")
sleep(2)

print("Факультет ФТТ")
sleep(2)

print("ЭПА-Тb")
sleep(2)

print("Начало сбора данных - ЭПА-Тb11")
sleep(2)
call(["python", "apa_tb11.py"])
print("Конец сбора данных - ЭПА-Тb11")

print("Начало сбора данных - ЭПА-Тb21")
sleep(2)
call(["python", "apa_tb21.py"])
print("Конец сбора данных - ЭПА-Тb21")

print("Начало сбора данных - ЭПА-Тb31")
sleep(2)
call(["python", "apa_tb31.py"])
print("Конец сбора данных - ЭПА-Тb31")

print("Начало сбора данных - ЭПА-Тb41")
sleep(2)
call(["python", "apa_tb41.py"])
print("Конец сбора данных - ЭПА-Тb41")

print("АПМ-Тb")
sleep(2)

print("Начало сбора данных - АПМ-Тb11")
sleep(2)
call(["python", "apm_tb11.py"])
print("Конец сбора данных - АПМ-Тb11")

print("Начало сбора данных - АПМ-Тb21")
sleep(2)
call(["python", "apm_tb21.py"])
print("Конец сбора данных - АПМ-Тb21")

print("Начало сбора данных - АПМ-Тb31")
sleep(2)
call(["python", "apm_tb31.py"])
print("Конец сбора данных - АПМ-Тb31")

print("Начало сбора данных - АПМ-Тb41")
sleep(2)
call(["python", "apm_tb41.py"])
print("Конец сбора данных - АПМ-Тb41")

print("БЖТ-Tb")
sleep(2)

print("Начало сбора данных - БЖТ-Tb11")
sleep(2)
call(["python", "bjt_tb11.py"])
print("Конец сбора данных - БЖТ-Tb11")

print("Начало сбора данных - БЖТ-Tb21")
sleep(2)
call(["python", "bjt_tb21.py"])
print("Конец сбора данных - БЖТ-Tb21")

print("Начало сбора данных - БЖТ-Tb31")
sleep(2)
call(["python", "bjt_tb31.py"])
print("Конец сбора данных - БЖТ-Tb31")

print("Начало сбора данных - БЖТ-Tb41")
sleep(2)
call(["python", "bjt_tb41.py"])
print("Конец сбора данных - БЖТ-Tb41")

print("ИКТС-Tb")
sleep(2)

print("Начало сбора данных - ИКТС-Tb11")
sleep(2)
call(["python", "ikts_tb11.py"])
print("Конец сбора данных - ИКТС-Tb11")

print("Начало сбора данных - ИКТС-Tb21")
sleep(2)
call(["python", "ikts_tb21.py"])
print("Конец сбора данных - ИКТС-Tb21")

print("Начало сбора данных - ИКТС-Tb31")
sleep(2)
call(["python", "ikts_tb31.py"])
print("Конец сбора данных - ИКТС-Tb31")

print("Начало сбора данных - ИКТС-Tb41")
sleep(2)
call(["python", "ikts_tb41.py"])
print("Конец сбора данных - ИКТС-Tb41")

print("ИСТ-Tb")
sleep(2)

print("Начало сбора данных - ИСТ-Tb11")
sleep(2)
call(["python", "ist_tb11.py"])
print("Конец сбора данных - ИСТ-Tb11")

print("Начало сбора данных - ИСТ-Tb21")
sleep(2)
call(["python", "ist_tb21.py"])
print("Конец сбора данных - ИСТ-Tb21")

print("Начало сбора данных - ИСТ-Tb31")
sleep(2)
call(["python", "ist_tb31.py"])
print("Конец сбора данных - ИСТ-Tb31")

print("Начало сбора данных - ИСТ-Tb41")
sleep(2)
call(["python", "ist_tb41.py"])
print("Конец сбора данных - ИСТ-Tb41")

print("ОБД-Тb")
sleep(2)

print("Начало сбора данных - ОБД-Тb11")
sleep(2)
call(["python", "obd_tb11.py"])
print("Конец сбора данных - ОБД-Тb11")

print("Начало сбора данных - ОБД-Тb21")
sleep(2)
call(["python", "obd_tb21.py"])
print("Конец сбора данных - ОБД-Тb21")

print("Начало сбора данных - ОБД-Тb31")
sleep(2)
call(["python", "obd_tb31.py"])
print("Конец сбора данных - ОБД-Тb31")

print("Начало сбора данных - ОБД-Тb41")
sleep(2)
call(["python", "obd_tb41.py"])
print("Конец сбора данных - ОБД-Тb41")


print("Факультет ФЭСиП")
sleep(2)

print("БУ-Эb")
sleep(2)

print("Начало сбора данных - БУ-Эb11")
sleep(2)
call(["python", "bu_ab11.py"])
print("Конец сбора данных - БУ-Эb11")

print("Начало сбора данных - БУ-Эb21")
sleep(2)
call(["python", "bu_ab21.py"])
print("Конец сбора данных - БУ-Эb21")

print("Начало сбора данных - БУ-Эb31")
sleep(2)
call(["python", "bu_ab31.py"])
print("Конец сбора данных - БУ-Эb31")

print("ТУРУ-Эb")
sleep(2)

print("Начало сбора данных - ТУРУ-Эb11")
sleep(2)
call(["python", "turu_ab11.py"])
print("Конец сбора данных - ТУРУ-Эb11")

print("Начало сбора данных - ТУРУ-Эb21")
sleep(2)
call(["python", "turu_ab21.py"])
print("Конец сбора данных - ТУРУ-Эb21")

print("Начало сбора данных - ТУРУ-Эb31")
sleep(2)
call(["python", "turu_ab31.py"])
print("Конец сбора данных - ТУРУ-Эb31")

print("УП-Эb")
sleep(2)

print("Начало сбора данных - УП-Эb11")
sleep(2)
call(["python", "up_ab11.py"])
print("Конец сбора данных - УП-Эb11")

print("Начало сбора данных - УП-Эb21")
sleep(2)
call(["python", "up_ab21.py"])
print("Конец сбора данных - УП-Эb21")

print("Начало сбора данных - УП-Эb31")
sleep(2)
call(["python", "up_ab31.py"])
print("Конец сбора данных - УП-Эb31")

print("Начало сбора данных - УП-Эb41")
sleep(2)
call(["python", "up_ab41.py"])
print("Конец сбора данных - УП-Эb41")

print("ЭУ-Эb")
sleep(2)

print("Начало сбора данных - ЭУ-Эb11")
sleep(2)
call(["python", "au_ab11.py"])
print("Конец сбора данных - ЭУ-Эb11")

print("Начало сбора данных - ЭУ-Эb21")
sleep(2)
call(["python", "au_ab21.py"])
print("Конец сбора данных - ЭУ-Эb21")

print("Начало сбора данных - ЭУ-Эb31")
sleep(2)
call(["python", "au_ab31.py"])
print("Конец сбора данных - ЭУ-Эb31")

print("Начало сбора данных - ЭУ-Эb41")
sleep(2)
call(["python", "au_ab41.py"])
print("Конец сбора данных - ЭУ-Эb41")


print("Факультет ЮСТиП")
sleep(2)

print("ГРП-Гb")
sleep(2)

print("Начало сбора данных - ГРП-Гb11")
sleep(2)
call(["python", "grp_gb11.py"])
print("Конец сбора данных - ГРП-Гb11")

print("Начало сбора данных - ГРП-Гb21")
sleep(2)
call(["python", "grp_gb21.py"])
print("Конец сбора данных - ГРП-Гb21")

print("Начало сбора данных - ГРП-Гb31")
sleep(2)
call(["python", "grp_gb31.py"])
print("Конец сбора данных - ГРП-Гb31")

print("Начало сбора данных - ГРП-Гb41")
sleep(2)
call(["python", "grp_gb41.py"])
print("Конец сбора данных - ГРП-Гb41")

print("ГРП-Гbv")
sleep(2)

print("Начало сбора данных - ГРП-Гbv11")
sleep(2)
call(["python", "grp_gbv11.py"])
print("Конец сбора данных - ГРП-Гbv11")

print("Начало сбора данных - ГРП-Гbv21")
sleep(2)
call(["python", "grp_gbv21.py"])
print("Конец сбора данных - ГРП-Гbv21")

print("Начало сбора данных - ГРП-Гbv31")
sleep(2)
call(["python", "grp_gbv31.py"])
print("Конец сбора данных - ГРП-Гbv31")

print("Начало сбора данных - ГРП-Гbv41")
sleep(2)
call(["python", "grp_gbv41.py"])
print("Конец сбора данных - ГРП-Гbv41")

print("ГРП-Гbvs")
sleep(2)

print("Начало сбора данных - ГРП-Гbvs11")
sleep(2)
call(["python", "grp_gbvs11.py"])
print("Конец сбора данных - ГРП-Гbvs11")

print("Начало сбора данных - ГРП-Гbvs21")
sleep(2)
call(["python", "grp_gbvs21.py"])
print("Конец сбора данных - ГРП-Гbvs21")

print("Начало сбора данных - ГРП-Гbvs31")
sleep(2)
call(["python", "grp_gbvs31.py"])
print("Конец сбора данных - ГРП-Гbvs31")

print("Начало сбора данных - ГРП-Гbvs41")
sleep(2)
call(["python", "grp_gbvs41.py"])
print("Конец сбора данных - ГРП-Гbvs41")

print("УГП-Гb")
sleep(2)

print("Начало сбора данных - УГП-Гb11")
sleep(2)
call(["python", "ugp_gb11.py"])
print("Конец сбора данных - УГП-Гb11")

print("Начало сбора данных - УГП-Гb21")
sleep(2)
call(["python", "ugp_gb21.py"])
print("Конец сбора данных - УГП-Гb21")

print("Начало сбора данных - УГП-Гb31")
sleep(2)
call(["python", "ugp_gb31.py"])
print("Конец сбора данных - УГП-Гb31")

print("Начало сбора данных - УГП-Гb41")
sleep(2)
call(["python", "ugp_gb41.py"])
print("Конец сбора данных - УГП-Гb41")

print("")
print("========================================")
print("Успешное заверешение сбора данных групп")
print("========================================")