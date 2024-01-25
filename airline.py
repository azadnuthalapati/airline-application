# pickle module is used for saving and loading an Airline object to and from external files.
import pickle

from employee import Employee
from flight import Flight

class Airline(object):
    '''Airline class models an airline with a list of employees and flights.'''

    def __init__(self, name, airline_code, primary_hub_code):
        '''
        Initializes an Airline object with instance variables (see below).

        Parameters:
            name (str): airline name
            airline_code (str): two-character code of airline
            primary_hub_code (str): three-letter code of airline's primary hub airport
        
        Instance variables:
            _name: initialized with the value of parameter name
            _airline_code: initialized with uppercased value of parameter airline_code
            _primary_hub_code: initialized with uppercased value of parameter primary_hub_code
            _employees: initialized to empty list
            __lights: initialized to empty list
        '''
        self._name = name
        self._airline_code = airline_code.upper()
        self._primary_hub_code = primary_hub_code.upper()
        self._employees = []
        self._flights = []


    def name(self):
        '''Returns the value of _name attribute of self object.'''
        return self._name


    def airline_code(self):
        '''Returns the value of _airline_code attribute of self object.'''
        return self._airline_code


    def primary_hub_code(self):
        '''Returns the value of _primary_hub_code attribute of self object.'''
        return self._primary_hub_code


    def employees(self):
        '''Returns the value of _employees attribute of self object.'''
        return self._employees


    def flights(self):
        '''Returns the value of _flights attribute of self object.'''
        return self._flights

    def find_employee(self, employee_id):
        '''
        Returns the employee with the given employee id.

        Parameter:
            employee_id (str): id of the employee to find in the list of employees

        Returns: Employee instance if found or None otherwise
        '''
        if (len(self._employees)):
            for i in self._employees:
                if i._id==employee_id:
                    return i
        return None

    def find_flight(self, flight_nbr):
        '''
        Returns the flight with the given flight_nbr.

        Parameter:
            flight_nbr (int): number of the flight to find in the list of flights

        Returns: Flight instance if found or None otherwise
        '''
        if(len(self._flights)):
            for i in self._flights:
                if i._flight_nbr==flight_nbr:
                    return i
        return None
    

    def add_employee(self, employee):
        '''
        Adds an employee to the list of employees of this airline.

        Parameter:
            employee (Employee): employee to add to the list of employees after validation(s)

        Validations and exceptions raised:
            - TypeError if employee is not an instance of Employee
            - ValueError if employee is already present in the list of employees
            - ValueError if there exists an employee in the list with the same employee id
                (can't have two employees with the same employee id)

        Implementation requirements:
            - Must make use of self.find_employee()
        '''
        if(not isinstance(employee,Employee)):
            raise TypeError("employee is not an instance of class Employee")
        elif employee in self._employees:
            raise ValueError("employee is already present in the list of employees")
        elif self.find_employee(employee._id)!=None:
            raise ValueError("can't have two employees with the same employee id")
        else:
            self._employees.append(employee)


    def remove_employee(self, employee_id):
        '''
        Removes the employee with given employee id from the list of employees.
        Removing an employee also requires that you remove this employee from the crew of any flights
        where this employee is assigned as a member.

        Parameter:
            employee_id (str): id of the employee to be removed from the list of employees

        Validations and exceptions raised:
            - ValueError if employee with given id not found in the list of employees

        Implementation requirements:
            - Must make use of self.find_employee()     
        '''
