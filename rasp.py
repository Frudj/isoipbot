import sqlite3

#=========
#=====фТТ=
#=========

#=========
#======ЭПА==apa_tb11, apa_tb21, apa_tb31, apa_tb41
#=========

base = sqlite3.connect('rasp.db')
cur = base.cursor()
a_apa_tb11 = cur.execute('''SELECT * FROM apa_tb11''')
b_apa_tb11 = a_apa_tb11.fetchall()
apa_tb11_list = []
for x_apa_tb11 in b_apa_tb11:
    apa_tb11_list.append(' | '.join(x_apa_tb11))
apa_tb11_str = '\n'.join(apa_tb11_list)
base.close()

base = sqlite3.connect('rasp.db')
cur = base.cursor()
a_apa_tb21 = cur.execute('''SELECT * FROM apa_tb21''')
b_apa_tb21 = a_apa_tb21.fetchall()
apa_tb21_list = []
for x_apa_tb21 in b_apa_tb21:
    apa_tb21_list.append(' | '.join(x_apa_tb21))
apa_tb21_str = '\n'.join(apa_tb21_list)
base.close()

base = sqlite3.connect('rasp.db')
cur = base.cursor()
a_apa_tb31 = cur.execute('''SELECT * FROM apa_tb31''')
b_apa_tb31 = a_apa_tb31.fetchall()
apa_tb31_list = []
for x_apa_tb31 in b_apa_tb31:
    apa_tb31_list.append(' | '.join(x_apa_tb31))
apa_tb31_str = '\n'.join(apa_tb31_list)
base.close()

base = sqlite3.connect('rasp.db')
cur = base.cursor()
a_apa_tb41 = cur.execute('''SELECT * FROM apa_tb41''')
b_apa_tb41 = a_apa_tb41.fetchall()
apa_tb41_list = []
for x_apa_tb41 in b_apa_tb41:
    apa_tb41_list.append(' | '.join(x_apa_tb41))
apa_tb41_str = '\n'.join(apa_tb41_list)
base.close()

#=========
#======АПМ==apm_tb11, apm_tb21, apm_tb31, apm_tb41
#=========

base = sqlite3.connect('rasp.db')
cur = base.cursor()
a_apm_tb11 = cur.execute('''SELECT * FROM apm_tb11''')
b_apm_tb11 = a_apm_tb11.fetchall()
apm_tb11_list = []
for x_apm_tb11 in b_apm_tb11:
    apm_tb11_list.append(' | '.join(x_apm_tb11))
apm_tb11_str = '\n'.join(apm_tb11_list)
base.close()

base = sqlite3.connect('rasp.db')
cur = base.cursor()
a_apm_tb21 = cur.execute('''SELECT * FROM apm_tb21''')
b_apm_tb21 = a_apm_tb21.fetchall()
apm_tb21_list = []
for x_apm_tb21 in b_apm_tb21:
    apm_tb21_list.append(' | '.join(x_apm_tb21))
apm_tb21_str = '\n'.join(apm_tb21_list)
base.close()

base = sqlite3.connect('rasp.db')
cur = base.cursor()
a_apm_tb31 = cur.execute('''SELECT * FROM apm_tb31''')
b_apm_tb31 = a_apm_tb31.fetchall()
apm_tb31_list = []
for x_apm_tb31 in b_apm_tb31:
    apm_tb31_list.append(' | '.join(x_apm_tb31))
apm_tb31_str = '\n'.join(apm_tb31_list)
base.close()

base = sqlite3.connect('rasp.db')
cur = base.cursor()
a_apm_tb41 = cur.execute('''SELECT * FROM apm_tb41''')
b_apm_tb41 = a_apm_tb41.fetchall()
apm_tb41_list = []
for x_apm_tb41 in b_apm_tb41:
    apm_tb41_list.append(' | '.join(x_apm_tb41))
apm_tb41_str = '\n'.join(apm_tb41_list)
base.close()

#=========
#=====БЖТ===bjt_tb11, bjt_tb21, bjt_tb31, bjt_tb41
#=========

base = sqlite3.connect('rasp.db')
cur = base.cursor()
a_bjt_tb11 = cur.execute('''SELECT * FROM bjt_tb11''')
b_bjt_tb11 = a_bjt_tb11.fetchall()
bjt_tb11_list = []
for x_bjt_tb11 in b_bjt_tb11:
    bjt_tb11_list.append(' | '.join(x_bjt_tb11))
