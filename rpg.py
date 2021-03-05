import time as t
print ('----------------------------------------------')
nickname = input('닉네임을 정하세요')
print ('----------------------------------------------')
worldlevel = 1
sword = ('wood')
money = 0



def start():
    global money
    print ('----------------------------------------------')
    print('rpg게임')
    print ('프로필: 1')
    print ('매뉴: 2')
    print ('----------------------------------------------')
    startanswer = input('무엇을 할지 숫자로 입력해 주세요')
    startanswer = int(startanswer)
    print ('----------------------------------------------')
    if startanswer == 1:
        profile()
    elif startanswer == 2:
        menu()
    else:
        print('다시입력해 주세요')

def profile():
    global money
    print ('----------------------------------------------')
    print ('{}님의 정보'.format(nickname))
    print ('칼:{}'.format(sword))
    print ('돈:{}'.format(money))
    profileanswer = input('나가고 싶으시다면 1을 입력하세요')
    profileanswer = int(profileanswer)
    print ('----------------------------------------------')
    if profileanswer == 1:
        start()

def menu():
    global money
    print ('----------------------------------------------')
    print ('월드 입장: 1')
    print ('상점: 2')
    print ('----------------------------------------------')
    menuanswer =  input('숫자를 입력해 원하는 곳으로 가세요')
    menuanswer = int(menuanswer)
    if menuanswer == 1:
        world()
    elif menuanswer == 2:
        store()

def world():
    global money
    print ('----------------------------------------------')
    worldanswer = input('레벨 입력')
    print ('----------------------------------------------')
    worldanswer = int(worldanswer)
    if worldanswer == 1:
        level1()
    elif worldanswer == 2:
        print('o')
    
        
def level1():
    global money
    goblin1lvhp = 50
    level1myHP = 100
    while goblin1lvhp > 0:
        print ('----------------------------------------------')
        print ('한마리의 약골 고블린이 있다')
        print ('공격:1')
        print ('수비:2')
        print ('도망:3')
        print ('----------------------------------------------')
        level1answer = int(input('무엇을 하시겠습니까?'))
        
        if level1answer == 1:
            goblin1lvhp = goblin1lvhp - (20)
            level1myHP -= (20)
            print ('----------------------------------------------')
            print ('고블린에게 20의 데미지 가 들어감.(남은 hp:{})'.format(goblin1lvhp))
            print ('읔 고블린이 나에게 20의 데미지를 입혔다....남은HP:{}'.format(level1myHP))
            print ('----------------------------------------------')
        elif level1answer == 2:
            print ('----------------------------------------------')
            print ('고블린이 나에게 20의 데미지를 주었지만 난 방어를 해서 0의 데미지를 입었다')
            print ('----------------------------------------------')
        elif level1answer == 3:
            print ('----------------------------------------------')
            print ('고블린이 날 잡고있어 도망치지 못한다...')
            print ('----------------------------------------------')
        else:
            print ('----------------------------------------------')
            print ('다시입력해 주십시오')
            print ('----------------------------------------------')


        if goblin1lvhp <= 0:
            print ('고블린이 힘없이 쓰러져 간다....')
            print ('1000원을 얻었다!')
            money += 1000
            print ('내돈{}'.format(money))
            t.sleep(5)
            start()
            
            


        
start()



