import pyodbc
import pandas as pd
import numpy as np

db_path = r'E:\code parking\database\moz.accdb'
conn_str = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=' + db_path
conn = pyodbc.connect(conn_str)
cursor = conn.cursor()
query = "SELECT * FROM MOTOR"
cursor.execute(query)
results = cursor.fetchall()
columns = [column[0] for column in cursor.description]
df = pd.DataFrame.from_records(results, columns=columns)

cursor.close()
conn.close()
df = np.array(df)
file_path = r'E:\code parking\database\rosobi.xlsx'
df_csv = np.array(pd.read_excel(file_path))

pelak_acc = df[:, 2]
pelak_csv = df_csv[:, 6]
pelak_brabar = 0
pelak_seen = set()
a = []
for number,i in enumerate(pelak_acc):
    for i2 in pelak_csv:
        if i2 == i and i not in pelak_seen:
            a.append(np.argwhere(pelak_acc==i)[0][0])
            pelak_brabar = pelak_brabar + 1
            pelak_seen.add(i)

print('pelak brabar = ', pelak_brabar)

motor_number_acc = df[:, 5]
motor_number_csv = df_csv[:, 3]
motor_brabar = 0
motor_seen = set()

for number,i in enumerate(motor_number_acc):
    for i2 in motor_number_csv:
        if i2 == i and i not in motor_seen:
            a.append(np.argwhere(motor_number_acc==i)[0][0])
            motor_brabar = motor_brabar + 1
            motor_seen.add(i)

print('motor_brabar = ', motor_brabar)

tane_number_acc = df[:, 4]
tane_number_csv = df_csv[:, 2]
tane_brabar = 0
tane_seen = set()

for number,i in enumerate(tane_number_acc):
    for i2 in tane_number_csv:

        if i2 == i and i not in tane_seen:
            a.append(np.argwhere(tane_number_acc == i)[0][0])
            tane_brabar = tane_brabar + 1
            tane_seen.add(i)

print('tane_brabar = ', tane_brabar)

