# Program Name: HeathAdriannaFinalProject
# Author: Adrianna Heath
# Date: April 12, 2022
# Summary: A dice rolling game called Yahtzee
# Variables:
#   CLS: function to clear screen
#   AskYorN: Function asking user a yes or no question
#   GetNum: function to get a number from the user
#   Timer: Function to use as a timer for SPLASH function
#           c: count for timer (int)
#   SPLASH: function to display YAHTZEE on the screen
#   RollDie: function to get a random number
#           r: random number (int)
#   ShowInstructions: Displays yahtzee instructions
#   DisplayScore: Function to display a scorecard
#           score, total: keep track of users score and total score (int)
#   FirstRoll: Function that rolls the die
#   ShowDice: function using ASCII art to display dice
#   ReRoll: function that rerolls selected dice
#   AddUp: function that adds up the users score
#   ConfirmRoll: function that has user select category for
#                   where to put score on scorecard
#   GetBonus: function that finds if user gets a bonus roll
#   FinalScore: function that finds and displays users final
#               score
#   response: answers to questions through program (str)
#   dtops, dr1, dr2, dr3, dbots, d1t, d1, d1b, d2, d0: ASCII art for dice (str)
#   tline, mline, bline, title: ASCII art for scorecard (str)
#   final, upper, lower: used to define and add sections of scorecard
#   cats: tuple for categories on scorecard
#   all_dice: list to keep track of dice
#   
#===================IMPORTS======================
import time
import random

#==================FUNCTIONS=====================

# CLEARS THE SCREEN
def CLS(num):
    print("\n"*num)
    return

# ASKS A QUESTION
def AskYorN(question):
    """Ask a yes or no question."""
    response=None
    while response not in ("y", "n"):
        response=input(question).lower()
    return response

# GETS A NUMBER
def GetNum(question,low,high):
    """Ask for a number within a range."""
    response=None
    while response not in range(low, high):
        response=int(input(question))
    return response

# TIMER FOR SCREEN
def Timer(sec):
    c=0
    toc=time.perf_counter()
    while c<sec:
        tic=time.perf_counter()
        c=tic-toc

# DICE PICKS A NUMBER
def RollDie():
    r=random.randint(1,6)
    return r

# DISPLAY YAHTZEE INSTRUCTIONS FROM YAHTZEE WEBSITE
def ShowInstructions():
    CLS(33)
    print("""
Each player keeps his own score on a YAHTZEE score card to be marked with the player’s name. To determine who goes first, 
each player places all five dice in the dice cup and rolls out all the dice; the player with the highest total starts the game. The play 
then continues clockwise. 
Each player in turn places all five dice in the cup, shakes the cup and rolls out the dice. Each turn consists of a maximum of three 
rolls. The first roll must be made with all five dice. If the player chooses to roll a second and, if desired, a third time, he may pick 
up any or all the dice and roll again. It is the skillful use of these two optional rolls of the dice that can turn an unlucky first or 
second roll into a high-scoring turn. A score must be entered after the last roll in the appropriate box or a zero entered in a box of the 
player’s choice. 
SCORE CARD
Now let’s look at the YAHTZEE score card. You’ll note that there are 13 scoring boxes–aces, twos, threes, etc., through Large 
Straight, YAHTZEE and Chance. On each completed turn, the player must score in one of the 13 boxes. 
If on the first roll of the dice , a player has he might choose to go for “Twos” in the Upper Section of the 
score card or “3 of a kind” (in this case 2’s) in the Lower Section of the score card. The player would then leave the dice marked 
“2” on the table, pick up the 1, 3 and 6 dice and attempt to toss more 2’s on his second roll. 
If on the second roll of the dice, he has he might stop there and enter 6 in the “Twos” box in the Upper Section of the score card or 17 (total of all five dice) in the
“3 of a kind” box in the Lower Section. Or he might choose to roll again in the hope of getting one or even two more 2’s. 
If the player chooses to roll again, he picks up the 5 and 6 dice only and tosses for his third and last roll. If, on this third roll, he has 
he could enter his score as 6 in the “Twos” box in the Upper Section of the score card or 11 (total of all five dice) in the “3 of a kind” box in 
the Lower Section. The choice of when to take a score either after the first, second, or third roll of the dice and where to score (in the Upper 
Section of Lower Section of the score card) will be determined by the goal the player has set for himself. The choice of where to score can 
be made at any time after the first, second or third roll. On completion of each turn, the player marks the score in the appropriate box on his score card, or may enter
a zero in a box of his choice. 
For example, if after the third roll a player has and if the “Ones,” “Twos” and “Fours” boxes in the Upper Section and 
the “3 of a kind “ and “Chance” boxes in the Lower Section have been previously filled, the player must enter a zero in any open box. Only 
one blank box may be filled at the end of each turn. The boxes may be filled in any order, according to the player’s best judgment. 
The game is completed after each player has had 13 turns and has filled every box in the column with a score or an optional zero. The 
scores are then totalled and entered on the reverse side of score pad.
HOW TO SCORE 
It’s simple! The YAHTZEE score card is divided into 2 sections; 
the Upper and Lower.
UPPER SECTION 
In the Upper Section there are boxes to score “Aces,” “Twos,” “Threes,” “Fours”, “Fives” and “Sixes.” If a player chooses to score in the Upper 
Section, he counts and adds only the dice with the same number and enters the total of these dice in the appropriate box. If a player, on his 
turn, rolls and elects to take his score in the Upper Section, he would enter 9 in the “Threes” box. NOTE: a player may enter the total of ANY NUMBER of same value 
dice in the appropriate box in the Upper Section. For example, if a player, on his turn, rolls 
he may choose to score 2 in the “Aces” box. On the other hand, if a player, on his turn, rolls 
he may, if he wishes, score 12 in the “Threes” box.
BONUS 
To earn a bonus of 35 points, a player must score 63 points or more in the Upper Section. (For
quick calculation, 63 may be reached by scoring 3 “Aces,” “Twos,” and so on through “Sixes.”) A bonus can be obtained by having a total of 63 
points or more scored in any manner in the Upper Section 
LOWER SECTION 
The Lower Section of the score card is played exactly as indicated. The “3 of a kind” box may be filled in only if the dice show at least 3 of 
the same number. For example: would be scored 18 (total of all dice) in the “3 of a kind” box.
    """)

