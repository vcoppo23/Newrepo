print ('Welcome to Rock-Paper-Scissors')
print ('type \'score\' to check score')
name = input("What's your name?: ")
r =  'r'
s =  's'
p =  'p'
pscore = 0
cscore = 0
pick = [ r , p , s]
lossmes = [ 'This is easy' , 'Are you even trying?','We can play go fish if this is to hard for you']
winmes = [ 'This game is rigged' , 'You\'re and idiot ' + name , 'screw you ' + name]
import random
def game():
    global pscore, cscore
    win = random.choice(winmes)
    lose = random.choice(lossmes)
    ran = random.choice(pick)
    player = input('Rock(r), Paper(p), or Scissors(s)?: ')
    if player == 'r' or 'p' or 's' or 'score':
        pass
    if player == 'score':
        print (name, '\'s score: ' , pscore, sep = '')
        print ('Computer\'s score:' , cscore)
        if cscore > pscore:
            print ('The Computer is winning!')
        elif pscore > cscore:
            print (name , 'is winning!')
        else:
            print ('It\'s a tie')
    else:
        if ran == r:
            print ('Rock!')
        elif ran == s:
            print ('Scissors!')
        elif ran == p:
            print ('Paper!')
    if player == r  and ran == s:
        print ("You Win")
        print (win)
        pscore = pscore + 1
    elif player == s  and ran == p:
        print ("You Win")
        print (win)
        pscore = pscore + 1
    elif player == p and ran == r:
        print ("You Win")
        print (win)
        pscore = pscore + 1
    elif player == s and ran == r:
        print ("You Lose")
        print (lose)
        cscore = cscore + 1
    elif player == p and ran == s:
        print ("You Lose")
        print (lose)
        cscore = cscore + 1
    elif player == r and ran == p:
        print ("You Lose")
        print (lose)
        cscore = cscore + 1
    elif player == ran:
        print ('Lets go again!')
game()
while True:
    game()




