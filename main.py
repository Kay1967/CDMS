from Component.UserInterface import *
from DbContext.database import * 
from View.LoginView import *
#from View.AdminView import *
#from View.AdvisorView import *
from Repository.UserRepository import *
from Service.LoginService import *
from Domain.User import *
import sqlite3
from termcolor import colored

main_heading = '''
██████████████████████████████████████████████
█                                            █
█                 MY COMPANY                 █
█                 ----------                 █
█             Administration System          █
█                                            █
██████████████████████████████████████████████


Main Menu'''
# GLobal Variables
# --------------------------------------------------------------------
max_input_try = 3
company_db_name = 'mycompany.db'
client_tb_name = 'client'
users_tb_name = 'users'
#---------------------------------------------------------------------
dbContext = db(company_db_name, client_tb_name, users_tb_name)
loginView = LoginView(dbContext)
main_interface = user_interface(main_heading, menueitems = loginView.GetMenu())

if __name__ == "__main__":
    main_interface.run()