# DISPLAY YAHTZEE ON SCREEN ON A TIMER
def SPLASH(num):
    CLS(33)
    print("""

                                                                                                                                      
YYYYYYY       YYYYYYY               hhhhhhh                     tttt                                                                  
Y:::::Y       Y:::::Y               h:::::h                  ttt:::t                                                                  
Y:::::Y       Y:::::Y               h:::::h                  t:::::t                                                                  
Y::::::Y     Y::::::Y               h:::::h                  t:::::t                                                                  
YYY:::::Y   Y:::::YYYaaaaaaaaaaaaa   h::::h hhhhh      ttttttt:::::ttttttt    zzzzzzzzzzzzzzzzz    eeeeeeeeeeee       eeeeeeeeeeee    
   Y:::::Y Y:::::Y   a::::::::::::a  h::::hh:::::hhh   t:::::::::::::::::t    z:::::::::::::::z  ee::::::::::::ee   ee::::::::::::ee  
    Y:::::Y:::::Y    aaaaaaaaa:::::a h::::::::::::::hh t:::::::::::::::::t    z::::::::::::::z  e::::::eeeee:::::eee::::::eeeee:::::ee
     Y:::::::::Y              a::::a h:::::::hhh::::::htttttt:::::::tttttt    zzzzzzzz::::::z  e::::::e     e:::::e::::::e     e:::::e
      Y:::::::Y        aaaaaaa:::::a h::::::h   h::::::h     t:::::t                z::::::z   e:::::::eeeee::::::e:::::::eeeee::::::e
       Y:::::Y       aa::::::::::::a h:::::h     h:::::h     t:::::t               z::::::z    e:::::::::::::::::ee:::::::::::::::::e 
       Y:::::Y      a::::aaaa::::::a h:::::h     h:::::h     t:::::t              z::::::z     e::::::eeeeeeeeeee e::::::eeeeeeeeeee  
       Y:::::Y     a::::a    a:::::a h:::::h     h:::::h     t:::::t    tttttt   z::::::z      e:::::::e          e:::::::e           
       Y:::::Y     a::::a    a:::::a h:::::h     h:::::h     t::::::tttt:::::t  z::::::zzzzzzzze::::::::e         e::::::::e          
    YYYY:::::YYYY  a:::::aaaa::::::a h:::::h     h:::::h     tt::::::::::::::t z::::::::::::::z e::::::::eeeeeeee  e::::::::eeeeeeee  
    Y:::::::::::Y   a::::::::::aa:::ah:::::h     h:::::h       tt:::::::::::ttz:::::::::::::::z  ee:::::::::::::e   ee:::::::::::::e  
    YYYYYYYYYYYYY    aaaaaaaaaa  aaaahhhhhhh     hhhhhhh         ttttttttttt  zzzzzzzzzzzzzzzzz    eeeeeeeeeeeeee     eeeeeeeeeeeeee  
                                                                                                                                      
                                                                                                                                      
                                                                                                                                      

     """)
    Timer(5)
    CLS(33)


