import mysql.connector

mydb = mysql.connector.connect(
    host="localhost", user="root", password="", database="expense-tracker"
)
my_cursor = mydb.cursor()
