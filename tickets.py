class SupplyTicket(object):

    '''
        checklist (dict of boolean variables) - {"perishables":t/f,
                            "imperishables":t/f,
                            "packaged":t/f,
                            "unpackaged":t/f}
        foods (dict) - {"food1":units, "food2":units, etc...}
        
        Optional - organization does not have to input immediately
        pickupInstructions (string) - how to pickup this food
        pickupHours (string) - when to pickup this food      
    '''
    def __init__(self, checklist, foods, 
        pickupInstructions = None, pickupHours = None):
        self.checklist = checklist
        self.foods = foods
        self.PI = pickupInstructions
        self.PH = pickupHours
        self.source = None

class RequestTicket(object):
    
    '''
        checklist (dict) - {"perishables":t/f,
                            "imperishables":t/f,
                            "packaged":t/f,
                            "unpackaged":t/f}
        foods (dict) - {"food1":units, "food2":units, etc...}
        
        Optional - organzation does not have to input immediately
        dropoffInstructions (string) - dropoff directions for this food
        dropoffHours (string) - dropoff times for this food
    '''
    def __init__(self, checklist, foods,
        dropoffInstructions = None, dropoffHours = None):
        self.checklist = checklist
        self.foods = foods
        self.DI = dropoffInstructions
        self.DH = dropoffHours
        self.source = None
