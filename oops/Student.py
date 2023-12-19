class Student:
    def __init__(self):
        self.name = ""
        self.marks = []
        self.address = ""

    # setup name
    def seName(self, name):
        self.name = name

    # setup marls
    def set_address(self, student_address):
        self.address = student_address

    # cal average
    def cal_avg(self):
        avg = 0
        for item in self.marks:
            avg += item

        return avg

# creating a object


# student 01
student_01 = Student()
student_01.seName("Ashish")
student_01.set_address("June Pargoan")

print(student_01.name)


# student 02
student_02 = Student()
student_02.seName("Akash")
student_02.set_address("Kolhapur")

print(student_02.name)
