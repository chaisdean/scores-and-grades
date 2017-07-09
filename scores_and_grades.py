# Assignment: Scores and Grades
# Write a function that generates ten scores between 60 and 100. Each time a score is generated, your function should display what the grade is for a particular score. Here is the grade table:

# Score: 60 - 69; Grade - D
# Score: 70 - 79; Grade - C
# Score: 80 - 89; Grade - B
# Score: 90 - 100; Grade - A

import random

def ten_scores():

    #print number
    for number in range(1,11):
        number = int(random.randint(60, 100))
        #print number
        if number >= 60 and number <= 69:
            print "Score: " + str(number) +"; Your grade is an 'D'"
        if number >=70 and number <= 79:
            print "Score: " + str(number) +"; your grade is an 'C' as in Chais"
        if number >=80 and number <= 89:
            print "Score: " + str(number) +"; your grade is an 'B' like Batman"
        if number >=90 and number <= 100:
            print "Score: " + str(number) + "; your grade is an 'A' for AWESOME!!!"
        #else:
             #print "Score: " + str(number) + "; you got a total 'F' bro!"

print ten_scores()
