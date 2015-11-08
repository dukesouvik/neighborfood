import tickets.py

class InsError(Exception):
    def __init__(self, typeOrg, typeIns, typeTick):
        self.org = typeOrg
        self.ins = typeIns
        self.tick = typeTick
        self.msg = "There are no default {} for this {}".format(self.ins, self.org)
        self.msg += " nor any specific {} for this {} ticket.".format(self.ins, self.tick)
    
class PInstructionsError(InsError):
    def __init__(self):
        super(PInstructionsError, self).__init__("Supplier", "pickup instructions", "supply")
        
class PHoursError(InsError):
    def __init__(self):
        super(PHoursError, self).__init__("Supplier", "pickup hours", "supply")
        
class DInstructionsError(InsError):
    def __init__(self):
        super(DInstructionsError, self).__init__("Distributor", "dropoff instructions", "request")

class DHoursError(InsError):
    def __init__(self):
        super(DHoursError, self).__init__("Distributor", "dropoff hours", "request")        

class Supplier(object):
    
    '''
        name (string) - what organization is it?
        address (dictionary) - formatted as {"number":"", "street":"", 
                    "city":"", "state":"", "zip":""}
        contact (string) - phone number
        typeOrg (string) - restaurant, supermarket, w/e they input in field
        email (string) - organization's email
        
        defaulted to NULL values, organization doesn't have to input immediately:
        defaultPickupInstructions (string) - how to usually pick up food
        defaultPickupHours (string) - when to usually pick up food
    '''
    def __init__(self, name, address, contact, typeOrg, email,
        defaultPickupInstructions = None, defaultPickupHours = None):
        
        self.name = name
        self.address = address
        self.contactInfo = contact
        self.typeOrg = typeOrg
        self.email = email
        
        self.tickets = []
        self.defaultPI = defaultPickupInstructions
        self.defaultPH = defaultPickupHours
        
    def addTicket(self, supplyTicket):
        if supplyTicket.PI or self.defaultPI:
            if supplyTicket.PI:
                pass
            else:
                supplyTicket.PI = self.defaultPI
        else:
            raise PInstructionsError
            
        if supplyTicket.PH or self.defaultPH:
            if supplyTicket.PH:
                pass
            else:
                supplyTicket.PH = self.defaultPH
        else:
            raise PHoursError
            
        self.tickets.append(supplyTicket)
        supplyTicket.source = self
    
    def removeTicket(self, supplyTicket):
        if supplyTicket in tickets:
            self.tickets.remove(supplyTicket)
            # TODO deletion of ticket from EVERYWHERE
        else:
            # TODO TODO TODO TODO
            pass

class Deliverer(object):
    
    '''
        name (string) - who is it?
        contact (string) - phone number 
        transportType (string) - car or pickupTruck, etc.
        email (string) - user's email
    '''
    def __init__(self, name, contact, transportType, email):
        self.name = name
        self.contactInfo = contact
        self.transport = transportType
        self.rating = 0
        self.email = email
        
    def updateRating(self, newValue):
        self.rating = newValue

class Requester(object):
        
    '''
        name (string) - what place is it?
        address (dictionary) - formatted as {"number":"", "street":"", 
                    "city":"", "state":"", "zip":""}
        contact (string) - phone number 
        typeOrg (string) - soup kitchen, food pantry
        email (string) - requester's email
        
        defaulted to NULL values, organization doesn't have to input immediately:
        defaultDropoffInstructions (string) - how to usually drop off food
        defaultDropoffHours (string) - when to usually drop off food
    '''
    
    def __init__(self, name, address, contact, typeOrg, email,
        defaultDropoffInstructions = None, defaultDropoffHours = None):
        
        self.name = name
        self.address = address
        self.contactInfo = contact
        self.typeOrg = typeOrg
        self.email = email

        self.tickets = []
        self.defaultDI = defaultDropoffInstructions
        self.defaultDH = defaultDropoffHours
    
    def addTicket(self, requestTicket):
        if requestTicket.DI or self.defaultDI:
            if requestTicket.DI:
                pass
            else:
                requestTicket.DI = self.defaultDI
        else:
            raise DInstructionsError
            
        if requestTicket.DH or self.defaultDH:
            if requestTicket.DH:
                pass
            else:
                requestTicket.DH = self.defaultDH
        else:
            raise DHoursError
            
        self.tickets.append(requestTicket)
        requestTicket.source = self
    
    def removeTicket(self, requestTicket):
        if requestTicket in tickets:
            self.tickets.remove(requestTicket)
        else:
            # TODO TODO TODO TODO
            pass
