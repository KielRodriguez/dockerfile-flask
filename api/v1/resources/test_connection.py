from flask_restful import Resource
from flask_mysqldb import MySQL

mysql = MySQL()

class TestConnection(Resource):
    def get(self):
        cur = mysql.connection.cursor()
        cur.execute('''SELECT NOW() AS date;''')
        rv = cur.fetchall()
        date= str(rv[0][0])
        cur.close()
        return {"date": str(date)}