bjt_tb11_str = '\n'.join(bjt_tb11_list)
base.close()

base = sqlite3.connect('rasp.db')
cur = base.cursor()
a_bjt_tb21 = cur.execute('''SELECT * FROM bjt_tb21''')
b_bjt_tb21 = a_bjt_tb21.fetchall()
bjt_tb21_list = []
for x_bjt_tb21 in b_bjt_tb21:
    bjt_tb21_list.append(' | '.join(x_bjt_tb21))
bjt_tb21_str = '\n'.join(bjt_tb21_list)
base.close()

base = sqlite3.connect('rasp.db')
cur = base.cursor()
a_bjt_tb31 = cur.execute('''SELECT * FROM bjt_tb31''')
b_bjt_tb31 = a_bjt_tb31.fetchall()
bjt_tb31_list = []
for x_bjt_tb31 in b_bjt_tb31:
    bjt_tb31_list.append(' | '.join(x_bjt_tb31))
bjt_tb31_str = '\n'.join(bjt_tb31_list)
base.close()

base = sqlite3.connect('rasp.db')
cur = base.cursor()
a_bjt_tb41 = cur.execute('''SELECT * FROM bjt_tb41''')
b_bjt_tb41 = a_bjt_tb41.fetchall()
bjt_tb41_list = []
for x_bjt_tb41 in b_bjt_tb41:
    bjt_tb41_list.append(' | '.join(x_bjt_tb41))
bjt_tb41_str = '\n'.join(bjt_tb41_list)
base.close()

#=========
#=====ИКТС===ikts_tb11, ikts_tb21, ikts_tb31, ikts_tb41
#=========

base = sqlite3.connect('rasp.db')
cur = base.cursor()
a_ikts_tb11 = cur.execute('''SELECT * FROM ikts_tb11''')
b_ikts_tb11 = a_ikts_tb11.fetchall()
ikts_tb11_list = []
for x_ikts_tb11 in b_ikts_tb11:
    ikts_tb11_list.append(' | '.join(x_ikts_tb11))
ikts_tb11_str = '\n'.join(ikts_tb11_list)
base.close()

base = sqlite3.connect('rasp.db')
cur = base.cursor()
a_ikts_tb21 = cur.execute('''SELECT * FROM ikts_tb21''')
b_ikts_tb21 = a_ikts_tb21.fetchall()
ikts_tb21_list = []
for x_ikts_tb21 in b_ikts_tb21:
    ikts_tb21_list.append(' | '.join(x_ikts_tb21))
ikts_tb21_str = '\n'.join(ikts_tb21_list)
base.close()

base = sqlite3.connect('rasp.db')
cur = base.cursor()
a_ikts_tb31 = cur.execute('''SELECT * FROM ikts_tb31''')
b_ikts_tb31 = a_ikts_tb31.fetchall()
ikts_tb31_list = []
for x_ikts_tb31 in b_ikts_tb31:
    ikts_tb31_list.append(' | '.join(x_ikts_tb31))
ikts_tb31_str = '\n'.join(ikts_tb31_list)
base.close()

base = sqlite3.connect('rasp.db')
cur = base.cursor()
a_ikts_tb41 = cur.execute('''SELECT * FROM ikts_tb41''')
b_ikts_tb41 = a_ikts_tb41.fetchall()
ikts_tb41_list = []
for x_ikts_tb41 in b_ikts_tb41:
    ikts_tb41_list.append(' | '.join(x_ikts_tb41))
ikts_tb41_str = '\n'.join(ikts_tb41_list)
base.close()

#=========
#=====ИСТ===ist_tb11, ist_tb21, ist_tb31, ist_tb41
#=========

base = sqlite3.connect('rasp.db')
cur = base.cursor()
a_ist_tb11 = cur.execute('''SELECT * FROM ist_tb11''')
b_ist_tb11 = a_ist_tb11.fetchall()
ist_tb11_list = []
for x_ist_tb11 in b_ist_tb11:
    ist_tb11_list.append(' | '.join(x_ist_tb11))
ist_tb11_str = '\n'.join(ist_tb11_list)
base.close()

base = sqlite3.connect('rasp.db')
cur = base.cursor()
a_ist_tb21 = cur.execute('''SELECT * FROM ist_tb21''')
b_ist_tb21 = a_ist_tb21.fetchall()
ist_tb21_list = []
for x_ist_tb21 in b_ist_tb21:
    ist_tb21_list.append(' | '.join(x_ist_tb21))
