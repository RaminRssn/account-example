import datetime
from encryption_controller import encryption
from Sq import SQL
#   ============================================================   Account Enviroment Controller  =========================================================  #
'''

VAL = acc_env(value)
root = 'off'

  |while True:
  |    **ROOT STAGE**
  |    while True:
  |        **VERIFY THE REQUEST STAGE**
  |        while True:
  |           **UPDATE THE VALUE STAGE**

                        "The module uses nested while loops in order to bring back the operator
                         to the previous stage while necessary. To jump into the root stage the
                         root variable should be 'on'. New object for SQL module is needed in the
                         UPDATE THE VALUE STAGE so that the new values be sent to the SQL module.  

    VAL.call_data()      "To call data from SQL module using the username as value.
    ENV.update_values()  "To update the requested value, using SQL module.

ROOT_REQ_T --> << Input the request key in the ROOT STAGE >>
ROOT_REQ_R --> << The value of the request key --> VERIFY THE REQUEST STAGE >>
VER_REQ -----> << Verify the request (y/n) question --> VERIFY THE REQUEST STAGE >>
DEL_ACC_REQ -> << Verify deleting the account --> ROOT STAGE >>
NEW_VALUE ---> << New value for the requested key --> UPDATE THE VALUE STAGE >>

            |VAL = acc_env(value, ROOT_REQ_T, NEW_VALUE)    # New object in UPDATE THE VALUE STAGE
            |VAL.call_data()                                # to finalize the update using SQL module
            |VAL.update_values()    

'''


#   =======================================================================================================================================================  #
class acc_env:
    """Account Environment"""
    def __init__(self, value, ROOT_REQ_T = None, NEW_VALUE = None, update = False):

        self.value = value
        self.ROOT_REQ_T = ROOT_REQ_T
        self.NEW_VALUE = NEW_VALUE
        self.update = update
        self.CALL_DICT = None
        self.CALL_TUPLE = None
        self.HELP_TABLE = f"""        
                        +------------+---------------------------+
                        |   Value    |          Purpose          |
                        +============+===========================+
                        |   username |  To change the Username   |
                        +------------+---------------------------+
                        |    name    |       to change name      |
                        +------------+---------------------------+
                        |    color   |       to chane color      |
                        +------------+---------------------------+
                        |    script  |      To write a script    | 
                        +------------+---------------------------+
                        |  password  |    To change password     |
                        +------------+---------------------------+
                        |    ID      |    To chane ID number     |
                        +------------+---------------------------+
                        |    phone   |   To change phone number  |
                        +------------+---------------------------+
                        |   delete   |   To delete the account   |
                        +------------+---------------------------+
                        |   logout   |  To sign-out the account  |
                        +============+===========================+
                    """
        
        
        self.EN_REQ_LIST = [
                             'password',
                             'script',
                             'ID',
                             'phone',
                           ]
        
    def call_data(self):
        

        CALL = SQL(self.value, self.ROOT_REQ_T, self.NEW_VALUE, self.update)
        CALL.acc_env_call()
        self.CALL_TUPLE = CALL.CALL_RESULT
        

        self.CALL_DECRYPTED_PASSWORD = encryption(self.CALL_TUPLE[0][1]).Decrypt() if not self.CALL_TUPLE[0][1] == '' else None
        self.CALL_DECRYPTED_ID_NUMBER = encryption(self.CALL_TUPLE[0][9]).Decrypt() if not self.CALL_TUPLE[0][9] == '' else None
        self.CALL_DECRYPTED_PHONE = encryption(self.CALL_TUPLE[0][10]).Decrypt() if not self.CALL_TUPLE[0][10] == '' else None
        self.CALL_DECRYPTED_SCRIPT = encryption(self.CALL_TUPLE[0][5]).Decrypt() if not self.CALL_TUPLE[0][5] == '' else None

        self.CALL_DICT = {
                             'username' : self.CALL_TUPLE[0][0],
                             'password' : self.CALL_DECRYPTED_PASSWORD,
                             'name' : self.CALL_TUPLE[0][3],
                             'color' : self.CALL_TUPLE[0][4],
                             'script' : self.CALL_DECRYPTED_SCRIPT,
                             'id' : self.CALL_DECRYPTED_ID_NUMBER,
                             'phone' : self.CALL_DECRYPTED_PHONE
                         }

        self.INFORMATION_TABLE = f"""

        Username :   {self.CALL_TUPLE[0][0]}
        _________
         
        Name:        {self.CALL_TUPLE[0][3]}
        _________

        ID Number :  {self.CALL_DECRYPTED_ID_NUMBER}
        _________

        Phone :      {self.CALL_DECRYPTED_PHONE}
        _________
   

                            """
            
    def update_values(self):
        if self.ROOT_REQ_T in self.EN_REQ_LIST:
            ACC_ENI = encryption(self.NEW_VALUE)
            self.NEW_VALUE = ACC_ENI.Encrypt()

        
        UPDATE = SQL(self.value, self.ROOT_REQ_T, self.NEW_VALUE, update = True)
        UPDATE.sql_connection()
        UPDATE.Exec_values()
        
            

