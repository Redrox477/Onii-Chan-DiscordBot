# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 09:38:52 2020

@author: Monish kumar
"""


#oddoreven
def o_e():
    import random
    score1 = 0
    score2 = 0
    wicket1 = 1
    wicket2 = 1
    toss = input("\nenter your toss[heads/tails] : ")
    coin = ['heads', 'tails']
    result = random.choice(coin)
    ai = ['bat', 'bowl']
    comtoss = random.choice(ai)
    firstinnings = 1
    #firstininngs
    while firstinnings == 1:
        if toss == result:
            print("\nYOU HAVE WON THE TOSS...:)")
            dec = input("\nCHOOSE YOUR DECISION[bat/bowl]? ")
            if dec == 'bat':
                comtoss = 'bowl'
                while wicket1 == 1:
                    bat = int(input("\nenter your bating.... : "))
                    bow = random.randint(1, 6)
                    print('\nbatting =', bat, '::', bow, '= bowling')
                    if bat == bow:
                        print("\noops...you are OUT!!")
                        wicket1 -= 1
                        print("\nfirst innings over....",
                              "\nyour total score:", score1)
                        firstinnings -= 1
                    else:
                        score1 += bat
                        print("\nscore as of now...", score1)
            elif dec == 'bowl':
                comtoss = 'bat'
                while wicket1 == 1:
                    bow = int(input("\nenter your bowling... : "))
                    bat = random.randint(1, 6)
                    print('\nbatting =', bat, '::', bow, '= bowling')
                    if bat == bow:
                        print("\ngreat !!..you bowled him out..")
                        wicket1 -= 1
                        print("\nfirst innings over....",
                              "\nyour opponent total score:", score1)
                        firstinnings -= 1
                    else:
                        score1 += bat
                        print('\nscore as of now....', score1)

        else:
            print("\nYOU HAVE LOSE THE TOSS ...better luck next time....!")
            print("\nthe oppenent has chosen to", comtoss, "first")
            if comtoss == 'bat':
                dec = 'bowl'
                while wicket1 == 1:
                    bow = int(input("\nenter your bowling.... : "))
                    bat = random.randint(1, 6)
                    print('\nbatting =', bat, '::', bow, '= bowling')
                    if bat == bow:
                        print("\ngreat !!..you bowled him out..")
                        wicket1 -= 1
                        print("\nfirst innings over....",
                              "\nyour opponent total score:", score1)
                        firstinnings -= 1
                    else:
                        score1 += bat
                        print('\nscore as of now.....', score1)
            elif comtoss == 'bowl':
                dec = 'bat'
                while wicket1 == 1:
                    bat = int(input("\nenter your batting... : "))
                    bow = random.randint(1, 6)
                    print('\nbatting =', bat, '::', bow, '= bowling')
                    if bat == bow:
                        print("\noops...you are OUT!!")
                        wicket1 -= 1
                        print("\nfirst innings over....",
                              "\nyour total score:", score1)
                        firstinnings -= 1
                    else:
                        score1 += bat
                        print('\nscore as of now.....', score1)
    #secondinnings
    print('\n********second innigs starts now********')
    secondinnings = 1
    while secondinnings == 1:
        if dec == 'bat' and comtoss == 'bowl':
            while wicket2 == 1:
                bow = int(input("\nenter your bowling... : "))
                bat = random.randint(1, 6)
                print('\nbatting =', bat, '::', bow, '= bowling')
                if bat == bow:
                    print("\ngreat !!..you bowled him out..")
                    wicket2 -= 1
                    print("\nsecond innings over....",
                          "\nyour opponent total score:", score2)
                    secondinnings -= 1
                    if score2 == score1:
                        print("\nMATCH IS TIED...LOL!!")
                        break
                    else:
                        print("\n YOU HAVE WON THE MATCH WOOOHOOO...")
                        break
                else:
                    score2 += bat
                    print('\nscore as of now....', score2)
                    if score2 > score1:
                        secondinnings -= 1
                        print("\nYOU HAVE LOST THE MATCH")
                        break
                    else:
                        continue
        else:
            while wicket2 == 1:
                bat = int(input("\nenter your bating.... : "))
                bow = random.randint(1, 6)
                print('\nbatting =', bat, '::', bow, '= bowling')
                if bat == bow:
                    print("\noops...you are OUT!!")
                    wicket2 -= 1
                    print("\nsecond  innings over....", "\nyour total score:",
                          score2)
                    secondinnings -= 1
                    if score2 == score1:
                        print("\nMATCH IS TIED...LOL!!")
                        break
                    else:
                        print("\n YOU HAVE lost THE MATCH alas....")
                        break
                else:
                    score2 += bat
                    print("\nscore as of now...", score2)
                    if score2 > score1:
                        secondinnings -= 1
                        print("\nYOU HAVE WON THE MATCH")
                        break
                    else:
                        continue
