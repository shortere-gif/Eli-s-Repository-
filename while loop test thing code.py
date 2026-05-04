''' This is a quiz about Hunt of the wilderpeople ''' 
int = maxscore = 9
int = Points = 0
int= incorrect = 0
hunt_list = []
# This part asks the question
question1 = input("What nickname does Paula use to describe Ricky to Bella?\n" \
                 "A) Walking whale B) Tupac  C) A bad egg \n"  )
# Adds a points a point to the correct score or wrong score
if question1 == 'C':
    Points += 1
else:
    incorrect += 1









#tally ups the correct and incorrect points
print(f'Correct answer {Points}')
print(f'Wrong answers {incorrect}')