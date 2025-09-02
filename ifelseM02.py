# Gabriel Moore
# ifelseM02.py
# This program will accept students names (as a string) and GPA (as a float) and return if they can make the Dean's list or Honor Roll. If the entered first name is ZZZ, the program will terminate without any further processing

lastName = str(input("Enter student last name: "))
if lastName != "ZZZ" :
    firstName = str(input("Enter student first name: "))
    gpa = float(input("Enter student GPA as a decimal (e.g: 3.0): "))

    if gpa > 3.5 :
        print(firstName + " " + lastName + " Bis elegible for the Dean's List!")
    elif gpa > 3.25 :
        print(firstName + " " + lastName + " is elegible for the Honor Roll!")
    else :
        print(firstName + " " + lastName + " is not elligble for any lists")
        
        
# //////////////////////////////////////////////////////////

# TEST LOGS

# Enter student last name: Moore
# Enter student first name: Gabriel
# Enter student GPA as a decimal (e.g: 3.0): 3.45
# Gabriel Moore is elegible for the Honor Roll!

# Enter student last name: ZZZ
# (process ended)

# Enter student last name: Baker
# Enter student first name: Michael
# Enter student GPA as a decimal (e.g: 3.0): 3.6
# Michael Baker is elegible for the Dean's List!

# Enter student last name: Hudson
# Enter student first name: Cory
# Enter student GPA as a decimal (e.g: 3.0): 2.1
# Cory Hudson is not elligble for any lists