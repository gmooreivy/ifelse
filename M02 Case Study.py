# Gabriel Moore
# ifelseM02.py
# This program will accept students names (as a string) and GPA (as a float) and return if they can make the Dean's list or Honor Roll. If the entered first name is ZZZ, the program will terminate without any further processing
while True :
    lastName = str(input("Enter student last name: "))
    if lastName == 'ZZZ' :
        break
    firstName = str(input("Enter student first name: "))
    gpa = float(input("Enter student GPA as a decimal (e.g: 3.0): "))

    if gpa >= 3.5 :
        print(firstName + " " + lastName + " is elegible for the Dean's List!")
    elif gpa >= 3.25 :
        print(firstName + " " + lastName + " is elegible for the Honor Roll!")
    else :
        print(firstName + " " + lastName + " is not elligble for any lists")   
        
# //////////////////////////////////////////////////////////

# TEST LOGS

"""

Enter student last name: Moore 
Enter student first name: Gabriel
Enter student GPA as a decimal (e.g: 3.0): 3.4
Gabriel Moore  is elegible for the Honor Roll!
Enter student last name: Baker
Enter student first name: Michael
Enter student GPA as a decimal (e.g: 3.0): 3.5
Michael Baker is elegible for the Dean's List!
Enter student last name: Privett
Enter student first name: Aiden
Enter student GPA as a decimal (e.g: 3.0): 3.0
Aiden Privett is not elligble for any lists
Enter student last name: Schorey
Enter student first name: Paul
Enter student GPA as a decimal (e.g: 3.0): 3.25
Paul Schorey is elegible for the Honor Roll!
Enter student last name: Tillman
Enter student first name: Landen
Enter student GPA as a decimal (e.g: 3.0): 3.5
Paul Schorey is elegible for the Dean's List!
Enter student last name: ZZZ
(end of process)

"""