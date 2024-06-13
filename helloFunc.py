#! /usr/bin/python3

import random

def hello():
    print('HOWDY')
    print('ITS FUCKING JOEVER')

def hello(name):
    print('testing overloading '+name)
    return len(name)

def getAnswer(answerNumber):
    if answerNumber==1:
        return 'its a 1'
    elif answerNumber==2:
        return 'its a 2'
    elif answerNumber==3:
        return 'its a 3'
    elif answerNumber==4:
        return 'its a 4'
    else:
        return 'testing general capture, ans is ' + str(answerNumber)


def simRand():
    r = random.randint(1,9)
    fortune = getAnswer(r)
    print(fortune)

def divideTest(num):
    try:
        return 42/num
    except ZeroDivisionError:
        print('u tried to div by zero u retard')

def collatz(num):
    try:
        if(num%2==0): #if even
            print(num//2)
            return num//2
        elif(num%2==1): #if odd
            print(3*num+1)
            return 3*num+1
    except ZeroDivisionError:
        print('do i even need this')
    

def col(num):
    try:
        num = int(num)#checks if int. goes straight to ValueError
        while(num != 1):
            num = collatz(num)
    except NameError:
        print('not an int')
    except TypeError: #skipped bc of int()
        print('WRONG TYPE')
    except ValueError:
        print('NOT AN INTTTTTTTTT')
        
def catNamer():
    catNames = []
    while True:
        print('Enter the name of cat ' + str(len(catNames) + 1) + ' (Or enter nothing to stop.):')
        name = input()
        if name == '':
            break
        catNames = catNames + [name] # list concatenation
    print('The cat names are:')
    for name in catNames:
        print(' ' + name)

def learnlist():
    testlist = ['hi', 1,2,3,4,['test',1.1,1.2,1.0]]
    print(testlist)
    if 'test' in testlist:
        print('its in there alright')
    elif 'test' in testlist[5]:
        print('guess it doesnt peek inside nested lists')#"in" does NOT peek inside nested lists.
    elif 'hi' in testlist:
        print('hi is in it')
    else:
        print('didnt work')
    myPets = ['Zophie', 'Pooka', 'Fat-tail']
    testOrNaw = False
    while(testOrNaw):#turned this off
        print(myPets)
        print('Enter a pet name:')
        name = input()
        if name not in myPets:
            print('I do not have a pet named ' + name)
        else:
            print(name + ' is my pet.')
        if name == 'exit':
            break
    #multiple assignment
    first,second,third=myPets
    print(first,second,third,'testingMultAss')
    print('myPets is: ',myPets)
    myPets+='newPet' #interesting. each char was added one at a time as its own item.
    print('ADDED ONE MORE. myPets is: ',myPets)
    newPetItem='Timmy the Racist'#I tried adding a number instead but was not interable. 
    #myPets= myPets+newPetItem#cant add a string either.
    myPets.append(newPetItem)
    print('ADDED TIMMY. myPets is: ',myPets)
    myPets.insert(1,'newInsertat1')
    print('newItemat1. myPets is: ',myPets)
    myPets.remove('Zophie')
    print('testing removal of Zophie',myPets)

    print()
    caseSort = ['b','B','A','a','c','C','A','a1','A2']
    print(caseSort)
    caseSort.sort(key=str.lower)#print only prints the return val
    print(caseSort)

def magic8():
    messages = ['It is certain',
        'It is decidedly so',
        'Yes definitely',
        'Reply hazy try again',
        'Ask again later',
        'Concentrate and ask again',
        'My reply is no',
        'Outlook not so good',
        'Very doubtful']
    print(messages[random.randint(0,len(messages)-1)])#random int between 0 and the length of the list which is -1 because 0 based
    print('loooooooooooooooooooooooooooooooooooooooooooooong'+ \
          'testing the backslacsh')
    testVar = messages[0]
    print('testVar is',testVar)
    messages[0] = 'newVal'
    print('does it have a ref or a copy',testVar)
    print('watabout the list',messages)
    
def commaCode(listvar):
    product = ''
    count = 0
    for i in listvar:

        product+=str(i) #force string
        if len(listvar)==1:
            break #check if list only has one element
        product+=', '
        count+=1
        if len(listvar)-1 == count: #if second to last item, add "and"
            product+='and '
            product+=str(listvar[-1])
            break
    return product # string with items sep by comma space and AND
                    #a,b,c,d becomes "a, b, c, and d"
#Summary: Forces a string so you can add ints.
#Checks if there's only one element. Breaks if so.
#extra extra credit would be to neglect comma if only two elements.
#we are not checking nested lists.

def CharPicGrid():
    grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]#want to turn it 90 degrees clockwise.
   #grid has 9 items. Each item has 6 more items.
    
    for x in range(0,len(grid[0])): #0-5. first nested item of each shell
        #first loop matches the X of the final product
        for y in range(0,len(grid)): #0-8

            print(grid[y][x], end='')#coordinates of source
        print()
            
