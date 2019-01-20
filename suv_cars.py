import car,id_exception
class suv_cars(car.cars):

    def __init__(self):
        self.rate=12
        # super().__init__()
        # self.car_collections=[]

    def car_add(self):
        no = int(input("How many cars do you want to add ?"))
        for x in range(no):
            dic = {'car_rate': 0, 'car_skms': 0, 'car_avl': True, 'car_cat': ''}
            car_id = input("Enter Car ID")
            try:
                if car_id in self.booked_cars or car_id in self.avl_cars:
                    raise id_exception.id_already_presents(id)
            except id_exception.id_already_presents as e:
                print(e)
                return
            dic['car_rate'] = self.rate
            dic['car_skms'] = int(input("Enter Starting Kms"))
            car_avl_t = input("Enter Car Availability")
            # car_avl=True
            # print("CAr is vaialbe ?", car_avl_t)
            if car_avl_t.startswith('Y') or car_avl_t.startswith('y'):
                # print("Entering if")
                dic['car_avl'] = True
                self.avl_cars.append(car_id)
            elif car_avl_t.startswith('N') or car_avl_t.startswith('n'):
                # print("Entering elif")
                dic['car_avl'] = False
                self.booked_cars.append(car_id)
            dic['car_cat'] = "suv"
            car_details = {car_id: dic}
            # self.car_collections.append(car_details)
            self.car_collection.append(car_details)



# if __name__=='__main__':
#     print("main")
#     c=suv_cars()
#     # c.initall()
#     cont=True
#     c.car_add()
#     c.car_display(1)
#     # c.car_book()
# if __name__=='__main__':
#     print("main")
#     c=suv_cars()
#     cont=True
#
#     while cont:
#         print(" Welcome User : \n Please choose one of the options given below :")
#         switcher = {1: c.car_add, 2: c.car_display, 3: c.car_book, 4: c.car_cal_bill, 5: c.car_display_booked,6: c.car_display_avl}
#         ch=int(input(" 1.Add Car/s \n 2.View all Cars \n 3.Book a car \n 4.Calculate Bill \n 5.view booked cars \n 6. view Available cars\n 7.Exit"))
#         if ch==7:
#             cont=False
#             break
#         switcher[ch]()
#
