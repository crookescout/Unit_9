import dog
import pack

my_dog = dog.Dog("Spot")
my_dog.print_name()
my_dog.sit()
my_dog.roll_over()
my_dog.print_trick_list()

my_pack = pack.Pack(my_dog)
print(my_pack.get_leader_name())
dog_2 = dog.Dog("Fido")
dog_3 = dog.Dog("Rover")

my_pack.add_member(dog_2)
my_pack.add_member(dog_3)

my_pack.print_pack()

