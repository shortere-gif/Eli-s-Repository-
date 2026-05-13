''' This is a quiz about Hunt of the wilderpeople ''' 
MAXSCORE = 9
points = 0
incorrect = 0
index = 0
index_1 = 0
print("Hunt of the wilderpeople quiz\n")
important_list = ["A","B","C"] # type: ignore
# This list has all the answer to see it you were right
answer_list = ["C","A","C","A","B","C","B","B","A"]
# This adds a point to if you got it correct wrong and changes the question.
questions_list = [
"1. What nickname does Paula use to describe Ricky to Bella? \n" 
"A) Walking whale\n"
"B) Tupac\n"
"C) A bad egg \n",

"2. What was the name of Rickys father figure? \n"
"A) Hector\n"
"B) Josh\n"
"C) Rick \n",

"3. What movie was referenced? \n"
"A) The Muppets\n" 
"B) lord of the rings\n"
"C) Terminator\n",

"4. What was the name of the child welfare officer searching for Ricky?\n"
"A) Paula Hall\n"
"B) Paul Blart\n"
"C) Paula Smith\n",

"5. Who is Psycho Sam?\n"
"A) A Psycho who was kicked out of town into the woods\n"
"B) A conspiracy theorist living alone in the bush who helps Ricky and Hec\n"
"C)A man who has a nickname of Psycho Sam\n",

"6. What injury does Hec sustain, which forces him to stop running?\n"
"A) Stabbed in the chest by a boar\n"
"B) Cut his leg open on a brunch\n"
"C) breaks his foot during their time in the bush\n",

"7. What is the Hunt for the Wilderpeople based on?\n"
"A) The movie is based on the book A good keen man by Barry Crump\n"
"B) The movie is based on the book Wild Pork and Watercress by Barry Crump\n"
"C) The movie is based on Harry Hobnail and the Pungapeople by Barry Crump\n",

"8. What does Ricky Baker love to write to help him express his feelings?\n"
"A) Ricky writes sudoku\n"
"B) Ricky plays haikus\n"
"C) Ricky shoots birds\n",

"9. Who directed the film?\n"
"A) The film is directed by Taika Waititi\n"
"B) The film is directed by Te Whanau a Apanui\n"
"C) The film is directed by Te Atarangi Amoroa\n",
]
while True:
     for question in questions_list: # type: ignore
        answer = input(question)
        answer = answer.upper()
        if answer == important_list[index_1]: 
          answer = True
          break
          answer == False
        else:
           print('That answer is invalid')
        if answer == answer_list[index]:
          points = points + 1  
        else: 
          incorrect = incorrect + 1
          index = index + 1
          break
     



#tallys ups the correct and incorrect points
print(f'Correct {points}')
print(f'Incorrect {incorrect}')