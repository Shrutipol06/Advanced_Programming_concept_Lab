class Father:
    def skills1(self):
        print("Father: Driving")


class Mother:
    def skills2(self):
        print("Mother: Cooking")


class Child(Father, Mother):
    def skills3(self):
        print("Child: Drawing")


c = Child()

c.skills1()
c.skills2()
c.skills3()