ist_tb21_str = '\n'.join(ist_tb21_list)
base.close()

base = sqlite3.connect('rasp.db')
cur = base.cursor()
a_ist_tb31 = cur.execute('''SELECT * FROM ist_tb31''')
b_ist_tb31 = a_ist_tb31.fetchall()
ist_tb31_list = []
for x_ist_tb31 in b_ist_tb31:
    ist_tb31_list.append(' | '.join(x_ist_tb31))
ist_tb31_str = '\n'.join(ist_tb31_list)
base.close()

base = sqlite3.connect('rasp.db')
cur = base.cursor()
a_ist_tb41 = cur.execute('''SELECT * FROM ist_tb41''')
b_ist_tb41 = a_ist_tb41.fetchall()
ist_tb41_list = []
for x_ist_tb41 in b_ist_tb41:
    ist_tb41_list.append(' | '.join(x_ist_tb41))
ist_tb41_str = '\n'.join(ist_tb41_list)
base.close()

#=========
#=====ОБД===obd_tb11, obd_tb21, obd_tb31, obd_tb41
#=========

base = sqlite3.connect('rasp.db')
cur = base.cursor()
a_obd_tb11 = cur.execute('''SELECT * FROM obd_tb11''')
b_obd_tb11 = a_obd_tb11.fetchall()
obd_tb11_list = []
for x_obd_tb11 in b_obd_tb11:
    obd_tb11_list.append(' | '.join(x_obd_tb11))
obd_tb11_str = '\n'.join(obd_tb11_list)
base.close()

base = sqlite3.connect('rasp.db')
cur = base.cursor()
a_obd_tb21 = cur.execute('''SELECT * FROM obd_tb21''')
b_obd_tb21 = a_obd_tb21.fetchall()
obd_tb21_list = []
for x_obd_tb21 in b_obd_tb21:
    obd_tb21_list.append(' | '.join(x_obd_tb21))
obd_tb21_str = '\n'.join(obd_tb21_list)
base.close()

base = sqlite3.connect('rasp.db')
cur = base.cursor()
a_obd_tb31 = cur.execute('''SELECT * FROM obd_tb31''')
b_obd_tb31 = a_obd_tb31.fetchall()
obd_tb31_list = []
for x_obd_tb31 in b_obd_tb31:
    obd_tb31_list.append(' | '.join(x_obd_tb31))
obd_tb31_str = '\n'.join(obd_tb31_list)
base.close()

base = sqlite3.connect('rasp.db')
cur = base.cursor()
a_obd_tb41 = cur.execute('''SELECT * FROM obd_tb41''')
b_obd_tb41 = a_obd_tb41.fetchall()
obd_tb41_list = []
for x_obd_tb41 in b_obd_tb41:
    obd_tb41_list.append(' | '.join(x_obd_tb41))
obd_tb41_str = '\n'.join(obd_tb41_list)
base.close()

#=========
#=====ФЭСиП=
#=========

#=========
#======БУ-Эb==bu_ab11, bu_abb21, bu_ab31
#=========

base = sqlite3.connect('rasp.db')
cur = base.cursor()
a_bu_ab11 = cur.execute('''SELECT * FROM bu_ab11''')
b_bu_ab11 = a_bu_ab11.fetchall()
bu_ab11_list = []
for x_bu_ab11 in b_bu_ab11:
    bu_ab11_list.append(' | '.join(x_bu_ab11))
bu_ab11_str = '\n'.join(bu_ab11_list)
base.close()

base = sqlite3.connect('rasp.db')
cur = base.cursor()
a_bu_ab21 = cur.execute('''SELECT * FROM bu_ab21''')
b_bu_ab21 = a_bu_ab21.fetchall()
bu_ab21_list = []
for x_bu_ab21 in b_bu_ab21:
    bu_ab21_list.append(' | '.join(x_bu_ab21))
bu_ab21_str = '\n'.join(bu_ab21_list)
base.close()

base = sqlite3.connect('rasp.db')
cur = base.cursor()
a_bu_ab31 = cur.execute('''SELECT * FROM bu_ab31''')
b_bu_ab31 = a_bu_ab31.fetchall()
bu_ab31_list = []
for x_bu_ab31 in b_bu_ab31:
    bu_ab31_list.append(' | '.join(x_bu_ab31))
bu_ab31_str = '\n'.join(bu_ab31_list)
base.close()

