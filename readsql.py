import os 

import pandas as pd 
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

load_dotenv()
host = os.getenv('HOST')
username = os.getenv('USER')
password = os.getenv('PASSWORD')

connection = mysql.connector.connect(host='localhost',
                                      user='root',
                                      password='1723',
                                      database='swiftmarket')

cursor = connection.cursor()

def queryToDataFrame (query):

    cursor.execute(query)
    rows = cursor.fetchall()
    df = pd.DataFrame(data=rows,columns=cursor.column_names)
    return df

def showTables():
    query = """SHOW TABLES;"""
    cursor.execute(query)
    rows = cursor.fetchall()
    df = dfDataFrame(data=rows,columns=cursor.column_names)
    return df 

def DescribeTable(table_name):
    query = f"""Describe{tablename};"""
    cursor.execute(query)
    rows = cursor.fetchall()
    df = pd.DataFrame(data=rows,columns=cursor.column_names)
    return df 

def add(x,y):
    return x+y




























