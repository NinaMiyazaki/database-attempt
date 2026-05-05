# docstring - Nina Miyazaki - cars database application
# imports
import sqlite3

# constants and variables
DATABASE = "cars.db"


# functions
def print_all_cars():
    '''print all cars nicely'''
    db = sqlite3.connect("cars.db")
    cursor = db.cursor()
    sql = "SELECT * FROM  car;"
    cursor.execute(sql)
    results = cursor.fetchall()
    print("car_name                      top_speed")
    # loop through all the results
    for car in results:
        print(f"{car[1]:<30}{car[2]:<4}")
    # loop finished here
    db.close()



# main code
while True:
    user_input = input("\nWhat would you like to do.\n1. Print all cars\n2. Exit\n")
    if user_input == "1":
        print_all_cars()
    elif user_input == "2":
        break
    else:
        print("That was not an option\n")