# private methods
class Hotel:

    def __init__(self):
        self.__bookRoom()
        self.__orderfood()

    @staticmethod
    def __bookRoom():
        print("Room Booked Success-fully")

    @staticmethod
    def __orderfood():
        print("Food Ordered Success-fully")


Hotel()