#=========
#======ТУРУ-Эb==turu_ab11, turu_ab21, turu_ab31
#=========

base = sqlite3.connect('rasp.db')
cur = base.cursor()
a_turu_ab11 = cur.execute('''SELECT * FROM turu_ab11''')
b_turu_ab11 = a_turu_ab11.fetchall()
turu_ab11_list = []
for x_turu_ab11 in b_turu_ab11:
    turu_ab11_list.append(' | '.join(x_turu_ab11))
turu_ab11_str = '\n'.join(turu_ab11_list)
base.close()

base = sqlite3.connect('rasp.db')
cur = base.cursor()
a_turu_ab21 = cur.execute('''SELECT * FROM turu_ab21''')
b_turu_ab21 = a_turu_ab21.fetchall()
turu_ab21_list = []
for x_turu_ab21 in b_turu_ab21:
    turu_ab21_list.append(' | '.join(x_turu_ab21))
turu_ab21_str = '\n'.join(turu_ab21_list)
base.close()

base = sqlite3.connect('rasp.db')
cur = base.cursor()
a_turu_ab31 = cur.execute('''SELECT * FROM turu_ab31''')
b_turu_ab31 = a_turu_ab31.fetchall()
turu_ab31_list = []
for x_turu_ab31 in b_turu_ab31:
    turu_ab31_list.append(' | '.join(x_turu_ab31))
turu_ab31_str = '\n'.join(turu_ab31_list)
base.close()

#=========
#======УП-Эb==up_ab11, up_ab21, up_ab31, up_ab41
#=========

base = sqlite3.connect('rasp.db')
cur = base.cursor()
a_up_ab11 = cur.execute('''SELECT * FROM up_ab11''')
b_up_ab11 = a_up_ab11.fetchall()
up_ab11_list = []
for x_up_ab11 in b_up_ab11:
    up_ab11_list.append(' | '.join(x_up_ab11))
up_ab11_str = '\n'.join(up_ab11_list)
base.close()

base = sqlite3.connect('rasp.db')
cur = base.cursor()
a_up_ab21 = cur.execute('''SELECT * FROM up_ab21''')
b_up_ab21 = a_up_ab21.fetchall()
up_ab21_list = []
for x_up_ab21 in b_up_ab21:
    up_ab21_list.append(' | '.join(x_up_ab21))
up_ab21_str = '\n'.join(up_ab21_list)
base.close()

base = sqlite3.connect('rasp.db')
cur = base.cursor()
a_up_ab31 = cur.execute('''SELECT * FROM up_ab31''')
b_up_ab31 = a_up_ab31.fetchall()
up_ab31_list = []
for x_up_ab31 in b_up_ab31:
    up_ab31_list.append(' | '.join(x_up_ab31))
up_ab31_str = '\n'.join(up_ab31_list)
base.close()

base = sqlite3.connect('rasp.db')
cur = base.cursor()
a_up_ab41 = cur.execute('''SELECT * FROM up_ab41''')
b_up_ab41 = a_up_ab41.fetchall()
up_ab41_list = []
for x_up_ab41 in b_up_ab41:
    up_ab41_list.append(' | '.join(x_up_ab41))
up_ab41_str = '\n'.join(up_ab41_list)
base.close()

#=========
#======ЭУ-Эb==au_ab11, au_ab21, au_ab31, au_ab41
#=========

base = sqlite3.connect('rasp.db')
cur = base.cursor()
a_au_ab11 = cur.execute('''SELECT * FROM au_ab11''')
b_au_ab11 = a_au_ab11.fetchall()
au_ab11_list = []
for x_au_ab11 in b_au_ab11:
    au_ab11_list.append(' | '.join(x_au_ab11))
au_ab11_str = '\n'.join(au_ab11_list)
base.close()

base = sqlite3.connect('rasp.db')
cur = base.cursor()
a_au_ab21 = cur.execute('''SELECT * FROM au_ab21''')
b_au_ab21 = a_au_ab21.fetchall()
au_ab21_list = []
for x_au_ab21 in b_au_ab21:
    au_ab21_list.append(' | '.join(x_au_ab21))
au_ab21_str = '\n'.join(au_ab21_list)
base.close()

base = sqlite3.connect('rasp.db')
cur = base.cursor()
a_au_ab31 = cur.execute('''SELECT * FROM au_ab31''')
b_au_ab31 = a_au_ab31.fetchall()
au_ab31_list = []
for x_au_ab31 in b_au_ab31:
    au_ab31_list.append(' | '.join(x_au_ab31))
