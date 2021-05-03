import sqlite3

#фТТ
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