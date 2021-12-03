
import sys

info = {}
with open("{}".format(sys.argv[1]),"r",encoding="utf-8") as file:
    for student_info in file:
        name = student_info.split(":")[0]
        info[name] = (student_info.split(":")[1]).split(",")
    for input in sys.argv[2].split(","):
        try:
            university = info[input][0]
            department = info[input][1]
            print("Name: {}\nUniversity:{}\nDepartment:{}".format(input,university,department))
        except KeyError:
            print("No info has found for {}!!".format(input))


