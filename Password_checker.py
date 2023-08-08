# ======================================================   Password controller  ==========================================#
'''
                                                    VAL = passchecker('INPUT VALUE')
                                                    VAL.check()
                                                    itrate in VAL.reason to print out reasons
                                                    VAL.result = 'OK'
                                                    VAL.result = 'Not OK'
'''
#  =======================================================================================================================#


class passchecker:
    def __init__(self, word):
        self.word = word
        self.reason = []
        self.result = ''
    def check(self):
        
        self.result = 'Not OK'
        if not any(i.isupper() for i in self.word):
            self.reason.append('Password should contains at least one upper word..')
        if not any(i.islower() for i in self.word):
            self.reason.append('Password should contains at least one lower word..')
        if not any(i.isdigit() for i in self.word):
            self.reason.append('Password should contains at least one number..')
        if len(self.word) < 8:
            self.reason.append('Password should contains at least 8 character..')
        if len(self.reason) == 0:
            self.reason.append('The password id fine..')
            self.result = 'OK'

    
#  =====================================================================================================================#        