au_ab31_str = '\n'.join(au_ab31_list)
base.close()

base = sqlite3.connect('rasp.db')
cur = base.cursor()
a_au_ab41 = cur.execute('''SELECT * FROM au_ab41''')
b_au_ab41 = a_au_ab41.fetchall()
au_ab41_list = []
for x_au_ab41 in b_au_ab41:
    au_ab41_list.append(' | '.join(x_au_ab41))
au_ab41_str = '\n'.join(au_ab41_list)
base.close()

#=========
#=====ЮСТиП=
#=========

#=========
#======ГРП-Гb==grp_gb11, grp_gb21, grp_gb31, grp_gb41
#=========

base = sqlite3.connect('rasp.db')
cur = base.cursor()
a_grp_gb11 = cur.execute('''SELECT * FROM grp_gb11''')
b_grp_gb11 = a_grp_gb11.fetchall()
grp_gb11_list = []
for x_grp_gb11 in b_grp_gb11:
    grp_gb11_list.append(' | '.join(x_grp_gb11))
grp_gb11_str = '\n'.join(grp_gb11_list)
base.close()

base = sqlite3.connect('rasp.db')
cur = base.cursor()
a_grp_gb21 = cur.execute('''SELECT * FROM grp_gb21''')
b_grp_gb21 = a_grp_gb21.fetchall()
grp_gb21_list = []
for x_grp_gb21 in b_grp_gb21:
    grp_gb21_list.append(' | '.join(x_grp_gb21))
grp_gb21_str = '\n'.join(grp_gb21_list)
base.close()

base = sqlite3.connect('rasp.db')
cur = base.cursor()
a_grp_gb31 = cur.execute('''SELECT * FROM grp_gb31''')
b_grp_gb31 = a_grp_gb31.fetchall()
grp_gb31_list = []
for x_grp_gb31 in b_grp_gb31:
    grp_gb31_list.append(' | '.join(x_grp_gb31))
grp_gb31_str = '\n'.join(grp_gb31_list)
base.close()

base = sqlite3.connect('rasp.db')
cur = base.cursor()
a_grp_gb41 = cur.execute('''SELECT * FROM grp_gb41''')
b_grp_gb41 = a_grp_gb41.fetchall()
grp_gb41_list = []
for x_grp_gb41 in b_grp_gb41:
    grp_gb41_list.append(' | '.join(x_grp_gb41))
grp_gb41_str = '\n'.join(grp_gb41_list)
base.close()

#=========
#======ГРП-Гbv==grp_gbv11, grp_gbv21, grp_gbv31, grp_gbv41
#=========

base = sqlite3.connect('rasp.db')
cur = base.cursor()
a_grp_gbv11 = cur.execute('''SELECT * FROM grp_gbv11''')
b_grp_gbv11 = a_grp_gbv11.fetchall()
grp_gbv11_list = []
for x_grp_gbv11 in b_grp_gbv11:
    grp_gbv11_list.append(' | '.join(x_grp_gbv11))
grp_gbv11_str = '\n'.join(grp_gbv11_list)
base.close()

base = sqlite3.connect('rasp.db')
cur = base.cursor()
a_grp_gbv21 = cur.execute('''SELECT * FROM grp_gbv21''')
b_grp_gbv21 = a_grp_gbv21.fetchall()
grp_gbv21_list = []
for x_grp_gbv21 in b_grp_gbv21:
    grp_gbv21_list.append(' | '.join(x_grp_gbv21))
grp_gbv21_str = '\n'.join(grp_gbv21_list)
base.close()

base = sqlite3.connect('rasp.db')
cur = base.cursor()
a_grp_gbv31 = cur.execute('''SELECT * FROM grp_gbv31''')
b_grp_gbv31 = a_grp_gbv31.fetchall()
grp_gbv31_list = []
for x_grp_gbv31 in b_grp_gbv31:
    grp_gbv31_list.append(' | '.join(x_grp_gbv31))
grp_gbv31_str = '\n'.join(grp_gbv31_list)
base.close()

base = sqlite3.connect('rasp.db')
cur = base.cursor()
a_grp_gbv41 = cur.execute('''SELECT * FROM grp_gbv41''')
b_grp_gbv41 = a_grp_gbv41.fetchall()
grp_gbv41_list = []
for x_grp_gbv41 in b_grp_gbv41:
    grp_gbv41_list.append(' | '.join(x_grp_gbv41))
