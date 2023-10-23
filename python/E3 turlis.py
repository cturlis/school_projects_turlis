attend =0
grades =0

class Student:
    def __init__(self,first_name,last_name,attend,grades):
        List_grades = []
        self.first_name= first_name
        self.last_name= last_name
        self.attend= attend
        self.grades= grades

    def __str__(self):
        print(str(self.first_name)+" "+str(self.last_name))
        print("attendance"+" "+str(self.attend))
        print("grades"+" "+ str(List_grades))
    
    def full_name(self):
        return self.first_name+" "+self.last_name

    def get_attend(self):
        return self.attend

    def class_attend(self):
        self.attend += 1

    def get_grades(self):
        return grades

    def add_grades(self,new_grades):
        self.grades = new_grades
        List_grades.append(new_grades)
        return List_grades
    
List_grades=[]

def main():
    person1= Student("Hugh","Mungus",int(attend),grades)
    person1.add_grades(67)
    person1.add_grades(90)
    person1.add_grades(87)
    print(person1.full_name())
    print("grades",List_grades)
    person1.class_attend()
    person1.class_attend()
    person1.get_attend()
    person1.__str__()


if __name__=="__main__":
    main()
        
        

    
