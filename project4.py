import sys

from airline import Airline
from employee import Employee
from flight import Flight

def display_menu():
    print(' 1. Create a new airline (starts with no employees and no flights)')
    print(' 2. Load airline data (airline info along with employees and flights) from a file')
    print(' 3. Save airline data (airline info along with employees and flights) to a file')
    print(' 4. Display airline information (name, airline code, and primary hub code)')
    print(' 5. Display list of employees')
    print(' 6. Display list of flights')
    print(' 7. Display crew for a flight')
    print(' 8. Add employee to airline database')
    print(' 9. Remove employee (by id) from airline database')
    print('10. Add flight to airline database')
    print('11. Remove flight (by number) from airline database')
    print('12. Find flights between two airports')
    print('13. Add crew to a flight')
    print('14. Remove crew from a flight')
    print('15. Exit program')

def get_menu_selection():
    while True:
        selection = input('Enter your selection (1 - 15) or press return for menu: ').strip()
        if selection == '':
            display_menu()
        else:
            selection = int(selection)
            if selection in range(1,16):
                break
            else:
                print('Invalid input. Try again.')
    return selection

def create_airline():
    try:
        airline_name = input('Enter airline name: ')
        airline_code = input('Enter airline IATA code: ')
        primary_hub_code = input('Enter primary hub code of this airline: ')
        return Airline(airline_name, airline_code, primary_hub_code)
    except Exception as ex:
        print(ex)

def load_airline_data_from_file():
    try:
        filename = input('Enter name of file to load the airline database from: ')
        airline = Airline.load_from_file(filename)
        return airline
    except Exception as ex:
        print(ex)

def save_airline_data_to_file(airline):
    try:
        filename = input('Enter name of file to save the airline database to: ')
        airline.save_to_file(filename)
    except Exception as ex:
        print(ex)

def display_airline_information(airline):
    print(airline)

def display_employees(airline):
    if len(airline.employees()) == 0:
        print('The airline currently has no employees.')
    else:
        for emp in airline.employees():
            print(emp)

def add_employee(airline):
    try:
        emp_name = input('Enter employee name: ')
        emp_id = input('Enter employee id: ')
        text = input('Is the employee a pilot? (y or n): ').upper()
        is_pilot = text == 'Y'
        employee = Employee(emp_name, emp_id, is_pilot, not is_pilot)
        airline.add_employee(employee)
    except Exception as ex:
        print(ex)

def remove_employee(airline):
    try:
        emp_id = input('Enter the id of employee to remove from airline database: ')
        airline.remove_employee(emp_id)
    except Exception as ex:
        print(ex)

def display_flights(airline):
    if len(airline.flights()) == 0:
        print('The airline currently has no flights.')
    else:
        for flight in airline.flights():
            print(flight)

def add_flight(airline):
    try:
        flight_nbr = int(input('Enter flight number: '))
        origin = input('Enter origin airport code: ')
        destination = input('Enter destination airport code: ')
        flight = Flight(flight_nbr, origin, destination)
        airline.add_flight(flight)
    except Exception as ex:
        print(ex)

def remove_flight(airline):
    try:
        flight_nbr = int(input('Enter the flight number of flight to remove from airline database: '))
        airline.remove_flight(flight_nbr)
    except Exception as ex:
        print(ex)

def display_flights_between_airports(airline):
    origin = input('Enter origin airport code: ')
    destination = input('Enter destination airport code: ')
    flights = airline.find_flights(origin, destination)
    if len(flights) == 0:
        print('There are no flights between origin and destination airports.')
    else:
        for flight in flights:
            print(flight)

def display_flight_crew(airline):
    try:
        flight_nbr = int(input('Enter flight number: '))
        flight_crew = airline.flight_crew(flight_nbr)
        if len(flight_crew) == 0:
            print('This flight currently has no crew assigned to it.') 
        else:       
            for crew in flight_crew:
                print(crew)
    except Exception as ex:
        print(ex)                

def add_crew_to_flight(airline):
    try:
        flight_nbr = int(input('Enter the flight number of flight to add crew to: '))
        employee_id = input('Enter the id of employee to add to this flight crew: ')
        airline.add_crew_to_flight(flight_nbr, employee_id)
    except Exception as ex:
        print(ex)

def remove_crew_from_flight(airline):
    try:
        flight_nbr = int(input('Enter the flight number of flight to remove crew from: '))
        employee_id = input('Enter the id of employee to remove from flight crew: ')
        airline.remove_crew_from_flight(flight_nbr, employee_id)
    except Exception as ex:
        print(ex)

def main():
    print('Welcome to Airline Database System...')
    airline = None
    display_menu()
    while True:
        selection = get_menu_selection()
        if selection == 1:
            airline = create_airline()
        elif selection == 2:
            airline = load_airline_data_from_file()
        elif selection == 3:
            save_airline_data_to_file(airline)
        elif selection == 4:
            display_airline_information(airline)
        elif selection == 5:
            display_employees(airline)
        elif selection == 6:
            display_flights(airline)
        elif selection == 7:
            display_flight_crew(airline)
        elif selection == 8:
            add_employee(airline)
        elif selection == 9:
            remove_employee(airline)
        elif selection == 10:
            add_flight(airline)
        elif selection == 11:
            remove_flight(airline)
        elif selection == 12:
            display_flights_between_airports(airline)
        elif selection == 13:
            add_crew_to_flight(airline)
        elif selection == 14:
            remove_crew_from_flight(airline)
        elif selection == 15:
            print('Exiting the program.')
            sys.exit()


# run main if this script is executed as a top-level program
if __name__ == '__main__':
    try:
        main()
    except Exception as ex:
        print(ex)        