#########################################
'''
value = 'ramin'                                             # Set 'ramin' as value for example

ENV = acc_env(value)                                        # First object of Account Environment
                                                            # only for reading the values of the 
root = 'off'                                                # specific column in the database table.

login = 'off'
                     ################
## ===============   #  ROOT STAGE  #   
                     ################
while True:
    if login == 'on' :
        break
    ENV.call_data()                                         # call_data() should be in the loop so that it calls the data
    print(ENV.HELP_TABLE , end = ' ')                       # every time the operator turns back into the root stage.
    print(ENV.INFORMATION_TABLE)                            
    ROOT_REQ_T = input(f'You are logged in as << {value} >> :')

    if ROOT_REQ_T.lower() == 'delete':
        while True:
            DEL_ACC_REQ = input('Are you sure you want to delete the user account?(y/n) : ')
            if DEL_ACC_REQ.lower() == 'y':
                DEL_ACC = SQL(value)
                DEL_ACC.del_acc()
                login = 'on'
                break
            else:
                break


    if not ROOT_REQ_T in ENV.CALL_DICT:
        continue


                     ##############################
## ===============   #  VERIFY THE REQUEST STAGE  #   
                     ##############################

    while True:
       
        if root == 'on':                                    #  Check if the root is 'on' to push the operator
            root = 'off'                                    #  to the root stage. the root variable could be
            break                                           #  turned to 'on' in any stage in order to jump 
                                                            #  into the root stage
        for i in ENV.CALL_DICT:
    
            if ROOT_REQ_T == i:                             #  Assigning the value of requested
                ROOT_REQ_R = ENV.CALL_DICT[i]               #  key "ROOT_REQ_T" to "ROOT_REQ_R"
                VER_REQ = input(f'The {i} value is << {ENV.CALL_DICT[i]} >>. Are you sure you want to change it? (y/n): ')
                break
    
        if not VER_REQ.lower() == 'y':                      # if the answer is not 'y': break the
            break                                           # loop and go back to the previous stage.
      
            
                     ############################
## ===============   #  UPDATE THE VALUE STAGE  #   
                     ############################
        

        while True:
            NEW_VALUE = input('Enter the new value (cancel) to back : ')
            if NEW_VALUE.lower() == 'cancel':
                root = 'on'                                 # turn the root 'on' and break to jump to
                break                                       # to the root stage.
            print('=' * 150)
            print(f'\n\t\t\t\tOLD value --> {ROOT_REQ_R}')
            print(f'\n\t\t\t\tNEW value --> {NEW_VALUE}')

            ENV = acc_env(value, ROOT_REQ_T, NEW_VALUE)     # New object of acc_env class this time including
            ENV.call_data()                                 # attribiutes "ROOT_REQ_T" and "NEW_VALUE" in order
            ENV.update_values()                             # to update the values in the Database.
            
            root = 'on'
            break

'''
