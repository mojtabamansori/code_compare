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
print(df[:,2])
