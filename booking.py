import suv_cars,hback_cars

class booking(suv_cars.suv_cars,hback_cars.hback_cars):

    def car_add(self):
        ch=int(input("Select which car/s you want to add :\n1.SUV\n2.Hatchback"))
        if ch==1:
            for cls in booking.__bases__:
                if cls.__name__=='suv_cars':
                    cls().car_add()

        if ch==2:
            for cls in booking.__bases__:
                if cls.__name__=='hback_cars':
                    cls().car_add()

    def car_display(self):
        ch = int(input("Select which car/s you want to display :\n1.All Cars\n2.SUV\n3.Hatchback"))
        super().car_display(ch)


    def car_display_avl(self):
        ch = int(input("Select which available car/s you want to display :\n1.All Cars\n2.SUV\n3.Hatchback"))
        super().car_display_avl(ch)

    def car_display_booked(self):
        ch = int(input("Select which booked car/s you want to display :\n1.All Cars\n2.SUV\n3.Hatchback"))
        super().car_display_booked(ch)


if __name__=='__main__':
    print("main")
    c=booking()
    cont=True
    # c.car_add()
    # c.car_display()


    while cont:
        print(" Welcome User : \n Please choose one of the options given below :")
        switcher = {1: c.car_add, 2: c.car_display, 3: c.car_book, 4: c.car_cal_bill, 5: c.car_display_booked,6: c.car_display_avl}
        ch=int(input(" 1.Add Car/s \n 2.View all Cars \n 3.Book a car \n 4.Calculate Bill \n 5.view booked cars \n 6. view Available cars\n 7.Exit"))
        if ch==7:
            cont=False
            break
        switcher[ch]()