from datetime import datetime 
from readwrite import *

# Main.py
def Shrestha_rental():
    """
    Displays the design for Shrestha Rental .
    """
    
    print('''
                               ------------------Shrestha Rental----------------------
                        
                                      ---------Gairigaon, Kathmandu---------
                                    
                            + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +
                            +                                                           +
                            +          SELECT A NUMBER YOU WANT :                       +
                            +                                                           +
                            +         Press [1]  --->  Display Rent Information         +
                            +         Press [2]  --->  Rent Payment (Bhada tirne)       +  
                            +         Press [3]  --->  Renter Left (Room xodeko)        +
                            +         Press [4]  --->  Add renter (Naya manxe)          +
                            +         Press [5]  --->  Increase rent                    +
                            +         Press [6]  --->  Exit                             +
                            +                                                           +
                            + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +        
        ''')
    
def design(rent_list):
    """
    Displays the rent inventory in a proper format.
    """
    # Print design for displaying inventory
    print("--------------------------------------------------------------------------------------------------------------")
 
    print("│ Room no. │ Name of People Living      │  Rent Given Month   │ How many month? │   Which Months Rent Given? │")
 
    print("--------------------------------------------------------------------------------------------------------------")
    
   
    for rent in rent_list:
        print((' '* 4) + str(rent['room']) + " " * (10 - len(str(rent['room'])))+rent['name_of_people'] + " " * (30 - len(rent['name_of_people']))+
                rent['kaile_deko'] + " " * (22 - len(rent['kaile_deko'])) + str(rent['kati_month']) + " " * (20 - len(str(rent['kati_month']))) +
                str(rent['kun_month']) + " " * (39 - len(str(rent['kun_month']))))
                #+ str(rent['rent_amount']) + " " * (10 - len(str(rent['rent_amount']))))  
    # Print bottom border
    print("--------------------------------------------------------------------------------------------------------------")

#inventory = read_files()
#design(inventory)

def operation(rent_list):
    inventory = read_files()
    design(inventory)
    while True:
        while True:
            try:
                room_no = int(input("\nEnter the Room Number: "))
                break
            except ValueError:
                print("\nPlease enter a numeric value.")
                
        # Check if rent exist or not
        rent_exist = None
        for rent in rent_list:
            if rent['room'] == room_no:
                rent_exist = rent
                break
            
        # If room number doesn't exist 
        if rent_exist is None:
            print("\nEnter valid Room number.")
        
        
    # If exist
        else:
            # To check if it is correct renter
            print('\nThe renter is:', rent['name_of_people'])
            sure = input("\nAre you sure to continue transaction?(y/n): ").lower()
            if sure == 'n':
                return 
            
                
            while True:
                try:
                    kati_month = int(input("\nHow many month of rent payment are they going to make?(Kati mahina ko ekaichoti dina lageko): "))
                    if kati_month <= 0:
                        print("\nEnter a positive number")
                    else:
                        break
                except ValueError:
                    print("\nPlease enter a numeric value.")
        
        
        for rent in rent_list:
            if rent['room'] == room_no:
                kun_kun_month = input('\nWhich months rent payment are they going to pay?(Kun month ko rent diyeko)(eg: Asar-Bhadra): ')
                month_paid = input('\nWhich month did they paid the rent?(Kaile rent diyeko): ')
                
                rent['kati_month'] = kati_month
                rent['kaile_deko'] =  month_paid
                rent['kun_month'] = kun_kun_month
                amount_paid = kati_month * rent['rent_amount']
                
                #print for confirmation of rent
                print(f"\n{kati_month} month rent paid by{rent['name_of_people']} with total {amount_paid}")
                
                #generating bill 
                year = str(datetime.now().year)
                
                with open(rent['name_of_people'] +" "+ year + ".txt", "w") as write_file:
                    invoice_detail = f"""
                                                                               
                    Invoice by: Jessica Shrestha        {datetime.now()}
                    ------------------------------------------------------------------------------  
                                                   
                    Name of renter:                     {rent['name_of_people']} 
                                              
                    How many month of rent paid:        {kati_month}
                    
                    Which month of rent paid:           {kun_kun_month}
                    
                    Rent Amount :                       Rs {rent['rent_amount']}
                    
                    Rent Paid At:                       {month_paid}
                    
                    ------------------------------------------------------------------------------   
                                                  
                    Total amount:                       Rs {amount_paid}                      
                    
                    """
                    write_file.write(invoice_detail)
                print("\nInvoice generated: ")
                print(invoice_detail)
                
        # Ask for another transaction
        another = input("\nDo you want to make another transaction? (y/n): ").strip().lower()
        if another == 'n':
            break
        