grp_gbv41_str = '\n'.join(grp_gbv41_list)
base.close()

#=========
#======ГРП-Гbvs==grp_gbvs11, grp_gbvs21, grp_gbvs31, grp_gbvs41
#=========

base = sqlite3.connect('rasp.db')
cur = base.cursor()
a_grp_gbvs11 = cur.execute('''SELECT * FROM grp_gbvs11''')
b_grp_gbvs11 = a_grp_gbvs11.fetchall()
grp_gbvs11_list = []
for x_grp_gbvs11 in b_grp_gbvs11:
    grp_gbvs11_list.append(' | '.join(x_grp_gbvs11))
grp_gbvs11_str = '\n'.join(grp_gbvs11_list)
base.close()

base = sqlite3.connect('rasp.db')
cur = base.cursor()
a_grp_gbvs21 = cur.execute('''SELECT * FROM grp_gbvs21''')
b_grp_gbvs21 = a_grp_gbvs21.fetchall()
grp_gbvs21_list = []
for x_grp_gbvs21 in b_grp_gbvs21:
    grp_gbvs21_list.append(' | '.join(x_grp_gbvs21))
grp_gbvs21_str = '\n'.join(grp_gbvs21_list)
base.close()

base = sqlite3.connect('rasp.db')
cur = base.cursor()
a_grp_gbvs31 = cur.execute('''SELECT * FROM grp_gbvs31''')
b_grp_gbvs31 = a_grp_gbvs31.fetchall()
grp_gbvs31_list = []
for x_grp_gbvs31 in b_grp_gbvs31:
    grp_gbvs31_list.append(' | '.join(x_grp_gbvs31))
grp_gbvs31_str = '\n'.join(grp_gbvs31_list)
base.close()

base = sqlite3.connect('rasp.db')
cur = base.cursor()
a_grp_gbvs41 = cur.execute('''SELECT * FROM grp_gbvs41''')
b_grp_gbvs41 = a_grp_gbvs41.fetchall()
grp_gbvs41_list = []
for x_grp_gbvs41 in b_grp_gbvs41:
    grp_gbvs41_list.append(' | '.join(x_grp_gbvs41))
grp_gbvs41_str = '\n'.join(grp_gbvs41_list)
base.close()

#=========
#======УГП-Гb==ugp_gb11, ugp_gb21, ugp_gb31, ugp_gb41
#=========

base = sqlite3.connect('rasp.db')
cur = base.cursor()
a_ugp_gb11 = cur.execute('''SELECT * FROM ugp_gb11''')
b_ugp_gb11 = a_ugp_gb11.fetchall()
ugp_gb11_list = []
for x_ugp_gb11 in b_ugp_gb11:
    ugp_gb11_list.append(' | '.join(x_ugp_gb11))
ugp_gb11_str = '\n'.join(ugp_gb11_list)
base.close()

base = sqlite3.connect('rasp.db')
cur = base.cursor()
a_ugp_gb21 = cur.execute('''SELECT * FROM ugp_gb21''')
b_ugp_gb21 = a_ugp_gb21.fetchall()
ugp_gb21_list = []
for x_ugp_gb21 in b_ugp_gb21:
    ugp_gb21_list.append(' | '.join(x_ugp_gb21))
ugp_gb21_str = '\n'.join(ugp_gb21_list)
base.close()

base = sqlite3.connect('rasp.db')
cur = base.cursor()
a_ugp_gb31 = cur.execute('''SELECT * FROM ugp_gb31''')
b_ugp_gb31 = a_ugp_gb31.fetchall()
ugp_gb31_list = []
for x_ugp_gb31 in b_ugp_gb31:
    ugp_gb31_list.append(' | '.join(x_ugp_gb31))
ugp_gb31_str = '\n'.join(ugp_gb31_list)
base.close()

base = sqlite3.connect('rasp.db')
cur = base.cursor()
a_ugp_gb41 = cur.execute('''SELECT * FROM ugp_gb41''')
b_ugp_gb41 = a_ugp_gb41.fetchall()
ugp_gb41_list = []
for x_ugp_gb41 in b_ugp_gb41:
    ugp_gb41_list.append(' | '.join(x_ugp_gb41))
ugp_gb41_str = '\n'.join(ugp_gb41_list)
base.close()
