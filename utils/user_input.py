from utils.common import MESSAGES

def y_or_n_input (msg) :
    while True :
        check_ignore_space = input(f"[Y/N] {msg} ").lower()
        if check_ignore_space == 'y' : return True
        elif check_ignore_space == 'n' : return False

def number_input (msg) :
    while True :
        try :
            return int(input(f"[Number] {msg} "))
        except ValueError :
            print("숫자를 입력해 주세요.")

class User_Input :
    def __init__(self) :
        self.delete_file_flag = None
        self.total_problem = -1
        self.target_problem = -1

        self.ignore_space_flag = None
        self.essentials = None
        self.forbiddens = None

        self.run()

    def run(self) :
        self._check_delete_file()
        if self.delete_file_flag : self._get_delete_problems()
        self._check_ignore_space()
        self._get_essentials()
        self._get_forbiddens()

    def _check_delete_file(self) :
        self.delete_file_flag = y_or_n_input(MESSAGES['check_delete_file'])

    def _get_delete_problems(self) :
        self.total_problem = number_input(MESSAGES['get_total_problem'])
        self.target_problem = number_input(MESSAGES['get_target_problem'])

    def _check_ignore_space(self) :
        self.ignore_space_flag = y_or_n_input(MESSAGES['check_ignore_space'])
    
    def _get_essentials(self) :
        self.essentials = input(MESSAGES['get_essentials']).split(',')
    
    def _get_forbiddens(self) :
        self.forbiddens = input(MESSAGES['get_forbiddens']).split(',')





        