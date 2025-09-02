from finalrent import *
from readwrite import *


def admin_nonadmin():
    while True:
        
        user_inp = input('''
                        Are you the house-owner? 
                        --> Enter the password to login 
                        --> Press Enter to view the rental detail 
                        --> Enter 0 to exit the program: ''')
        
        if user_inp == 'yes':
            print('''
                  ----------------------------------------------------------------
                    Do you want to perform transaction or view the rental list? 
                    Press [1] to perform transaction
                    Press [2] to view the rental detail with rent amount
                  ----------------------------------------------------------------
                  ''')
            askk = input('\t\t\tEnter your choice (1 or 2): ')
            if askk == '1':
                main()
            
            elif askk == '2':
                design_a(rent_list=read_files())
                return admin_nonadmin()
            
        elif user_inp == "":
            design(rent_list=read_files())
            return admin_nonadmin()
        
        elif user_inp == '0':
            print("Exiting the program")
            break
        
        else:
            print("\nIncorrect password. Try again!!")
            return admin_nonadmin()
admin_nonadmin()  
