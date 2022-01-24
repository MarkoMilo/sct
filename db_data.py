import mysql.connector
from mysql.connector import errorcode
from mysql.connector import connection

# try:
#     mydb = mysql.connector.connect(
#       host="localhost",
#       user="root",
#       password="123456",
#       database="sql_store"
#     )
# except mysql.connector.Error as err:
#     if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
#         print("Something is wrong with your user name or password")
#     elif err.errno == errorcode.ER_BAD_DB_ERROR:
#         print("Database does not exist")
#     else:
#         print(err)
# else:
#   mydb.close()


def ret_db_data(table="shifts"):
    """
    The function returns data from the database
    :param table: table in database, default shifts
    :return: all data from specified table in format list of tuples(each tuple is row in db)
    """
    mydb = mysql.connector.MySQLConnection(user='smartcat', password='smartcat', port=9092,
                                     host='localhost',
                                     database='work_shifts')
    mycursor = mydb.cursor()
    querry = "SELECT * FROM {}".format(table)
    mycursor.execute(querry)
    myresult = mycursor.fetchall()
    mydb.close()
    return myresult