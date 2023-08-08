from Password_checker import passchecker
from encryption_controller import encryption
from Sq import SQL

#  ===========================   LOG-IN Controller  =========================== #
"""
 VAL = login(USER_NAME value, PASSWORD value)
 VAL.li_user_check()
 VAL.li_pass_check()

if VAL.USER_VAL.COND == 1:
    print('USERNAME IS CORRECT..')
    if VAL.LOG_IN_PASS_RESULT == 1:
        print('PASSWORD IS CORRECT..')
    else: print('PASSWORD IS INCORRECT..')
if VAL.USER_VAL.COND == 0:
    print('USERNAME DOESN\'T EXIST..')
"""
#  ============================================================================ #

class login:
    def __init__(self,USER_NAME, PASSWORD):
        self.USER_NAME = USER_NAME
        self.PASSWORD = PASSWORD
        self.LOG_IN_PASS_RESULT = 0
        self.USER_VAL = ''
        
    def li_user_check(self):
        """ Username checking in the Database
        """

        self.USER_VAL = SQL(self.USER_NAME)
        self.USER_VAL.sql_connection()
        next(self.USER_VAL.__iter__())

    def li_pass_check(self):
        """Password check in the Database
        """
        if self.USER_VAL.COND == 1:
            self.USER_VAL.pass_check()

            LI_EN_PASS = encryption(self.USER_VAL.PASS_RESULT)                          # Decrypt the password in the database
            LI_EN_PASS_R = LI_EN_PASS.Decrypt()
            
            if self.PASSWORD == LI_EN_PASS_R:
                self.LOG_IN_PASS_RESULT = 1
                

# ============================================================================  #
