import csv
import sqlite3
import os.path

db_file = '../app/site.db'

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, db_file)

# insert into sqlite database

con = sqlite3.connect(db_path)
cur = con.cursor()

with open('countries_list.csv', 'r') as fin:  # `with` statement available in 2.5+
    # csv.DictReader uses first line in file for column headings by default
    dr = csv.DictReader(fin)  # comma is default delimiter
    next(dr)
    # Nested lists, tuples are used for executemany, not for execute.
    to_db = [(i['Country Code'], i['Latitude'], i['Longitude']
              , i['Country Name']) for i in dr]

create_table_sql = """CREATE TABLE IF NOT EXISTS country (
id INTEGER PRIMARY KEY NOT NULL ,
country_code varchar(4),
latitude Float,
longitude Float,
country_name varchar(100)
);
"""
cur.execute(create_table_sql)
cur.execute("DELETE FROM main.country;")
cur.executemany("INSERT INTO main.country (country_code, latitude,	longitude"
                ", country_name) VALUES (?, ?, ?, ?);", to_db)


con.commit()
con.close()
