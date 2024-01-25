# import module that defines unit-testing framework
import unittest

# import classes from modules
from airline import Airline
from employee import Employee
from flight import Flight

class Project4Test(unittest.TestCase):

    def test_add_employee_1(self):
        airline = Airline('American','AA','DFW')
        employee = Employee('James Cruise','AA-11111',True,False)
        airline.add_employee(employee)
        self.assertEqual(1,len(airline.employees()))
        self.assertTrue(employee in airline.employees())

    def test_add_employee_2(self):
        airline = Airline('American','AA','DFW')
        employee = Employee('John Doe','AA-22222',False,True)
        airline.add_employee(employee)
        self.assertEqual(1,len(airline.employees()))
        self.assertTrue(employee in airline.employees())

    def test_add_employee_3(self):
        airline = Airline.load_from_file('master.pkl')
        employee = Employee('Bradley Miller','AA-11112',True,False)
        airline.add_employee(employee)
        self.assertEqual(13,len(airline.employees()))
        self.assertTrue(employee in airline.employees())

    def test_add_employee_4(self):
        airline = Airline.load_from_file('master.pkl')
        employee = Employee('Samantha Jones','AA-88880',False,True)
        airline.add_employee(employee)
        self.assertEqual(13,len(airline.employees()))
        self.assertTrue(employee in airline.employees())

    def test_add_employee_5(self):
        with self.assertRaises(TypeError):
            airline = Airline('American','AA','DFW')
            airline.add_employee('John Doe')

    def test_add_employee_6(self):
        with self.assertRaises(TypeError):
            airline = Airline.load_from_file('master.pkl')
            airline.add_employee('John Doe')

    def test_add_employee_7(self):
        with self.assertRaises(ValueError):
            airline = Airline.load_from_file('master.pkl')
            employee = Employee('James Cruise','AA-11111',True,False)
            airline.add_employee(employee)

    def test_add_employee_8(self):
        with self.assertRaises(ValueError):
            airline = Airline.load_from_file('master.pkl')
            employee = Employee('James Smith','AA-11111',True,False)
            airline.add_employee(employee)

    def test_remove_employee_1(self):
        airline = Airline.load_from_file('master.pkl')
        airline.remove_employee('AA-55555')
        self.assertEqual(11,len(airline.employees()))
        emp_list = [emp for emp in airline.employees() if emp.id() == 'AA-55555']
        self.assertEqual([],emp_list)

    def test_remove_employee_2(self):
        with self.assertRaises(ValueError):
            airline = Airline.load_from_file('master.pkl')
            airline.remove_employee('AA-11335')

    def test_remove_employee_3(self):
        with self.assertRaises(ValueError):
            airline = Airline('American','AA','DFW')
            airline.remove_employee('AA-11335')

    def test_find_employee_1(self):
        airline = Airline.load_from_file('master.pkl')
        employee = airline.find_employee('AA-77777')
        self.assertEqual('AA-77777',employee.id())

    def test_find_employee_2(self):
        airline = Airline.load_from_file('master.pkl')
        employee = airline.find_employee('AA-44555')
        self.assertEqual(None,employee)

    def test_find_employee_3(self):
        airline = Airline('American','AA','DFW')
        employee = airline.find_employee('AA-44555')
        self.assertEqual(None,employee)

    def test_add_flight_1(self):
        airline = Airline('American','AA','DFW')
        flight = Flight(1210,'GRR','ORD')
        airline.add_flight(flight)
        self.assertEqual(1,len(airline.flights()))
        self.assertTrue(flight in airline.flights())

    def test_add_flight_2(self):
        airline = Airline.load_from_file('master.pkl')
        flight = Flight(1250,'GRR','ORD')
        airline.add_flight(flight)
        self.assertEqual(23,len(airline.flights()))
        self.assertTrue(flight in airline.flights())

    def test_add_flight_3(self):
        with self.assertRaises(TypeError):
            airline = Airline('American','AA','DFW')
            airline.add_flight('I am flight 3000')

    def test_add_flight_4(self):
        with self.assertRaises(TypeError):
            airline = Airline.load_from_file('master.pkl')
            airline.add_flight('I am flight 3000')

    def test_add_flight_5(self):
        with self.assertRaises(ValueError):
            airline = Airline.load_from_file('master.pkl')
            flight = Flight(1210,'GRR','ORD')
            airline.add_flight(flight)

    def test_add_flight_6(self):
        with self.assertRaises(ValueError):
            airline = Airline.load_from_file('master.pkl')
            flight = Flight(1210,'FRA','BLR')
            airline.add_flight(flight)

    def test_remove_flight_1(self):
        airline = Airline.load_from_file('master.pkl')
        airline.remove_flight(1230)
        self.assertEqual(21,len(airline.flights()))
        flight_list = [flight for flight in airline.flights() if flight.flight_nbr() == 1230]
        self.assertEqual([],flight_list)

    def test_remove_flight_2(self):
        with self.assertRaises(ValueError):
            airline = Airline.load_from_file('master.pkl')
            airline.remove_flight(1250)

    def test_remove_flight_3(self):
        with self.assertRaises(ValueError):
            airline = Airline('American','AA','DFW')
            airline.remove_flight(1250)

    def test_find_flight_1(self):
        airline = Airline.load_from_file('master.pkl')
        flight = airline.find_flight(1240)
        self.assertEqual(1240,flight.flight_nbr())

    def test_find_flight_2(self):
        airline = Airline.load_from_file('master.pkl')
        flight = airline.find_flight(1250)
        self.assertEqual(None,flight)

    def test_find_flight_3(self):
        airline = Airline('American','AA','DFW')
        flight = airline.find_flight(1250)
        self.assertEqual(None,flight)

    def test_flight_crew_1(self):
        airline = Airline.load_from_file('master.pkl')
        crew = airline.flight_crew(1210)
        self.assertEqual(4,len(crew))
        result = set([c.id() for c in crew])
        self.assertEqual({'AA-11111','AA-33333','AA-22222','AA-55555'},result)

    def test_flight_crew_2(self):
        with self.assertRaises(ValueError):
            airline = Airline('American','AA','DFW')
            airline.flight_crew(1250)

    def test_flight_crew_3(self):
        with self.assertRaises(ValueError):
            airline = Airline.load_from_file('master.pkl')
            airline.flight_crew(1250)

    def test_flights_between_airports_1(self):
        airline = Airline.load_from_file('master.pkl')
        flights = airline.find_flights('ORD','FRA')
        self.assertEqual(4,len(flights))
        result = set([f.flight_nbr() for f in flights])
        self.assertEqual({1240,1241,1242,1243},result)

    def test_flights_between_airports_2(self):
        airline = Airline.load_from_file('master.pkl')
        flights = airline.find_flights('GRR','FRA')
        self.assertEqual([],flights)

    def test_flights_between_airports_3(self):
        airline = Airline('Delta','DL','ATL')
        flights = airline.find_flights('GRR','ATL')
        self.assertEqual([],flights)

    def test_add_crew_to_flight_1(self):
        airline = Airline.load_from_file('master.pkl')
        airline.add_crew_to_flight(1230,'AA-11111')
        crew = airline.flight_crew(1230)
        self.assertEqual(5,len(crew))
        result = set([c.id() for c in crew])
        self.assertEqual({'AA-11111','AA-99990','AA-88885','AA-77777','AA-99995'},result)

    def test_add_crew_to_flight_2(self):
        with self.assertRaises(ValueError):
            airline = Airline.load_from_file('master.pkl')
            airline.add_crew_to_flight(1250,'AA-11111')

    def test_add_crew_to_flight_3(self):
        with self.assertRaises(ValueError):
            airline = Airline.load_from_file('master.pkl')
            airline.add_crew_to_flight(1210,'AA-10000')

    def test_add_crew_to_flight_4(self):
        with self.assertRaises(ValueError):
            airline = Airline.load_from_file('master.pkl')
            airline.add_crew_to_flight(1210,'AA-11111')

    def test_remove_crew_from_flight_1(self):
        airline = Airline.load_from_file('master.pkl')
        airline.remove_crew_from_flight(1230,'AA-99990')
        crew = airline.flight_crew(1230)
        self.assertEqual(3,len(crew))
        result = set([c.id() for c in crew])
        self.assertEqual({'AA-88885','AA-77777','AA-99995'},result)

    def test_remove_crew_from_flight_2(self):
        with self.assertRaises(ValueError):
            airline = Airline.load_from_file('master.pkl')
            airline.remove_crew_from_flight(1250,'AA-11111')

    def test_remove_crew_from_flight_3(self):
        with self.assertRaises(ValueError):
            airline = Airline.load_from_file('master.pkl')
            airline.remove_crew_from_flight(1210,'AA-10000')

    def test_remove_crew_from_flight_4(self):
        with self.assertRaises(ValueError):
            airline = Airline.load_from_file('master.pkl')
            airline.remove_crew_from_flight(1210,'AA-66666')

    def test_flight_deck_crew(self):
        airline = Airline.load_from_file('master.pkl')
        flight = airline.find_flight(1210)
        result = set([c.id() for c in flight.deck_crew()])
        self.assertEqual({'AA-11111','AA-33333'},result)

    def test_flight_cabin_crew(self):
        airline = Airline.load_from_file('master.pkl')
        flight = airline.find_flight(1210)
        result = set([c.id() for c in flight.cabin_crew()])
        self.assertEqual({'AA-22222','AA-55555'},result)


# run the unit tests only if this script is executed as a top-level program
if __name__ == '__main__':
    unittest.main(verbosity=2)
