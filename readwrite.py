import os
'''
def get_absolute_path(filename):
    # Get the absolute path of the script's directory (works for both .py and .exe)
    base_path = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_path, filename)


def read_files():
    rent_list = []  # empty list to store rent details
    file_path = get_absolute_path('rents.txt')  # Get the absolute path of the file
    try:
        with open(file_path, 'r') as rent_file:
            for rent in rent_file:
                rent = rent.replace("\n", "").split(",")
                if len(rent) == 6:
                    rent_dictionary = {
                        'room': int(rent[0]),
                        'name_of_people': rent[1],
                        'kaile_deko': rent[2],
                        'kati_month': int(rent[3]),
                        'kun_month': rent[4],
                        'rent_amount': float(rent[5])
                    }
                    rent_list.append(rent_dictionary)
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    return rent_list

def write_rent_data(rent_list):
    file_path = get_absolute_path('rents.txt')  # Get the absolute path of the file
    with open(file_path, 'w') as file:
        for rent in rent_list:
            modify_data = f"{rent['room']},{rent['name_of_people']},{rent['kaile_deko']},{rent['kati_month']},{rent['kun_month']},{rent['rent_amount']}\n"
            file.write(modify_data)'''
            
            
def design_a(rent_list):
    """
    Displays the rent inventory in a proper format.
    """
    # Print design for displaying inventory
    print("-----------------------------------------------------------------------------------------------------------------------------")
 
    print("│ Room no. │ Name of People Living      │  Rent Given Month   │ How many month? │   Which Months Rent Given? │ Rent Amount")
 
    print("-----------------------------------------------------------------------------------------------------------------------------")
    
  
    
    for rent in rent_list:
        print((' '* 4) + str(rent['room']) + " " * (10 - len(str(rent['room'])))+rent['name_of_people'] + " " * (30 - len(rent['name_of_people']))+
                rent['kaile_deko'] + " " * (22 - len(rent['kaile_deko'])) + str(rent['kati_month']) + " " * (20 - len(str(rent['kati_month']))) +
                str(rent['kun_month']) + " " * (27 - len(str(rent['kun_month'])))
                + str(rent['rent_amount']) + " " * (10 - len(str(rent['rent_amount']))))
    # Print bottom border
    print("------------------------------------------------------------------------------------------------------------------------------")


# Read.py
def read_files():
    """
    parameter : none
    return: rent_list
    reads data from rents.txt
    """
    rent_list = []  # empty list to store rent details
    try:
        with open("rents.txt", 'r') as rent_file:  # change the file variable to avoid conflict
            for rent in rent_file:
                rent = rent.replace("\n", "").split(",")
                if len(rent) == 6:
                    rent_dictionary = {
                        'room': int(rent[0]),
                        'name_of_people': rent[1],
                        'kaile_deko': rent[2],
                        'kati_month': int(rent[3]),
                        'kun_month': rent[4],
                        'rent_amount': float(rent[5])
                    }
                    rent_list.append(rent_dictionary)
    except FileNotFoundError:
        print("File not found.")
    return rent_list

# Write.py
def write_rent_data(rent_list):
    """
    Modifies rent data in rents.txt file
    parameter: rent_list
    
    """
    with open('rents.txt', 'w') as file:
        for rent in rent_list:
            modify_data = f"{rent['room']},{rent['name_of_people']},{rent['kaile_deko']},{rent['kati_month']},{rent['kun_month']},{rent['rent_amount']}\n"          
            file.write(modify_data)
#print(read_files())