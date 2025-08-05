import sqlite3
def connect_db():
    conn=sqlite3.connect("D:\\DB_2_\\luutru\\CNPM.db")
    return conn