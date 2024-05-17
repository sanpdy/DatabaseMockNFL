import sys
import re
import mysql.connector
from tabulate import tabulate


def open_database(hostname, user_name, mysql_pw, database_name):
    global conn
    conn = mysql.connector.connect(host=hostname, user=user_name, password=mysql_pw, database=database_name)
    global cursor
    cursor = conn.cursor()


def print_format(result):
    header = []
    for cd in cursor.description:
        header.append(cd[0])
    return(tabulate(result, headers=header))

def execute_select(query):
    cursor.execute(query)
    result = print_format(cursor.fetchall())
    return result

def insert(table, values):
    query = "INSERT INTO " + table + " values (" + values + ")" + ';'
    cursor.execute(query)
    conn.commit()


def execute_update(query):
    cursor.execute(query)
    conn.commit()


def sanatize_input(text):
    # return a string with no special characters (Not true sanitation)
    return re.sub(r'[^a-zA-Z0-9\s]', '', text)


def close_db() :
    cursor.close()
    conn.close()