from Password_checker import passchecker
from encryption_controller import encryption
from Sq import SQL
from log_in import login
from Sign_up import Signup
from acc_env import acc_env


def main():

    """Define jumpin values"""
    root = 'off'
    Login = 'off'
    signup = 'off'
    environment = 'off'
    value = None
    

    while True:
        """LOG-IN LEVEL
        """  

        print("""
          ├————————————————————————————————————————————————————————————————╢ LOG_IN ╟————————————————————————————————————————————————————————————————————┤
(su) To Signup.
(exit) to exit.
              """)
        Login = 'off'
        LOG_USER_NAME = input('ENTER USERNAME : ')
        if LOG_USER_NAME.lower() == 'exit':
            break
        if LOG_USER_NAME.lower() == 'su':                                       # If the input value is "su", the rest of LOG-in
            signup = 'on'                                                       # procedure will be ignored and the operator goes
                                                                                # to SIGN-UP LEVEL.
        else:
            LOG_PASSWORD = input('ENTER PASSWORD : ')
        
            
            VAL = login(LOG_USER_NAME, LOG_PASSWORD)
            VAL.li_user_check()                                                 # Sending username to database to check.
            VAL.li_pass_check()                                                 # Sending password to database to chaeck.

            if VAL.USER_VAL.COND == 1:
                print('\nUSERNAME IS CORRECT..')
                if VAL.LOG_IN_PASS_RESULT == 1:
                    print('PASSWORD IS CORRECT..')
                else: print('PASSWORD IS INCORRECT..\n')
            if VAL.USER_VAL.COND == 0:
                print('\nUSERNAME DOESN\'T EXIST..\n')

            if VAL.LOG_IN_PASS_RESULT != 1 or VAL.USER_VAL.COND != 1:
                continue

            value = LOG_USER_NAME      # <===                                   # In case no problem with log_in, the variable value 
            environment = 'on'         # <===                                   # takes the value of Username. Then it will jump  
                                                                                # to USER ENVIRONMENT by turning the environment 'on'

        while True:

            """SIGN-UP LEVEL
            """

            if Login == 'on':
                break
            if signup == 'on':
                signup = 'off'
                S_U_MESSAGE = []
                FORBIDDEN_VALUES = [
                                    '',
                                    'cancel',
                                    'su',
                                    'logout',
                                    'login',
                                    'signout',
                                    'signin',
                                    'exit',
                                  ]
                print("""
         ├————————————————————————————————————————————————————————————————╢ SIGN_UP ╟————————————————————————————————————————————————————————————————————┤
                      """)
                #▌  █
                print('==> (cancel) to go back to login page')
                USER_NAME = input('Enter your Username : ')
                if USER_NAME.lower() == 'cancel':
                    break
                PASSWORD = input('Enter your Password :')
                NAME = input('Enter your full name :')
                while True:  
                    ID_NUMBER = input("Enter ID-Number : ")
                    PHONE = input("Enter Phone number : ")
                    if ID_NUMBER.isnumeric() and PHONE.isnumeric(): break
                    print('\n\t\t\t• Failure : ID or Phone value error..\n• Please re-Enter the values correctly..\n')

                SU = Signup(USER_NAME, PASSWORD, NAME, ID_NUMBER, PHONE)
                SU.su_user_check()


                if SU.USER_CHK_R == False:
                    S_U_MESSAGE.append('\n\t\t\t• Username is already exists; try another username..')
                elif USER_NAME.lower() in FORBIDDEN_VALUES or USER_NAME.isspace():
                    S_U_MESSAGE.append('\n\t\t\t• Username error : Forbidden value..')
                    SU.USER_CHK_R = False
                else:
                    S_U_MESSAGE.append('\n\t\t\t• Username is accepted..')
                    

                SU.su_pass_check()
                [S_U_MESSAGE.append(i) for i in SU.PSWCHK.reason if SU.PSWCHK.result == 'Not OK']

                for i in S_U_MESSAGE:
                    print('\t\t\t• ' + i)

                if SU.USER_CHK_R == True and SU.PSWCHK.result == 'OK':
                    SU.register()
                    print('\n\t\t\tº You are registered..')
                    break
                elif SU.USER_CHK_R != True or SU.PSWCHK.result != 'OK':
                    signup = 'on'
                    continue

                

            while True:

                """USER ENVIRONMENT
                """                                                     ################
                                                                        #  ROOT STAGE  #
                if Login == 'on':                                       ################
                    break
                if environment == 'on':
                    environment = 'off'
                    ENV = acc_env(value)
                    ENV.call_data()
                    print("""
      ├————————————————————————————————————————————————————————————————╢ USER ENVIRONMENT ╟————————————————————————————————————————————————————————————————————┤
                          """)                                                                        # call_data() should be in the loop so that it calls the data
                    print(ENV.HELP_TABLE , end = ' ')                                                 # every time the operator turns back into the root stage.
                    print(ENV.INFORMATION_TABLE)                            
                    ROOT_REQ_T = input(f'You are logged in as << {value} >> :')

                    if ROOT_REQ_T.lower() == 'logout':                                                # In order to log_out   
                        Login = 'on'                                                                  # and jump to log-in page 
                        break                                                                         

                    if ROOT_REQ_T.lower() == 'delete':
                        while True:
                            DEL_ACC_REQ = input('Are you sure you want to delete the user account?(y/n) : ')
                            if DEL_ACC_REQ.lower() == 'y':
                                DEL_ACC = SQL(value)
                                DEL_ACC.del_acc()
                                Login = 'on'
                                break
                            else:
                                break


                    if not ROOT_REQ_T.lower() in ENV.CALL_DICT:
                        print('Error..')
                        environment = 'on'
                        continue

                    

                    while True:                         ##############################
                                                        #  VERIFY THE REQUEST STAGE  #
                                                        ##############################
                        if root == 'on':                                                     #  Check if the root is 'on' to push the operator
                            root = 'off'                                                     #  to the root stage. the root variable could be
                            break                                                            #  turned to 'on' in any stage in order to jump 
                                                                                             #  into the root stage
                        for i in ENV.CALL_DICT:
                         
                            if ROOT_REQ_T.lower() == i:                                      #  Assigning the value of requested
                                ROOT_REQ_R = ENV.CALL_DICT[i]                                #  key "ROOT_REQ_T" to "ROOT_REQ_R"
                                VER_REQ = input(f'The {i} value is << {ENV.CALL_DICT[i]} >>. Are you sure you want to change it? (y/n): ')
                                break
        
                        if not VER_REQ.lower() == 'y':                                       # if the answer is not 'y': break the
                            environment = 'on'                                               # loop and go back to the previous stage.
                            break                                                            



                        while True:                     ############################
                                                        #  UPDATE THE VALUE STAGE  #
                                                        ############################                        
                            NEW_VALUE = input('Enter the new value (cancel) to back : ')
                            if NEW_VALUE.lower() == 'cancel':
                                root = 'on'                                                 # turn the root and environment 'on' and
                                environment = 'on'                                          # break to jump to the root stage.
                                break                                                       
                            print('=' * 150)
                            print(f'\n\t\t\t\tOLD value --> {ROOT_REQ_R}')
                            print(f'\n\t\t\t\tNEW value --> {NEW_VALUE}')

                            ENV = acc_env(value, ROOT_REQ_T, NEW_VALUE)                     # New object of acc_env class this time including
                            ENV.call_data()                                                 # attribiutes "ROOT_REQ_T" and "NEW_VALUE" in order
                            ENV.update_values()                                             # to update the values in the Database.
                
                            root = 'on'
                            environment = 'on'
                            break




    print('GOOD BYE')

if __name__ == '__main__':

    main()
