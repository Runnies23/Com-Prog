class Course:
    def __init__(self, title, code, credit):
        self.title = title 
        self.course_id = code
        self.credit = credit

class Teacher:
    def __init__(self, firstname, lastname, id):
        self.firstname = firstname
        self.lastname = lastname
        self.id = id

    def __str__(self):
        return f"{self.firstname} {self.lastname} ({self.id})"
    
class Major:
    def __init__(self,  id, name, faculty):
        self.id = id
        self.name = name
        self.faculty = faculty

    def __str__(self):
        return f"{self.name} ({self.id})"
    

class Student:
    def __init__(self, id, firstname, lastname):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.courses = []
        self.num_course = []
        self.total_credit = 0
        self.advisor = None
        self.major = None

    def add_course(self, course) -> bool:
        if(self.total_credit+course.credit<=25 and course.title not in self.courses):
            self.courses.append(course.title)
            self.num_course.append(course.course_id)
            self.total_credit += course.credit
            return True
        else: return False
    
    def drop_course(self, course) -> bool:
        if(self.courses[-1]==course.title):
            self.courses.append("")
            self.courses.remove(course.title)
            self.num_course.remove(course.course_id)
            self.total_credit -= course.credit

            return True
        
        elif(len(self.courses)>0 and course.title in self.courses):
            self.courses.remove(course.title)
            self.num_course.remove(course.course_id)
            self.total_credit -= course.credit
            return True
        
        else: return False
    
    def set_advisor(self, advisor):
        self.advisor = advisor

    def set_major(self, major):
        self.major = major

    def __str__(self) -> str:
        txt = f"Student ID: {self.id}\nName: {self.firstname} {self.lastname}\nMajor: {self.major}\nAdvisor: {self.advisor}\nCourses: {' '.join(self.num_course)} "
        return txt
    
# test
c_ls = "01219111 01219113 01219245 01219221 01204212 01219213 01420113 01420114 01420111".split(" ")
ad = Teacher("Preeda", "Lerdpongvipusana", "E901")
m = Major("E17", "Software & Knowledge Engineering", "Engineering")
s = Student(5610546231, "Chinnaporn", "Soonue")

s.set_advisor(ad)
s.set_major(m)
for index, i in enumerate(c_ls):
    s.add_course(Course(f"sth{index}", i, 1))

s.drop_course(Course(f"sth2", "01219113", 1))

print(s)
print(s.total_credit)