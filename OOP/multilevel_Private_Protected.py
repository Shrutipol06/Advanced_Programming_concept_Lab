class Grandfather:
    def __init__(self):
        self.__money = 10000       # Private variable
        self._house = "Big House"  # Protected variable

    def __show_money(self):        # Private function
        print("Money:", self.__money)

    def _show_house(self):         # Protected function
        print("House:", self._house)

    def display(self):
        self.__show_money()
        self._show_house()


class Father(Grandfather):
    def show_father(self):
        print("Father class")
        self._show_house()


class Son(Father):
    def show_son(self):
        print("Son class")
        self._show_house()


s = Son()

s.display()
s.show_father()
s.show_son()