# DISPLAY A SCORECARD
def DisplayScore(c,score):
    # CLS(33)
    print("Score =",score)
    total=0
    for j in range(1,14):
        if score[j]<0:
            total+=0
        else:
            total+=score[j]
    score[0]=total
    print("\n\n                  Score Card      \n")
    print(tline)
    print(title)
    for a in range(1,14,1):
        #if s[a]==-1:
            #s[a]=0
        print(mline)
        if a>9:
             number=" "+str(a)+""
        else:
              number=" "+str(a)+" "
        if score[a]<10:
            scor=" "+str(score[a])+" "
        elif score[a]<100:
            scor=" "+str(score[a])+""
        else:
            scor=str(score[a])
        print(" ║ "+number+"   │   "+cats[a]+"    │     "+scor+"      ║ ")
    print(mline)
    if total<=99 and total>9:
        print(" ║       │   Total             │      "+str(total)+"      ║")
    elif total>99:
        print(" ║       │   Total             │      "+str(total)+"     ║")
    else:
        print(" ║       │   Total             │      "+str(total)+"       ║")
    print(bline)
    return score

# ROLLS 5 DIE
def FirstRoll():
    dice5=[]
    for a in range(5):
        dice5.append(RollDie())
    return dice5

# DISPLAY HORIZONTALLY
def ShowDice(dlist):
    row1=" "
    row2=" "
    row3=" "
    for a in dlist:
        if a == 1:
            p1=d0+" "
            p2=d1+" "
            p3=d0+" "
        elif a == 2:
            p1=d1t+" "
            p2=d0+" "
            p3=d1b+" "
        elif a == 3:
            p1=d1t+" "
            p2=d1+" "
            p3=d1b+" "
        elif a == 4:
            p1=d2+" "
            p2=d0+" "
            p3=d2+" "
        elif a == 5:
            p1=d2+" "
            p2=d1+" "
            p3=d2+" "
        else:    #It's a six
            p1=d2+" "
            p2=d2+" "
            p3=d2+" "
        row1+=p1
        row2+=p2
        row3+=p3

    print(dtops)
    print(row1)
    print(row2)
    print(row3)
    print(dbots)

# SELECT WHICH DICE USER WANTS TO ROLL AGAIN
def ReRoll(dlist):
    count=0
    for z in dlist:
        count+=1
        question="Die number "+str(count)+" is a "+str(z)+" do you want to reroll it? y/n "
        ans=AskYorN(question)
        if ans=="y":
            dlist[count-1]=RollDie()
    return dlist

def AddUp(n,dlist):
    tot=0
    for a in dlist:
        if a==n:
            tot+=n
    return tot
    

def ConfirmRoll(dice_list,score):
    used=True
    while used:
        question="Select the category to place this roll: (1-13) "
        c_num=GetNum(question, 1, 14)
        if score[c_num]!=0:
            used=True   # This means the category has already been used
        else:
            used=False  # This means the category has not been used yet
    if c_num==1:
        stotal=AddUp(1,dice_list)
        score[1]=stotal
    elif c_num==2:
        stotal=AddUp(2,dice_list)
        score[2]=stotal
    elif c_num==3:
        stotal=AddUp(3,dice_list)
        score[3]=stotal
    elif c_num==4:
        stotal=AddUp(4,dice_list)
        score[4]=stotal
    elif c_num==5:
        stotal=AddUp(5,dice_list)
        score[5]=stotal
    elif c_num==6:
        stotal=AddUp(6,dice_list)
        score[6]=stotal
    elif c_num==7:
        # 3 of a kind
        score[7]=sum(dice_list)
    elif c_num==8:
        # 4 of a kind
        if (dice_list[0]==dice_list[1] and dice_list[1]==dice_list[2] and dice_list[2]==dice_list[3])\
           or (dice_list[1]==dice_list[2] and dice_list[2]==dice_list[3] and dice_list[4]==dice_list[4]):
            score[8]=sum(dice_list)
    elif c_num==9:       # Full House
        if (dice_list[0]==dice_list[1] and dice_list[2]==dice_list[4])\
            or (dice_list[3]==dice_list[4] and dice_list[2]==dice_list[0]):
            score[9]=25
        else:
            score=0
    elif c_num==10:         # Small Straight
        score[10]=30
    elif c_num==11:
        score[11]=40
    elif c_num==12:
        # Yahtzee 5 of a kind
        if dice_list[0]==dice_list[1] and dice_list[1]==dice_list[2] and dice_list[2]==dice_list[3]\
           and dice_list[3]==dice_list[4]:
            score[12]=50
        else:
            score[12]=0   # no yahtzee
    else:
        score[13]=sum(dice_list)