def leave_people(rent_list):
    leave = int(input("\nRenter of which room number is leaving?: "))
    
    # Check if rent exist or not
    rent_exist = None
    for rent in rent_list:
        if rent['room'] == leave:
            rent_exist = rent
            break
        
    # If room number doesn't exist 
    if rent_exist is None:
        print("\nEnter valid Room number.")

    # If exist
    else:
        # To check if it is correct renter
        print('\nThe renter is:', rent['name_of_people'])
        sure = input("\nAre you sure this person is leaving?(y/n): ").lower()
        if sure == 'n':
            return 
        elif sure == 'y':
            # Mark the room as empty
            rent['name_of_people'] = "EMPTY"
            rent['kaile_deko'] = "N/A"
            rent['kati_month'] = 0
            rent['kun_month'] = "N/A"
            rent['rent_amount'] = 0.0
            
            print(f"Room {rent['room']} is now marked as empty.")
            
            # Save the changes to the text file
            write_rent_data(rent_list)
            print("\nRent information updated in rents.txt.")  
            
def add_people(rent_list):
    
    all_occupied = True  # Flag to track if all rooms are occupied

    # Check if there is an empty room first
    for rent in rent_list:
        if rent['name_of_people'] == 'EMPTY':
            all_occupied = False
            break
    
    # If all rooms are occupied, terminate the function
    if all_occupied:
        print("Sorry! All rooms are occupied!")
        return
        
    add = int(input('\nWhich room number are they going to stay on?: '))
    # Check if rent exist or not
    rent_exist = None
    for rent in rent_list:
        if rent['room'] == add:
            rent_exist = rent
            break
        
    # If room number doesn't exist 
    if rent_exist is None:
        print("Enter valid Room number.")
    
    # CHeck if room is empty
    if rent['name_of_people'].upper() == "EMPTY":
        name = input('\nEnter the name of new renter: ')
        stay_in_month = input('\nWhich month did they join the room?: ')
        try:
            month_int = int(input('\nHow many month rent are they going to give?: '))
        except ValueError:
            print('\nEnter a number.')
            return
        
        which_month = input('\nWhich month rent? (eg: Asar-Bhadra): ')
        try:
            rentamount = float(input('\nRent Amount: '))
        except:
            print('Enter the rent amount.')
            return
        # Update the room data in the rent_list
        rent['name_of_people'] = name
        rent['kun_month'] = which_month
        rent['kati_month'] = month_int
        rent['kaile_deko'] = stay_in_month
        rent['rent_amount'] = rentamount
    
        print(f"\nNew renter {name} added to room {rent['room']}.")

    # Write the updated rent_list to the text file
        write_rent_data(rent_list)
        print("\nRent information updated in rent.txt.")
        #generating bill 
        year = str(datetime.now().year)
        amount_paid = month_int*rentamount
        
        with open(rent['name_of_people'] +" "+ year + ".txt", "w") as write_file:
            invoice_detail = f"""
                                                                        
            Invoice by: Jessica Shrestha        {datetime.now()}
            ------------------------------------------------------------------------------  
                                            
            Name of renter:                     {name} 
            
            Renter joined at:                   {stay_in_month}
                                        
            How many month of rent paid:        {month_int}
            
            Which month of rent paid:           {which_month}
            
            Rent Amount :                       Rs {rent['rent_amount']}
            
            ------------------------------------------------------------------------------   
                                            
            Total amount:                       Rs {amount_paid}                      
            
            """
            write_file.write(invoice_detail)
        print("\nInvoice generated: ")
        print(invoice_detail)
    else:
        print(f"\nRoom {add} is already occupied by {rent['name_of_people']}.")
        return add_people(rent_list=read_files())
    


def increase_rent(rent_list):
    """
    Increases rent amount for all rooms in the rent list.
    """
    try:
        amount = float(input("\nEnter the amount you want to increase: "))
    except ValueError:
        print("\nPlease enter a valid number for the amount.")
        return

    for rent in rent_list:
        rent['rent_amount'] += amount  # Increase rent for each room
    
    # After the loop, write the updated rent list to the file
    write_rent_data(rent_list)
    print(f"\nRent increased by {amount} for everyone.")
    


def main():
    """
    Main function to call other functions
    parameter: none
    
    """
    while True:
        Shrestha_rental()  # Display main message
        try:
            user_choice = int(input("\nEnter your choice (1-6): "))
            inventory = read_files()
            
            if user_choice == 1:
                design_a(inventory) # Display designed inventory
                return main()
                '''while True:
                    # Ask if user want to view collection again
                    ask_choice = input("Press y to view collection again \nPress [n] to exit inventory : ")
                    if ask_choice.lower() == "y":
                        design(inventory)
                    elif ask_choice.lower() == "n":
                        print() # To print newline character
                        print("""
                              **************************************
                              *  Thank you for the transaction. *
                              **************************************
                              """)
                        
                        break
                    else:
                        print("Please enter '[y]' to view collection or '[n]' to exit inventory") '''
                        
                        
            elif user_choice == 2:
                # Transaction
                rent_list = read_files()
                operation(rent_list)
                write_rent_data(rent_list)
                
            elif user_choice == 3:
                design(inventory)
                leave_people(rent_list=read_files())
                
            elif user_choice == 4:
                design(inventory)
                add_people(rent_list=read_files())
                
            elif user_choice == 5:
                rent_list = read_files()
                increase_rent(rent_list)
            
            elif user_choice == 6:
                print("\nThank you.")
                break # To end the program
                
            else:
                print("\nPlease select a valid option.")
        
        except ValueError:
            print("\nInvalid input. Please enter a number.")

#main()

