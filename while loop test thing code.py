''' This is a quiz about Hunt of the wilderpeople ''' 
MAXSCORE = 9
points = 0
incorrect = 0
index = 0
# This list asks all the questions
questions_list = ["1. What nickname does Paula use to describe Ricky to Bella?\n\
                  A) Walking whale B) Tupac  C) A bad egg \n",
                 "2.What was the name of Rickys father figure \n"
                 "A) Hector B)  Josh  C)  Rick \n",
                 "3. What movie was referenced? \n"
                 "A) The Muppets B) lord of the rings C) Terminator\n",]
# This list has all the answer to see it you were right
answer_list = ["C", "A", "C"]

for question in questions_list:
     answer = input(question)
     answer = answer.upper()
     if answer == answer_list[index]:
          points = points + 1
          
     else: 
          incorrect = incorrect + 1
          
     index = index + 1
    

#tallys ups the correct and incorrect points
print(f'Correct {points}')
print(f'Incorrect {incorrect}')