def GetBonus(scard):
    upper=0
    for a in range(1,7):
        upper+=skore[a]
        if upper>62:
            B=35
        else:
            B=0
    return B


def FinalScore(end):
    CLS(33)
    final=0
    upper=0
    lower=0
    B=0
    for h in range(8,14):
        lower+=skore[h]
    for a in range(1,7):
        upper+=skore[a]
        if upper>62:
            final+=35
            B=35
        else:
            B=0
    for j in range(1,14):
        final+=skore[j]
    print(" ╔═════════════════════════════╤══════════════╗")
    if final<9:
        print(" ║ Total of both sections      │     ",final,"      ║")
    elif final>99:
        print(" ║ Total of both sections      │     ",final,"  ║")
    else:
        print(" ║ Total of both sections      │     ",final,"     ║")
    print(" ╟─────────────────────────────┼──────────────║")
    
    if upper<9:
        print(" ║ Total of upper section      │     ",upper,"      ║")
    elif upper>99:
        print(" ║ Total of upper section      │     ",upper,"  ║")
    else:
        print(" ║ Total of upper section      │     ",upper,"     ║")
    print(" ╟─────────────────────────────┼──────────────║")
    
    if B>0:
        print(" ║ 35 point bonus              │     ",B,"     ║")
    else:
        print(" ║ 35 point bonus              │     ",B,"      ║")
    print(" ╟─────────────────────────────┼──────────────║")
    
    if lower<9:
        print(" ║ Total of lower section      │     ",lower,"      ║")
    elif lower>99:
        print(" ║ Total of lower section      │     ",lower,"    ║")
    else:
        print(" ║ Total of lower section      │     ",lower,"     ║")
    print(" ╚═════════════════════════════╧══════════════╝")
        

    
# Main Program Function
def main(scorez):
    print("in main",scorez)
    SPLASH(1)
    ShowInstructions()
    input("Press enter to continue...")
    scorez=DisplayScore(cats,scorez)
    count=1
    while count<14:
        input("Continue...")
        all_dice=FirstRoll()
        print("The first roll is: ",all_dice)
        print("\nInitial Roll")
        ShowDice(all_dice)
        all_dice=ReRoll(all_dice)
        print("\nSecond Roll")
        ShowDice(all_dice)
        all_dice=ReRoll(all_dice)
        print("\nThird Roll")
        all_dice.sort()
        ShowDice(all_dice)
        print("in main",scorez)
        scorez=DisplayScore(cats,scorez)
        ConfirmRoll(all_dice,scorez)
        input("confirmed")
        scorez=DisplayScore(cats,scorez)
        GetBonus(scorez)
        count+=1
    FinalScore(scorez)

#=================DECLARATIONS===================
# Variables that need initialized
# A tuple of cetgory names
cats=("BB","Ones          ","Twos          ","Threes        ","Fours         ","Fives         ","Sixes         ","3 of a kind   ","4 of a kind   ",\
      "Full House    ","Small Straight","Large Straight","Yahtzee       ","Chance        ")

# A list of values for the score card
skore=[0,0,0,0,0,0,0,0,0,0,0,0,0,0]      # list of values for the scorecard

# Score card top line
tline= " ╔═══════╤═════════════════════╤══════════════╗"

# Score card middle line
mline= " ╟───────┼─────────────────────┼──────────────║"

# Score card bottom line
bline= " ╚═══════╧═════════════════════╧══════════════╝"

# Score card title line
title= " ║ Num   │      Category       │     Score    ║"

all_dice=[]

# Parts to display horizontally
dtops="  ┌───────┐   ┌───────┐   ┌───────┐   ┌───────┐   ┌───────┐ "
dr1=" "
dr2=" "
dr3=" "
dbots="  └───────┘   └───────┘   └───────┘   └───────┘   └───────┘ "
d1t=" │ o     │ "
d1 =" │   o   │ "
d1b=" │     o │ "
d2 =" │ o   o │ "
d0 =" │       │ "


# doube line chars ═ ║ ╔ ╗ ╚ ╝ ╠ ╣ ╦ ╩ ╬ 
# single line chars ─ │ ┌ ┐ └ ┘ ├ ┤ ┬ ┴ ┼
# mixed line chars ╟ ╢ ╤ ╧ ╨ ╫
#=================MAIN PROGRAM===================
CLS(33)
input("Press enter to begin...")
main(skore)
input("Finished...")



