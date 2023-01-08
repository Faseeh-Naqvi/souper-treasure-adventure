

def intro() :
    print('BOO!')
    print('Welcome to the super scary story ')
    print('you are a treasure hunter named...')
    print('sorry what is your name again?')
    name=input('Enter your name: ').capitalize()
    print('oh yea you\'re '+name+' I... I mean I allready knew that... ')
    print('.')
    print('.')
    print('.')
    print('Anyway so you are a young and daring treasure hunter named Scrooge McDuck...')
    isNameRight=''
    while not(isNameRight == 'Y' or isNameRight == 'N'):
        isNameRight=input('Right? (Y:yes N:no) : ').upper()
    if isNameRight == 'Y' : 
        name = 'Scrooge McDuck'
    if isNameRight == 'N' :
        print('')
        print('ughh fine you are no fun.')
        print('Anyway so you are a young and daring treasure hunter named',name)
        print('')
    print('You are on a mission to find a treasure in an abandoned facility but as you were making it inside you smelt something funny and fell asleep...')
    print('')
    wakeUp=input('Type W to wake up: ').upper()
    while not(wakeUp == 'W'):
        print('Ahem... you were not supposed to type that... please play along.')
        print('lets try that again then shall we?')
        wakeUp=input('Type W to wake up: ').upper()

def entrance():
    print('You wake up to find yourself sitting outside a seemingly abandoned facility.')
    print('')
    print('there are two doors.')
    print('A: A brown rudsted door')
    print('B: a shiny gold plated door with silver engravings. ')
    print('the engravings say something in spanish ~ la codicia será el veneno ~')
    print('under it in small writing it says "what is the Slovak term for soup?"')
    print('')
   
def normal_room() :
    print('you turn to see a beggar sitting in filth.')
    print('He asks you for money')
    print('A: Give him a coin')
    print('B: refuse his request')
    print('')   

def greedy_room() :
    print('there is a solid diamond totem. it  resembles a boy with its arms outstretched almost like it is begging. in its hand is a dusty soup bowl. There is an inscription under it in czech it says : ztracený totem')
    print('A: you put a coin into the totems soup bowl ')
    print('B: you try to steal the totem')
    print('C: you leave the totem and go into the door infront of you')
    print('')

def generous_altruist_ending():
    
    print('Give money to the beggar and he smiled.')
    print('There is a door that opens which leads you to the treasure.')
    print('')
    print('YOU SURVIVED')
    print('You got the generous altruist ending')
    print('YOU WIN')

def indifferent_miser_ending() :
    print('You don\'t give money to the beggar.')
    print('The beggar transforms into a monster; it sees how you were not greedy and gives you a merciful death.')
    print('YOU DIED')
    print('You got the indifferent miser ending')
    print('THE END')
    
def secret_acension_ending() :
    print('Reality starts to distort and shift around you.')
    print('You inhale a rush of air like you have just woken up from a horrible nightmare as you ascend dimensions.')
    print('Once you leave the third dimension you cannot return you are now a higher being. congratulations you have ascended.')
    print('You got the Secret Ascension ending.')
    print('THE END')

def greedy_altruist_ending_1():
    print('You can now leave the factory')
    closeDoor=''
    print('A: Close door')
    print('B: Leave door open')
    while not(closeDoor == 'A' or closeDoor == 'B') :
        closeDoor= input('Do you close the door on your way out ?: ').upper()
    if closeDoor =='A':
        print('You close it and the monster is now waiting for its next victim')
    else:
        print('You leave it open and you unleash the monster upon the world')
        print('THE END')

def abyss_ending():
    print('You grab the totem as the world crumbles around you and you are taken into an abyss never to be seen again.')
    print('You get the abyss ending.')
    print('THE END')

def greedy_genocide_ending():
    print(' You don\'t give money to the beggar') 
    print('you feel a deep sadness and rage churn inside you as the monster starts to envelop you.')
    print(' An incarnation of hate envelops your soul trapping it for all of eternity leaving you helpless as you watch it leave the factory walking in your skin.')
    print('You get the greedy genocide ending')
    print('THE END')
#this is where the program starts:
print('it is recomended to use google translate while playing this game for the full experience.')
print('')
intro()

entrance()

choiceDoor =''
while not (choiceDoor == 'A' or choiceDoor == 'B'):
    choiceDoor= input('Which door will you go through?: ').upper()
    print('')

if choiceDoor== 'A':
    print('')
    print('You enter a dusty room filed with cobwebs and rat droppings (eww)')
    normal_room()

    donateMoney = ''
    while  not(donateMoney == 'A' or donateMoney == 'B') :
        donateMoney=input('Give him money?: ').upper()
        print('')
    else:         
        if donateMoney == 'A' :
            generous_altruist_ending()
            closeDoor=''
            print('A: Close door')
            print('B: Leave door open')
            while not(closeDoor == 'A' or closeDoor == 'B') :
                closeDoor= input('Do you close the door on your way out ?: ').upper()
            if closeDoor =='A':
                print('You close it and the monster is now waiting for its next victim')
            else:
                print('You leave it open and you unleash the monster upon the world')
                print('THE END')
        elif donateMoney == 'B' :
            indifferent_miser_ending()
   


elif choiceDoor == 'B' :
    print('')
    print('You enter a gold plated room with diamond plated armchairs and a platnum floor it leads into two doors one says in a language you recognise as urdu لالچی مت بنو۔ یہاں سے گزرنا') 
    greedy_room()
    actionChoice=''
    while not(actionChoice == 'A' or actionChoice == 'B' or actionChoice == 'C'   ):
        actionChoice = input('What will you do ?: ').upper()
    if actionChoice == 'A' :
        print('You put a coin into the little boys hand and the eyes start to glow')
        wish = input( 'You are granted one wish what will it be?: ').capitalize()
        if wish == 'Polievka':
            secret_acension_ending()
        else:
            print('Your wish of', wish,'has been granted congratulations')
            greedy_altruist_ending_1()
    elif actionChoice =='B':
        abyss_ending()
    else:
        print('You leave the totem behind')
