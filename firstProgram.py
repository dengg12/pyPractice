#This program says hello and asks for my name
import sys

while(True):
    print('0, 1, 2,3 or exit')
    spam = input();
    if(spam == '0'):
        print('Hello World')
        print('What is your name?') #ask for name
        myName = input()
        print('It good to meet u, ' + myName)
        print('The length of your name is: ')
        print(len(myName))
        print('Wat u age')
        myAge=input()
        print('u age is: '+myAge)
        print('u will be ' + str(int(myAge)+1)+' in one year')
    elif(spam =='1'):
        while(True):
            print('1,2, or etc')
            spam1 = input()
            if(spam1 == '1'):
                print('Hello')
            elif(spam1 == '2'):
                print('Howdy')
            elif(spam1 == 'exit'):
                break
            else:
                print('Greetings')
                continue
    elif(spam=='2'):
        for i in range(10):
            print('counting in range(10) ' + str(i))
        for i in range(0,10):
            print('counting in range(0,10) ' + str(i))
        for i in range(0,10,1):
            print('counting in range(0,10,1) ' + str(i))
    elif(spam=='3'):
        print('this is for')
        for i in range(1,11): #for is not inclusive
            print(i)
        print('now while')
        x=1
        while(x<11):
            print(x)
            x+=1 #this is da wey to increment by 1
    elif(spam=='exit'):
        print('byebye')
        sys.exit()
    else:
        print('it is wat it is')
        continue

