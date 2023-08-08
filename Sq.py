import sqlite3
from sqlite3 import Error
import datetime
# ================================================================== Database controller ===================================================== #
'''
    VAL = SQL(value)                 
    VAL.sql_connection()     "" To connect to the Databse file ""
    next(VAL.__iter__())     "" To check if the input username exists
                                in the Database "" ... <<The result will
                                save in COND variable>>
    VAL.Exec_values()        "" Execute new values in the Database ""
    VAL.pass_check()         "" To check if the input password is matched
                                with the one into the Database "" ... <<The
                                result will save in PASS_RESULT variable>>
    VAL.acc_env_call()
                                                                
    << VAL.COND = 1 >>--> The username value is already exists in Database.
    << VAL.COND = 0 >>--> The username value is not in the Database.
    << VAL.COND = 2 >>--> An iterate function doesn't work.
    << VAL.PASS_RESULT >> --> The value of password from inside the Database attached to the input username.
    << VAL.CALL_RESULT >> -->
'''
# ============================================================================================================================================ #


class SQL():
    def __init__(self, value, column = None, valueII = None, update = False, encode = None):

        self.column = column
        self.valueII = valueII
        self.value = value
        self.inside_values = []        
        try:
           self.con = sqlite3.connect('databaseONE.db')
        except Error:
           print('Error with connecting to the Database..')
        self.cur = self.con.cursor()
        self.rows = []
        self.COND = 2
        self.PASS_RESULT = None
        self.CALL_RESULT = None
        self.encode = encode
        self.update = update


    def sql_connection(self):

        self.cur.execute("""CREATE TABLE IF NOT EXISTS useraccount(username TEXT,
                            password TEXT, Date date,name text ,color text,
                            script text, empty1 text, empty2 text, number int,
                            ID text, phone text)""")
        self.con.commit()

        self.cur.execute('SELECT username FROM useraccount')
        self.rows = self.cur.fetchall()

    def __iter__(self):
        """Checking the existance of username in the Database
        """
        for i in self.rows:                         
            for j in i:                             
                self.inside_values.append(j)
        if self.value[0:] in self.inside_values:
            self.COND = 1
            pass
        else:
            self.COND = 0
        yield self.inside_values

    def pass_check(self):
        self.cur.execute("SELECT password FROM useraccount WHERE username LIKE '%'||?||'%'", (self.value,))
        self.PASS_RESULT = self.cur.fetchone()[0]
        
    def Exec_values(self):
        """
        EXECUTING NEW VALUES 
        """
        if self.update == False:
            try:
                self.cur.execute('INSERT INTO useraccount values(?,?,?,?,?,?,?,?,?,?,?);', self.value)
                self.con.commit()
            except Error:
                print('Error with saving the values..')
        if self.update == True:
            #print(f'SET name to : {self.valueII}\nWHERE username LIKE {self.value}') 
            try:
                self.cur.execute("UPDATE useraccount set "+self.column+" = ? WHERE username LIKE '%'||?||'%'", (self.valueII, self.value,))
                self.con.commit()
            except Error:
                print('Error with updating the values..', error)
        self.update = False
        self.con.close()
#**************************
    def acc_env_call(self):
        self.cur.execute("SELECT * FROM useraccount WHERE username LIKE '%'||?||'%'", (self.value,))
        self.CALL_RESULT = self.cur.fetchall()

    def del_acc(self):
       self.cur.execute("DELETE FROM useraccount WHERE username LIKE '%'||?||'%'", (self.value,))
       self.con.commit()
       self.con.close()
        
        
    

#================================================================================================================================#