#         if(not isinstance(employee,Employee)):
#             raise TypeError("employee is not an instance of class Employee")
#         elif employee not in self._employees:
#             raise ValueError("employee is not present in the list of employees")
#         elif self.find_employee(employee._id)==None:
#             raise ValueError("can't find the employee with the given employee id")
#         else:
#             self._employees.remove(employee)
        if self.find_employee(employee_id)==None:
            raise ValueError("employee with given id not found in the list of employees")
        else:
            self._employees.remove(self.find_employee(employee_id))


    


    def add_flight(self, flight):
        '''
        Adds a flight to the list of flights of this airline.

        Parameter:
            flight (Flight): flight to add to the list of flights after validation(s)

        Validations and exceptions raised:
            - TypeError if flight is not an instance of Flight
            - ValueError if flight is already present in the list of flights
            - ValueError if there exists a flight in the list with the same flight number
                (can't have two flights with the same flight number)

        Implementation requirements:
            - Must make use of self.self.self.find_flight()
        '''
        if(not isinstance(flight,Flight)):
            raise TypeError("flight is not an instance of class Flight")
        elif flight in self._flights:
            raise ValueError("flight is already present in the list of Flight")
        elif self.find_flight(flight._flight_nbr)!=None:
            raise ValueError("can't have two flights with the same flight nbr")
        else:
            self._flights.append(flight)


    def remove_flight(self, flight_nbr):
        '''
        Removes the flight with given flight number from the list of flights.

        Parameter:
            flight_nbr (int): number of the flight to remove from the list of flights

        Validations and exceptions raised:
            - ValueError if flight with given number not found in the list of flights

        Implementation requirements:
            - Must make use of self.self.self.find_flight()     
        '''
        if self.find_flight(flight_nbr)==None:
            raise ValueError("flight with given nbr not found in the list of flights")
        else:
            self._flights.remove(self.find_flight(flight_nbr))


    def find_flights(self, origin, dest):
        '''
        Returns a list of flights between origin airport and destination airport. The returned
        list could be empty if there are no flights between origin and destination airports.

        Parameters:
            origin (str): code of origin airport
            dest (str): code of destination airport
        '''
        lst=[]
        for i in self._flights:
            if i._origin_airport_code==origin and i._dest_airport_code==dest:
                lst.append(i)
        return lst


    def flight_crew(self, flight_nbr):
        '''
        Returns a list of crew for the flight with given flight number. The returned
        list could be empty if the flight has no crew assigned yet.

        Parameters:
            flight_nbr (int): flight number

        Validations and exceptions raised:
            - ValueError if flight with given number not found in the list of flights

        Implementation requirements:
            - Must make use of self.self.find_flight()
        '''
        if self.find_flight(flight_nbr)==None:
            raise ValueError("flight with given number not found in the list of flights")
        else:
            return self.find_flight(flight_nbr)._crew


    def add_crew_to_flight(self, flight_nbr, employee_id):
        '''
        Adds a member to the crew of the flight with given flight number.

        Parameters:
            flight_nbr (int): flight number
            empolyee_id (str): id of the employee to be added to the flight crew

        Validations and exceptions raised:
            - ValueError if flight with given number not found in the list of flights
            - ValueError if employee with given id not found in the list of employees
            - ValueError if employee to add is already a member of the flight crew

        Implementation requirements:
            - Must make use of self.self.find_flight()
            - Must make use of self.find_employee()
        '''
        if self.find_flight (flight_nbr)==None:
            raise ValueError("flight with given number not found in the list of flights")
        elif self.find_employee(employee_id)==None:
            raise ValueError("employee with given id not found in the list of employees")
        elif self.find_employee(employee_id) in self.find_flight(flight_nbr)._crew:
            raise ValueError("employee to add is already a member of the flight crew")
        else:
            self.find_flight(flight_nbr)._crew.append(self.find_employee(employee_id))


    def remove_crew_from_flight(self, flight_nbr, employee_id):
        '''
        Removes a member from the crew of the flight with given flight number.

        Parameters:
            flight_nbr (int): flight number
            empolyee_id (str): id of the employee to remove from the flight crew

        Validations and exceptions raised:
            - ValueError if flight with given number not found in the list of flights
            - ValueError if employee with given id not found in the list of employees
            - ValueError if employee to remove is not a member of the flight crew

        Implementation requirements:
            - Must make use of self.self.find_flight()
            - Must make use of self.find_employee()
        '''
        if self.find_flight(flight_nbr)==None:
            raise ValueError("flight with given number not found in the list of flights")
        elif self.find_employee(employee_id)==None:
            raise ValueError("employee with given id not found in the list of employees")
        elif self.find_employee(employee_id) not in self.find_flight(flight_nbr)._crew:
            raise ValueError("employee to remove is not a member of the flight crew")
        else:
            self.find_flight(flight_nbr)._crew.remove(self.find_employee(employee_id))


    def __str__(self):
        '''Returns a printable string representation of Airline object.'''
        return 'Airline: %s; Airline Code: %s; Primary Hub Code: %s' % (self._name,
            self._airline_code, self._primary_hub_code)


    def __eq__(self, other):
        '''Returns True if self object is value equivalent to other object, False otherwise.'''
        return (self._name,self._airline_code,self._primary_hub_code)==(other._name,other._airline_code,other._primary_hub_code)


    def save_to_file(self, filename):
        '''
        Saves the self Airline instance to the specified file using Python object serialization.

        Parameter:
            filename (str): name of the file to save the airline database to
        '''
        with open(filename, 'wb') as outfile:
            pickle.dump(self, outfile, pickle.DEFAULT_PROTOCOL)


    @staticmethod
    def load_from_file(filename):
        '''
        Loads the airline database information from the specified file and returns
        an Airline object with all its data.

        Parameter:
            filename (str): name of the file to load the airline database from
        '''
        with open(filename, 'rb') as infile:
            airline = pickle.load(infile)  
            return airline


'''a = Airline('American','AA','DFW')
employee = Employee('James Cruise','AA-11111',True,False)
flight = Flight(1210,'GRR','ORD')
a.add_employee(employee)
a.add_flight(flight)
#airline = Airline('American','AA','DFW')'''
'''print(a.find_employee(employee._id))'''
