class Student:
    # Access modifier
    # private :
    # private member only access the within the class not outside the class
    # Note - This Not a class attribute this a private attribute
    __adhara_card = ""
    __pad_card = None

    def __init__(self, name, pan_card, adhara_card):
        self.name = name
        self.__pad_card = pan_card
        self.__adhara_card = adhara_card

    def get_adhara_card(self):
        return self.__pad_card


student_01 = Student("Ashish", "CRTPG5371G", 651329811261)

print(student_01.get_adhara_card())
