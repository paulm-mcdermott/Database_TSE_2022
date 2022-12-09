import mysql.connector

my_connection = mysql.connector.connect(
  host="localhost",
  user="pmcderm27",
)
print(my_connection)

my_cursor = my_connection.cursor()

my_cursor.execute("SHOW DATABASES")

for x in my_cursor:
  print(x)