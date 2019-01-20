
class id_already_booked(Exception):
    def __init__(self,id):
        self.id=id

    def __str__(self):
        strg="Car with ID : "+self.id+" Already Booked.Please select the car from available cars"
        return repr(strg)

class id_already_available(Exception):
    def __init__(self,id):
        self.id=id

    def __str__(self):
        strg="Car with ID : "+self.id+" Already Available.To calculate bill ,Please select the car from booked cars"
        return repr(strg)


class id_already_presents(Exception):
    def __init__(self,id):
        self.id=id

    def __str__(self):
        strg="Car with entered ID Already Present.To add car please select another ID"
        return repr(strg)

