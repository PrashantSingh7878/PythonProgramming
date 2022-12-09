import random
print('>>>>>>>>>>>>>>> LETS CHECK YOUR GENERAL KNOWLEDGE >>>>>>>>>>>>>>>')

un=input('Enter Your Name: ').lower()
print('')
print('Hi {}, You are only allowed to answer True and False.'.format(un))
print('No other input will be accepted')
score=0

que=['Delhi is the capital of India: ','India won the 2022 T20 world cup: ','V is the roman number indication of 4: ',
     'Minimum age required to vote is 15: ','There are 27 days in february: ','Electrical train is faster than electrical car: ',
     'Python is compiler language: ','alexa is a amazon product: ','17 is prime number: ','2 threes are 6: ',
     'India is a democratic  county: ','A banana a day keeps an doctor away: ','RGB stands for Red Blue Green: ',
     'The france is between spain and germany: ','17 means 5 in 24 hours notation clock: ','second hand of the clock is faster than minute hand: ',
     'cheetah is the fastest animal: ']
print('')

ans=['true','false','false','false','false','true','false','true','true','true','true','false','true','true','true','true','true']
while True:
    for i in range(5):
        a=random.randint(0,len(que)-1)
        sawal=que[a]
        print(sawal)
        jawab=input().lower()
        if jawab==ans[a]:
            print('Congrats! Correct Answer')
            print('>>[[ 1 point added ]]<<')
            score+=1
        else:
            print('''No, your answer is wrong :(''')
        print()
        print()
        del que[a]
        del ans[a]
    print('{} You Scored {}'.format(un,score))


    i=input('Do you want to play again???(y/n):').lower()
    print('************************************************************')
    print('')
    
    if i=='y':
        continue
    else:
        break
