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

def print_cars_with_speed():
    speed = input("What speed? ")
    '''print all cars with speed'''
    db = sqlite3.connect("cars.db")
    cursor = db.cursor()
    sql = "SELECT * FROM car WHERE top_speed > ?;"
    cursor.execute(sql, (speed,))
    results = cursor.fetchall()
    print("car_name                      top_speed")
    # loop through all the results
    for car in results:
        print(f"{car[1]:<30}{car[2]:<4}")
    # loop finished here
    db.close()


# main code
while True:
    user_input = input(
    """
    What would you like to do?
    1. Print all cars
    2. Print cars with specific speed
    3. Exit
    """)
    if user_input == "1":
        print_all_cars()
    elif user_input == "2":
        print_cars_with_speed()
    elif user_input == "3":
        break
    else:
        print("That was not an option\n")