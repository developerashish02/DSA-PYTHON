# creating a class blue print
class Mobile:
    def __init__(self, modal, camera):
        self.modal = modal
        self.camera = camera

    # actions or called as methods

    def makeCalls(self, number):
        print("Calling.....{}".format(number))

    # getting camera
    def get_camera(self):
        print(self.camera, "Hello Testing")


# creating a objects of a class or using blueprint
mobile_obj = Mobile("Apple 14", 64)
mobile_obj_2 = Mobile("I Phone 22", 9545959973)
# call methods
mobile_obj.makeCalls(8459618890)

# access the attributes
print(mobile_obj.modal)
print(mobile_obj.camera)
print(mobile_obj.get_camera())
# getting attributes of object 2
print(mobile_obj_2.modal)
print(mobile_obj_2.camera)
