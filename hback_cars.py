import car,id_exception
class hback_cars(car.cars):

    def __init__(self):
        self.rate=8

    def car_add(self):
        no = int(input("How many cars do you want to add ?"))
        for x in range(no):
            dic = {'car_rate': 0, 'car_skms': 0, 'car_avl': True, 'car_cat': ''}
            car_id = input("Enter Car ID")
            try:
                if car_id in self.booked_cars or car_id in self.avl_cars:
                    raise id_exception.id_already_presents(car_id)
            except id_exception.id_already_presents as e:
                print(e)
                return
            dic['car_rate'] = self.rate
            dic['car_skms'] = int(input("Enter Starting Kms"))
            car_avl_t = input("Enter Car Availability")
            # car_avl=True
            if car_avl_t.startswith('Y') or car_avl_t.startswith('y'):
                # print("Entering if")
                dic['car_avl'] = True
                self.avl_cars.append(car_id)
            elif car_avl_t.startswith('N') or car_avl_t.startswith('n'):
                # print("Entering elif")
                dic['car_avl'] = False
                self.booked_cars.append(car_id)
            dic['car_cat'] = "hback"
            car_details = {car_id: dic}
            self.car_collection.append(car_details)