class cars:
    car_collection = []
    avl_cars = []
    booked_cars = []
    tp = 0
    def __init__(self):
        self.car_collection=[]
        self.avl_cars=[]
        self.booked_cars=[]
        self.tp=0


    def car_add(self):
        no=int(input("How many cars do you want to add ?"))
        for x in range(no):
            dic = {'car_rate': 0, 'car_skms': 0, 'car_avl': True, 'car_cat': ''}
            car_id = input("Enter Car ID")
            dic['car_rate'] = 10
            dic['car_skms'] = int(input("Enter Starting Kms"))
            car_avl_t = input("Enter Car Availability")
            # car_avl=True
            if car_avl_t is 'Y' or 'y':
                dic['car_avl'] = True
                self.avl_cars.append(car_id)
            else:
                dic['car_avl'] = False
                self.booked_cars.append(car_id)
            dic['car_cat'] = input("Enter Car Category")
            car_details = {car_id: dic}
            self.car_collection.append((car_details))


    def car_display(self,a):
        print("lenghth: ",len(self.car_collection))

        if a==1:
            print("Displaying all cars : ")
            for i in self.car_collection:
                print(i)
        if a==2:
            print("Displaying SUV Cars")
            for i in range(len(self.car_collection)):
                for j, k in self.car_collection[i].items():
                    if k['car_cat'] == 'suv':
                        print(k)
        if a == 3:
            print("Displaying HatchBack Cars")
            for i in range(len(self.car_collection)):
                for j, k in self.car_collection[i].items():
                    if k['car_cat'] == 'hback':
                        print(k)

    def car_display_avl(self,a):
        if a==1:
            print("All Available Cars :")
            for i in range(len(self.car_collection)):
                for j, k in self.car_collection[i].items():
                    if k['car_avl'] == True:
                        print(k)

        if a == 2:
            print("All Available SUV Cars :")
            for i in range(len(self.car_collection)):
                for j, k in self.car_collection[i].items():
                    if k['car_avl'] == True and k['car_cat'] == 'suv':
                        print(self.car_collection[i])

        if a == 3:
            print("All Available Hatchback Cars :")
            for i in range(len(self.car_collection)):
                for j, k in self.car_collection[i].items():
                    if k['car_avl'] == True and k['car_cat'] == 'suv':
                        print(self.car_collection[i])


    def car_display_booked(self,a):
        if a==1:
            print("All Booked Cars :")
            for i in range(len(self.car_collection)):
                for j, k in self.car_collection[i].items():
                    if k['car_avl'] == False :
                        print(self.car_collection[i])
        if a==2:
            print("All Booked Cars :")
            for i in range(len(self.car_collection)):
                for j, k in self.car_collection[i].items():
                    if k['car_avl'] == False and k['car_cat'] == 'suv' :
                        print(self.car_collection[i])

        if a==3:
            print("All Booked Cars :")
            for i in range(len(self.car_collection)):
                for j, k in self.car_collection[i].items():
                    if k['car_avl'] == False and k['car_cat'] == 'hback' :
                        print(self.car_collection[i])

    def car_book(self):
        id=input("Enter ID of car you want to book : ")
        print("booked your car")
        for i in range(len(self.car_collection)):
            for j,k in self.car_collection[i].items():
                if j==id:
                    k['car_avl']=False
                    print("found ",j)
                    print(self.car_collection[i])

    def car_cal_bill(self):
        id=input("Enter ID of car")
        end_kms=int(input("Enter End Kms "))
        print("calculating bill ")
        for i in range(len(self.car_collection)):
            for j,k in self.car_collection[i].items():
                if j==id:
                    total_kms=end_kms-k['car_skms']
                    bill=total_kms*k['car_rate']
                    print("Total Bill is : ",bill)
                    k['car_skms']=end_kms
                    k['car_avl']=True





