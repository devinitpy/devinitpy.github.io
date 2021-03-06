'''
Assement Test 1
    Each qn carries  10 marks, bonus qn carries 20 marks, Passmark is 50%
    Given a list containing dictionaries of students
    write  functions that interacts with the data as stated in the comments
'''
from operator import itemgetter, attrgetter


data = [{"name":"nelson","marks":70},
        {"name":"getrude","marks":85},
        {"name":"hana","marks":65},
        {"name":"emma","marks":55},
        {"name":"richard","marks":60},
        {"name":"sophie","marks": 90}]

#Qn1 . function that returns students average score

# dictionary_var = {"name":"nelson","marks":70}
# mark = dictionary_var.get("marks",0)
# mark = dictionary_var["marks"]
def student_data(data_in,attr):
    value_list = []
    for obj in data_in:
        value_list.append(obj[attr])
    return value_list

def summation(score_list):
    total = sum(score_list)
    average = total/len(score_list)
    print average

scores =student_data(data,"marks")
summation(scores)



# Qn 2. function that returns a list of all the student names sorted in ascending order
names = student_data(data,"name")
sorted_names = names.sort()
#Qn3 . write a function that returns a students grade
#i.e grade = grading_function(data[0])


def marks_grade(score):
    if score >= 80:
        grade = 5
    elif score >=70 and score < 80:
        grade = 4
    elif score >= 60 and score < 70:
        grade = 3
    elif score >= 50 and score <60:
        grade = 2
    elif score >=40 and score <50:
        grade  = 1
    else:
        grade = 0
    return grade

def grading_function(obj):
    raw_grade = marks_grade(obj["marks"])
    grades_list=["F","O","D","C","B","A"]
    my_grade = grades_list[raw_grade]
    return my_grade

student_grade=grading_function(data[0])
print student_grade

#Q4 write a function that adds to each student dictionary / object a grade attribute i.e data[0]={"name":"allan","marks": 70 , "grade": "B"}


def grade_attribute(data_in):
    for obj in data_in:
        obj["grade"] = grading_function(obj)
    print data_in

grade_attribute(data)

#Bonus Question 5: sort the data list by student marks and return student with highest score
#hint https://wiki.python.org/moin/HowTo/Sorting

def sort_objs(data_in,attr):
    new_list = sorted(data_in, key=itemgetter(attr),reverse=True)
    print new_list
    return new_list[0]

sort_objs(data,"marks")
