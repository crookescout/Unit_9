import dog


class Pack:

    def __init__(self, dog):
        self.dog = dog
        self.members = []
        self.leader_index = 0
        self.members.append(dog)

    def get_leader_name(self):
        return self.members[self.leader_index].get_name()

    def add_member(self, dog):
        self.members.append(dog)

    def print_pack(self):
        print("The pack contains:")
        for member in self.members:
            print(member.get_name())

