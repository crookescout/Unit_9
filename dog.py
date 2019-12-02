# Scout Crooke, 12/02/19, this program works on daily exercises

class Dog:

    def __init__(self, name):
        self.name = name
        self.trick_list = []

    def get_name(self):
        return self.name

    def print_name(self):
        print(self.name)

    def sit(self):
        print(str(self.name) + " sits.")
        self.trick_list.append("sit")

    def roll_over(self):
        print(str(self.name) + " rolls over.")
        self.trick_list.append("roll over")

    def bark(self):
        print(str(self.name) + " barks.")
        self.trick_list.append("bark")

    def trick_check(self):
        if self.trick_list == []:
            print(str(self.name) + " ")

