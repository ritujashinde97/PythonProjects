import random
from time import sleep

print(input("Storyname:"))
mainChar = input("Main Character :")
rivalChar = input("Rival :")
activity = input("Daily activity (eg. Netflix and Chill) :")
posAdj = input("Positive adjective (eg. Funny / Happy ) :")
negAdj = input("Negative adjective (eg. Lazy / Sad) :")

word1 = ['question', 'answer', 'comment']
word2 = ['protected', 'war','amazing victory', 'Celebration']
word3 = ['ramayan', 'helpful' , 'brother', 'bow and arrow']
word4 = ['liked', 'disliked', 'happy', 'freedom', 'destruction']

sentence = ['Once upon a time', 'mainChar' , 'was born in Ayoddhya', '.\n','He had to', 'fight with', 'rivalChar','.',
            'mainChar', 'tried to sort the matter', 'but', 'rivalChar' ,'was' ,'negAdj', '.\n','mainChar', 'word2','Sita',
            '.\n','Lakshman was ', 'mainChar','word3', 'It led huge', 'word4', '.\n','word3', 'happened', '.\n','it was', 'word2','.\n' ]

for item in sentence :
    if item == "activity": sentence[sentence.index(item)] = activity
    elif item == "mainChar": sentence[sentence.index(item)] = mainChar
    elif item == "rivalChar": sentence[sentence.index(item)] = rivalChar
    elif item == "posAdj": sentence[sentence.index(item)] = posAdj
    elif item == "negAdj": sentence[sentence.index(item)] = negAdj
    elif item == "word1": sentence[sentence.index(item)] = random.choice(word1)
    elif item == "word2": sentence[sentence.index(item)] = random.choice(word2)
    elif item == "word3": sentence[sentence.index(item)] = random.choice(word3)
    elif item == "word4": sentence[sentence.index(item)] = random.choice(word4)
    else: continue

#story
story = " ".join(item for item in sentence)
print("\n Story is generating... \n")
sleep(1)
print(story)

