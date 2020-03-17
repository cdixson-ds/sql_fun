import pandas as pd
import sqlite3

df = pd.read_csv('buddymove_holidayiq.csv')

conn = sqlite3.connect("buddymove_holidayiq.sqlite3")

cursor = conn.cursor()

df.to_sql("buddymove_holidayiq.sqlite3", conn)

query = "SELECT * FROM 'buddymove_holidayiq.sqlite3'"
cursor.execute(query).fetchall()

print('Table size:_', df.shape)

query2 = '''
SELECT COUNT (*) FROM 'buddymove_holidayiq.sqlite3' WHERE "Nature" >= 100 AND "Shopping" >= 100
'''

print(f"How many reviewed at least 100 in Nature and Shopping? : {cursor.execute(query2).fetchall()[0][0]} users")



