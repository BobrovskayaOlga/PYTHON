from student import Student
from course_group import CourseGroup

student = Student("Виктор", "Бобровский", 19, "Электромеханик")
classmate1 = Student("Артем", "Лавров", 18, "Электромеханик")
classmate2 = Student("Анна", "Соколова", 19, "Электромеханик")
classmate3 = Student("Дмитрий", "Федорович", 20, "Электромеханик")

course_group = CourseGroup(student, [classmate1, classmate2, classmate3])

print(course_group)