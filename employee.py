class Employee(object):
    '''Employee class models an employee (pilot or attendant) of an airline.'''
    def __init__(self, name, id, is_pilot, is_attendant):
        '''
        Initializes an Employee object with instance variables (see below).

        Parameters:
            name (str): employee name
            id (str): employee id
            is_pilot (boolean): True if employee is a pilot
            is_attendant (boolean): True if employee is an attendant
        
        Instance variables:
            _name: initialized with the value of parameter name
            _id: initialized with uppercased value of parameter id
            _is_pilot: initialized with the value of parameter is_pilot
            _is_attendant: initialized with the value of parameter is_attendant
        '''
        self._name = name
        self._id = id.upper()
        self._is_pilot = is_pilot
        self._is_attendant = is_attendant


    def name(self):
        '''Returns the value of _name attribute of self object.'''
        return self._name


    def id(self):
        '''Returns the value of _id attribute of self object.'''
        return self._id


    def is_pilot(self):
        '''Returns the value of _is_pilot attribute of self object.'''
        return self._is_pilot


    def is_attendant(self):
        '''Returns the value of _is_attendant attribute of self object.'''
        return self._is_attendant


    def __str__(self):
        '''Returns a printable string representation of self object.'''
        return 'Name: %s; ID: %s; Is Pilot? %s; Is Attendant? %s' % (self._name, \
            self._id, self._is_pilot, self._is_attendant)


    def __eq__(self, other):
        '''Returns True if self object is value equivalent to other object, False otherwise.'''
        return id(self)==id(other)
