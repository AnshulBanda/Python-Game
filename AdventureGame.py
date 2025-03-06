import time
import sys
import random
health=100


def dprint(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.005)

damage_val = {"axe":10,"sword":7,"bow and arrow":12,"Shield":0,"Explosive":20,"fire":30,"ice":30,"explosion":50}
def villain(health_villain,damage_range):
    health_villain = health_villain
    health_chr = health
    while (health_villain > 0 and health_chr>0):
        wep = input(f"Enter the weapon you need to use {inventory}: ")
        if(wep in inventory):
            health_villain = health_villain- damage_val[wep]
            damage = random.randint(1,damage_range) 
            health_chr = health_chr - damage
            dprint(f"Stats: Your Health:{health_chr} Enemy Health:{health_villain} Damage:{damage}")
        else:
             dprint("Weapon not in inventory")
    if(health_villain <= 0 and health_chr>0):
           status = 0  
           dprint("Enemy Defeated,Your health is restored to 100")
           status = 0
    elif(health_chr<=0 and health_villain>0):
            status = 0  
            dprint("You are dead")
            input()
            dprint('Game Over')
            exit()
            status = 1
    return status  
dprint("You awaken to the gentle warmth of sunlight streaming through your window, casting a golden hue across the room. The familiar creaks of your humble abode welcome you back to the conscious world. It's a new day in the mystical land of (name of place), and the choices you make will shape the destiny that awaits.")
input()
print()
dprint("You slowly rise from your comfortable haven, shaking off the remnants of dreams. The air is charged with anticipation, and a sense of adventure beckons you forward.")
print()
input()
dprint("Your mother calls out your name , it seems as if the vegetables have run out ...... it's time for you to run some errands")
input()
print()
dprint("The scorching heat makes you feel as if you will melt on spot , however you stay determined and keep moving on")
input()
print()
dprint("You finally arrive at an old marketplace , it's been a while since you last arrived ,but the place has always been reliable for buying your essentials")
input()
print()
dprint("Suddenly! You see an old man fall down , help him get back up ? : " )
if(input() =="yes"):
 print()
 dprint('Thank You young man ,if only there were more people like you in this world')
 input()
 print()
 dprint("Alas!There are of few things an old, broke man can do to repay your favour, however i can tell you a secret of mine")
 input()
 print()
 dprint("Beyond this place behind a mountain lies a cave,which is rumored to have several treasures hidden in its lands...it is certianly a place for younings like you to adventure about")
 input()
 print()
 dprint("The old man walks away in solitude")
 input()
 print()
 dprint('You have Two choices now, either follow what the old man said or simply ignore it : ')
 if(input()=="follow"):
    print()
    dprint("You decide to follow the old man's words , but in order to go on an adventure you must buy some items")
    input()
    print()
    money=random.randint(1000,5000)
    print(f"You look around the marketplace , you have about {money}(currency)")
    print()
    print("total money available:",money)
    inventory={}
    market_weapon={'sword':1000,'shield':1500,'bow and arrow':750,'axe':1500,'explosive':2500}
    print("These are the weapons available in market:")
    print(market_weapon)
    market_magic={'fire':1000,'ice':1000,'heal':500,'explosion':3500}
    print("These are the magic available in market:")
    print(market_magic)
    while True:
     command=input("What do  you want to buy from market? :")
     if command=="weapon":
        key=input("enter which weapon you want:")
        if key in market_weapon:
            if key in inventory:
               print("cant buy again")
               print("inventory",inventory)
            elif key not in inventory:
                value=market_weapon[key]
                if money<value:
                    print("not enough money")
                else:
                    rem=money-value
                    money=rem
                    print("the money remaining is:",money)
                    inventory[key]=value
                    print("inventory",inventory)
     elif command=="magic":
        key=input("enter which magic you want:")
        if key in market_magic :
            if key in inventory:
               print("cant buy again")
               print("inventory",inventory)
            elif key not in inventory:
                value=market_magic[key]
                if money<value:
                    print("not enough money")
                else:
                    rem=money-value
                    money=rem
                    print("the money remaining is:",money)
                    inventory[key]=value
                    print("inventory",inventory)

     elif command=="nothing" or "I'm done":
         def enemy1():
            dprint("As you near the entrance of the cave, you think about the journey you are about to embark on, the risk you are about to take,")
            dprint("the pain you will experience. You wonder if you would be considered a coward for turning around and backing away.")
            dprint("You reach the entrance of the cave. You have one chance to turn back if you wish to, its now or never")
            Ans=input("turn back or continue? : ")
            if (Ans=="turn back"):
                dprint("You turn back and run away from the cave, fearing you would lose your life. You choose to live the life of a coward than to not live at all")
                dprint("GAME END")
                exit()
            elif (Ans=="continue"):
                dprint("you continue on into the cave. The darkness and cold atmosphere of the cave sends chills down your spine. you light a torch to use to\n"
                    "guide your way.")
                dprint("As you continue, you hear a sound......squeaking. It sounds like a small animal moving around in the dark. You think to yourself")
                dprint(" 'it must be a small mouse. Cant let a small animal like that scare me otherwise i wouldnt survive here'")
                dprint("You soldier on. As you walk on the squeaking sounds grows stronger. 'Multiple mice??? it must be' you tell yourself. You continue on until\n"
                    "something falls right before your eyes. look bend down to examine it, it looks like....... feces? you look up to figure out where it came\n"
                    "from and thats when you notice them. BATS!!!!!!!!! A WHOLE NEST OF THEM!!\n"
                    "They let out a loud screech, before taking flight to attack. Who are they attacking? YOU!!\n!"
                    "Its time to do or die for you")
                Ans1=input("what will you do? run or fight : ")
                if (Ans1=="run"):
                        dprint("you make a run for it. throught the darkness of the cave, you try to navigate your way to safety. As you run, your leg hits a rock\n"
                            "and you trip over. you look behind you to see how far the bats. You turn around and then you see a bat 10cms away from your face.\n"
                            "they attack your body, ripping of your flesh from the bones. its over for you as you get swarmed by bats and get eaten alive")
                        dprint("GAME END")
                        exit()  
                elif (Ans1=="fight"):
                        print("you decide to make your stand. its only your first enemy, you must fight them.")
                        status = villain(25,5)
                return status

         def enemy2():
            dprint("Atter fighting the bats, you realise the bats are the first of many foes you will face in the cave. \n"
            "you feel shivers go down your spine but at the same time you feel a sense of excitment. to continue deeper into the cave/n"
            "and fight more enemies, all for that treasure.")
            dprint("You continue into the cave. you keep wwalking for a while until you start the feel the ground shaking. Earthquake? that can't be right \n"
                "its too weak to be an earthquake. it has to be something else, something big. you continue with caution. what could it be? a rolling or\n"
                "falling rock? no it would have stopped by now. this is something that is constantly moving, but what could it be? you keep walking until you\n"
                "reach an open area. you look around and you see it. the cause of the commotion. GIANT CRABS!!!!!!\n")
            dprint("You try to walk around them but oh no!! they notice you. they yell out and the start charging at you at incredible speeds")
            dprint("Its time to fight")


            
            villain(50,15)
            return status


         def enemy3():
            dprint("As you continue ahead you hear several footsteps and prepare for another combat,you are startled by 2 dogs that stand in front of you.\n"
                "You close your eyes and open them to refocus as you see an entire army of dogs and behind it seems like their leader The Undead Warrior.")
            dprint("The Undead Warrior raises his sword and points it towards you ,before you realise the army of dogs are flooding towards you")
            status=villain(50,25)
            return status


         def enemy4():
            dprint("You are terribly exhausted after that battle you rest lying down on the ground you open the bag and use the bandages you have left in it.\n"
                "You regret not fighting more carefully as some of those bites by the dogs might get worse .Your mouth feels dry and you are desperate for some water to quench your thirst.")
            dprint("After a few hours you pick up your bag and have some food and continue into the cave , it is only then you realise that you have come too far to now go back and forget about the treasure./n"
                "You remember about all the things you have been through and continue ahead not ready to look back .")
            dprint("You hear the falling of water and suddenly your body is completely energized as you run towards the sound of water. The falling of water becomes louder as you move forward .\n"
                "You can start seeing a cliff from which where the water is falling from , you fall to the ground and start drinking the water with the palm of your hands.Then suddenly you hear the sound of someone walking you raise your head to see a man in black robe standing on top of the cliff a chain bearing a skull as an ornament. ")
            print("Looking at the mage a shiver runs down your spine as you stand up and look at him the mage unveils his hood and uncovers his frightening half dead face . ")
            print("You start speaking \"I am here for the treasure,do you know where it is ?\" You can see the fire in the mage's eye as he declares \"OVER MY DEAD BODY! \".\n"
                "You wonder if he realises the irony of what he had just said but you hold that train of thoughts as you see him jumping down the cliff and ready to engage in yet another battle .")
            status=villain(50,15)
            return status


         def enemy5():
            dprint("you end the underground palace. everywhere is empty. the palace grounds, the courtyard, everything just empty. its almost haunted like.\n"
            "you think to yourself:\n"
            "'cant stop now, after all that i faced, i will win against what lies ahead. I have to get that treasure, even if it costs me a limb'\n"
            "As you walk forward towards to castle entrance, you see a sign that reads:\n"
            "'HE WHO WISHES TO CONTINUE WILL FEEL THE WRATH OF THE QUEEN OF DARKNESS.'\n"
            "There is more next to the sign, a book. you open the book and read its contents. Its about the Queen that rules this castle.\n"
            "you read through to learn that queen was a feared ruler who lead an army of warriors so strong, they were feared in the land.\n"
            "however due to the queen's obsession with magic, she cursed the whole land. everyone died including her mighty army\n"
            "the queen however, went into a state of dormancy to protect her treasure. It is said that queen will wake up to fight and \n"
            "defend whats her's against anything that may come her way. after all during her obsession with magic, she achieved immortality.")
            dprint("now you know what lies ahead, in the castle. A queen so strong that she was feared throughtout the land. But she has treasure that you must\n"
            "get your hands on.\n"
            "so you soldier on into the castle. you make your way to the throne room where you expect to find both the queen and her treasure.\n"
            "And Just as you expected. There she was, the queen. laying down in the sleep waiting for someone to touch her tresure. you walk closer to\n"
            "the treasure and as soon as you get close enough, she awakens. The Undead queen awakens.\n")
            dprint("she sees you at the other end of the room. Anger flows through her body as she realises that you're there to steal her treasure.\n"
            "you final fight begins now")
            status=villain(75,40)
            return status




         def if_win():
            dprint("YOU HAVE DONE IT!! YOU HAVE BEATEN THE UNDEAD QUEEN!!!!! Now time to get your hands on that treasure. You look around to see if you can\n"
                "find the chest in which the treasure is kept. In the corner, you see a big golden box. That has to be the treasure chest. it has to be it\n"
                "You run towards the chest with excitment. As you kneel down to open the chest, you look at it to admire it. The chest seems to be made of\n"
                "solid gold which itself is good enough to make you rich for years to come, but you're here for whats inside the chest.\n"
                "you open the small latch on the chest and lift up the top to look inside. You have a big smile on your face from the excitment of being able\n"
                "to live out your wildest fantasies. As you look inside to see the treasure, two massive arms pop out from the chest to grab hold of you.\n"
                "the arms then pull you into the chest. you scream, trying to free yourself from the arms. inside the chest  there is a mouth, with razor sharp\n"
                "teeth. As the arms pull you into the chest, you realize that there never was any treasure in the chest. There was only a curse inside the chest\n"
                "waiting for someone like you to come along so that it can kill you.")
            dprint("GAME OVER")
                    
         status  = enemy1()
         if (status==0):
            status = enemy2()
            if(status==0):
                dprint("you have defeated the giant crab, WELL DONE!!!\n"
                "now time for you to carry on into the next part of the cave and fight your way to the treasure")
                status = enemy3()
                if (status==0):
                    status = enemy4()
                    if (status==0):
                            status=enemy5()
                            if(status==0):
                                if_win()

     
 else:
    print()
    dprint('You decide to be lazy and go home')
    input()
    print()
    dprint("END")
else:
   print()
   dprint("You walk away .... a truck comes by and hits the poor old man , but its not like you could have done anything")
   input()
   print()
   dprint("You decide go to back home and sleep , You've seen enough for the day")
   input()
   print()
   dprint('END')