def bday():
    birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}
    print(birthdays)
    while True:
        print('Enter a name: (exit to quit)')
        name = input()
        if name == 'exit':
            break
        if name in birthdays:
            print(birthdays[name] + ' is the birthday of ' + name)
        else:
            print('I do not have birthday information for ' + name)
            print('What is their birthday?')
            bday = input()
            birthdays[name] = bday
            print('Birthday database updated.')

import pprint

def dIC():
    spam = {'color': 'red', 'age': 42}
    for k, v in spam.items(): #items() returns two 'items' before each comma
        print('Key: ' + k + ' Value: ' + str(v))
    if('color' in spam.keys()):
        print('color is in')
    if(42 in spam):
        print('42 is in')#seems to by default check keys and not values. 

    picnicItems = {'apples': 5, 'cups': 2}#use of get() can peek without indexEr
    print('I am bringing ' + str(picnicItems.get('cups', 0)) + ' cups.')
    print('I am bringing ' + str(picnicItems.get('eggs', 0)) + ' eggs.')
#character counter
    message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
    count = {}
    for character in message:
        count.setdefault(character, 0)#first time,set to 0. if exist do nothing
        count[character] = count[character] + 1#always increment. guarantee to exist
    pprint.pprint(count)



def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
def playT():
    theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}#8 configs to win
    turn = 'X'
    for i in range(9):
        printBoard(theBoard)
        print('Turn for ' + turn + '. Move on which space?')
        move = input()
        theBoard[move] = turn
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'
    printBoard(theBoard)

pi2={'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
def di(inv):
    #take a dictionary and display all key-val
    print('Inventory:')
    invCount=0

    for k,v in inv.items():
        print(v,k)
        invCount+=v
    print('Total number of items: ',invCount)

dra = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
def add2(inv,addedItems):
    #inv parameter is dictionary, addedItems is list to add. return a dic
    for i in addedItems:
        inv.setdefault(i,0)
        inv[i]+=1
    return inv
    """multiline comments here
adsfad
dfd
sdf"""
def printPicnic(itemsDict, leftWidth, rightWidth):
    print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-'))
    for k, v in itemsDict.items():
        print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))
    
picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}
printPicnic(picnicItems, 12, 5)
printPicnic(picnicItems, 20, 6)
#import pyperclip
GLOBAL_num_pets = 0 

class Pet(object):

 
    def __init__(self, name):
        self.name = name
        global GLOBAL_num_pets
        GLOBAL_num_pets+=1
        self.num_pets = GLOBAL_num_pets
 
    def speak(self):
        print("My name's %s and the number of pets is %d" % (self.name, self.num_pets))

rover = Pet("rover")
spot = Pet("spot")
 
rover.speak()
spot.speak()

#Q1: Write a function that reverses each word in a string.
#Input:  hello world out there.       Output:  there. out world hello

def reverse(inputString):
    print('Input string is: ', inputString)
    listOfstrings = inputString.split() #default splits on spaces ' '
    for i in range(len(listOfstrings)-1,-1,-1):
        print(listOfstrings[i], end = ' ')
        ###for j in range(len(listOfstrings[i])-1,-1,-1):
       #     print(listOfstrings[i][j],end='')
       # print(' ',end='')

reverse('hello world out there.')
#Q2:  Write a function that implements the Linux "tail" command.
#The tail command basically prints out the last 10 lines in a file by default.


def tailfunc(fileName):
    file = open(fileName)
    listOflines = file.readlines()
    tailLen = len(listOflines) #len is not index based because you cant have a
    #file with "0 lines" when it has 1 line.
    print('length of lines of file: ',fileName,' is: ',tailLen)
    for i in range(tailLen - 11 if tailLen > 10 else 0, tailLen,1):
        print(i,listOflines[i], end = '')
#tailfunc('interviewQuestions (1).txt')
tailfunc('test.txt')
