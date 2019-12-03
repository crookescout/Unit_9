import dog

class Pack:

    def __init__(self, dog):
        self.dog = dog
        self.members = []
        self.leader_index = 0
        self.members.append(dog)

    def get_leader_name(self):
        return self.members[self.leader_index].get_name()