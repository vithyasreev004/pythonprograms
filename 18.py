class StudentGrade:
    def __init__(self):
        self.w = 0
        self.l = 0
        self.a = 0

    def marks(self):
        self.w = float(input("ENTER THE WRITTEN TEST SCORE OUT OF 100: "))
        self.l = float(input("ENTER THE LAB TEST SCORE OUT OF 100: "))
        self.a = float(input("ENTER THE ASSIGNMENT TEST SCORE OUT OF 100: "))

    def score(self):
        wcount = self.w * 70 / 100
        lcount = self.l * 20 / 100
        acount = self.a * 10 / 100
        grade = (wcount + lcount + acount)
        print("THE WEIGHTED SCORE OF THE STUDENT:", grade)
obj = StudentGrade()
obj.marks()
obj.score()
