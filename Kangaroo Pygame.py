import random
import pygame
reset_screen = False
reset_scrn = False
input_needed = False
tutorial = False
gamestart = False
user = False
start = True
active = False
reinforceddoors = False
shinypetrol = False
sonicwifi = False
wipers = False
wheel = False
hat = False
bow = False
perry = False
lights = False
echidna = False
h = 0
name = ""
ItemsActive = False
current_space = 1
KangaCash = 2000
pick = 0
pet = []
your_inventory = []
active_item = []
headwear = []
equipped_item = []
a = 0
b = 0
c = 0
d = 0
Shop = [
    #"Pretty Lights",
    #"Overcharged Space Canons",
    #"Reinforced Doors",
    #"Shiny Petrol",
    "A Pretty Bow",
    #"A Cool Hat",
    #"Sonic Speed WiFi",
    #"New Windshield Wipers",
    #"A Platypus Poster?",
    "Powered Steering Wheel",
    "Pet Echidna"
]
Shop_Descriptions = {
    "Pretty Lights":("Equipping these lights will earn you 15% more KangaCash","while in use. (Only one decoration may be in use at a time.)","",""),
    "Overcharged Space Canons":("Firing these space cannons will shoot you ahead two spaces.","","",""),
    "Reinforced Doors":("These doors will prevent you from going up to one space","backwards on your turn.","",""),
    "Shiny Petrol":("The shininess will take you twice as many spaces on your turn in style.","","",""),
    "A Cool Hat":("Your coolness will earn you 10% more KangaCash while equipped.","(Only one piece of headwear may be equipped at a time.)","",""),
    "A Pretty Bow":("Your prettiness will give you a 15% chance to move an extra","space while equipped. (Only one piece of headwear","may be equipped at a time.)",""),
    "Sonic Speed WiFi":("Your fast WiFi will take you an extra space further on","your turn.","",""),
    "New Windshield Wipers":("Your clear vision will allow you to reverse any","backwards movement you would have encountered on your turn.","",""),
    "A Platypus Poster?":("This awesome poster will give you a 10% chance to move","an extra space while in use. (Only one decoration may be in use at a time.)","",""),
    "Powered Steering Wheel":("This steering wheel will allow you to move up to","four spaces in any direction of your choice for your turn.","",""),
    "Pet Echidna":("This golden echidna will bring you both joy and 5 KangaCash","per turn.","","")
}
Shop_Prices = {
    "Pretty Lights":20,
    "Overcharged Space Canons":25,
    "Reinforced Doors":15,
    "Shiny Petrol":30,
    "A Cool Hat":20,
    "A Pretty Bow":30,
    "Sonic Speed WiFi":25,
    "New Windshield Wipers":25,
    "A Platypus Poster?":20,
    "Powered Steering Wheel":50,
    "Pet Echidna": 55
}
card = [
    #"Whirly Bird",
    #"Blackout",
    #"New Pair of Thongs",
    #"Cryo Machine",
    #"Wombat Encounter",
    #"Butcher",
    #"42 Wallaby Way, Sydney",
    #"Rockin' with it",
    #"Canceled",
    #"Bludge Around the House",
    #"Postie",
    #"Snaggs",
    "The Great Emu War",
    #"Shrimp on the Barbie",
    #"Opera",
    #"Dingo Encounter",
    #"New New Perth",
    #"Kangaroo Revolution",
    #"Boomerang",
    #"Wildfire"
]
card_description = {
    "Snaggs":("You go forward in time to eat some awesome sausages. ","Advance one space and lose 10 KangaCash","",""),
    "New Pair of Thongs":("You find some cool flipflops and decide to wear them in ","the future. Everyone loves them and wants to be your friend. ","Advance three spaces and gain 10 KangaCash",""),
    "Whirly Bird":("A helicopter crashes into your time machine. Lose ","10 KangaCash and fall back one space.","",""),
    "Blackout":("The power goes out in your time machine as you travel ","forward in time. You crash land 300 years before expected.","Advance two spaces and lose 10 KangaCash.",""),
    "Cryo Machine":("You fall into a cryo machine and wake up 1,000 years ","in the future. Advance five spaces and collect 10 KangaCash.","",""),
    "Wombat Encounter":("A wombat appears. He gives you a turbo engine ","attachment for your time machine. Advance two spaces ", "and gain 10 KangaCash.",""),
    "Butcher":("A butcher chases you, and you hastily escape by going ","forward in time. Advance one space and lose 10 KangaCash.","",""),
    "42 Wallaby Way, Sydney":("You go back in time to help a clownfish ","find his son. Go back one space and gain 20 KangaCash.","",""),
    "Rockin' with it":("You go back in time to audition for AC/DC. Go back ","one space and collect 30 KangaCash.","",""),
    "Canceled":("You accidentally become the world's most hated kangaroo. ","Go back two spaces and lose 20 KangaCash.","",""),
    "Bludge Around the House":("You don't want to do anything today. No ","advancement and lose 10 KangaCash.","",""),
    "Kangaroo Revolution":("You start a kangaroo revolution and travel ","forward in time to see the progress. Everything has gone as","planned. Advance three spaces and gain 20 KangaCash.",""),
    "Postie":("You receive an inheritence letter in the mail. You invest ","it and travel forward in time to collect the interest. ","Advance four spaces and collect 30 Kangacash.",""),
    "The Great Emu War":("You travel back in time to fight in the Great Emu ","War. You win. Go back two spaces and collect 20 KangaCash.","",""),
    "Shrimp on the Barbie":("You create an amazing barbecue sauce and travel ","forward in time to collect your royalties. Advance two","spaces and collect 20 KangaCash.",""),
    "Opera":("Someone named 'Sydney O. House' wants you to perform opera","in a few years. Advance one space and collect 10 KangaCash.","",""),
    "Dingo Encounter":("You escape a dingo by traveling into the future. Advance ","two spaces. No changes to KangaCash.","",""),
    "New New Perth":("You travel into the future to see Perth rebuilt after the ","Western Australian uprising of 2799. Advance four","spaces and collect 20 KangaCash.",""),
    "Boomerang":("While visiting the past, you find a magical boomerang that","shoots you forward in time. Advance two spaces","and collect 10 KangaCash.",""),
    "Wildfire":("A horrible fire breaks out and you barely make it out","alive by going forward in time. Advance two spaces","and lose 20 KangaCash.","")
}
card_money = {
    "Wildfire":-20,
    "Boomerang":10,
    "Whirly Bird":-10,
    "Blackout":-10,
    "New Pair of Thongs":10,
    "Cryo Machine":10,
    "Wombat Encounter":10,
    "Butcher":-10,
    "42 Wallaby Way, Sydney":20,
    "Rockin' with it":30,
    "Canceled":-20,
    "Bludge Around the House":-10,
    "Postie":30,
    "Snaggs":-10,
    "The Great Emu War":20,
    "Shrimp on the Barbie":20,
    "Opera":10,
    "Dingo Encounter":0,
    "New New Perth":20,
    "Kangaroo Revolution":20
}
card_space = {
    "Wildfire": 2,
    "Boomerang": 2,
    "Whirly Bird":-1,
    "Blackout":2,
    "New Pair of Thongs":3,
    "Cryo Machine":5,
    "Wombat Encounter":2,
    "Butcher":1,
    "42 Wallaby Way, Sydney":-1,
    "Rockin' with it":-1,
    "Canceled":-2,
    "Bludge Around the House":0,
    "Postie":4,
    "Snaggs":1,
    "The Great Emu War":-2,
    "Shrimp on the Barbie":2,
    "Opera":1,
    "Dingo Encounter":2,
    "New New Perth":4,
    "Kangaroo Revolution":3
}
Roll = 0
def Screen():
    default_screen = [250, 204, 125]
    screen.fill(default_screen)
    default_info = ("KangaCash Balance: " + str(KangaCash))
    words = font.render(default_info, True, "Black")
    if gamestart == True:
        screen.blit(words,((1020*ratio[0]),(820*ratio[1])))
def user_input(x):
    global input_needed
    global user 
    global d
    end = False
    user = True
    text_((x))
    while end == False:
        input_needed = True
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_y:
                    input_needed = True
                    d = 'y'
                    text_((d,"","",""))
                    end = True
                elif event.key == pygame.K_a:
                    input_needed = True
                    d = 'a'
                    text_((d,"","",""))
                    end = True
                elif event.key == pygame.K_b:
                    input_needed = True
                    d = 'b'
                    text_((d,"","",""))
                    end = True
                elif event.key == pygame.K_c:
                    input_needed = True
                    d = 'c'
                    text_((d,"","",""))
                    end = True
                elif event.key == pygame.K_RETURN:
                    input_needed = True
                    d = ' '
                    text_((d,"","",""))
                    end = True
def num_input():
    global d
    global input_needed
    global enter
    end = False
    input_needed = True
    enter = False
    d = ""
    text_(("How many spaces would you like to travel? ","Enter a number between -4 and 4.","",""))
    while end == False:
        input_needed = True
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    input_needed = True
                    d = str(d)+ '1'
                    text_((d,"","",""))
                    end = True
                elif event.key == pygame.K_2:
                    input_needed = True
                    d = str(d)+ '2'
                    text_((d,"","",""))
                    end = True
                elif event.key == pygame.K_3:
                    input_needed = True
                    d = str(d)+ '3'
                    text_((d,"","",""))
                    end = True
                elif event.key == pygame.K_4:
                    input_needed = True
                    d = str(d)+ '4'
                    text_((d,"","",""))
                    end = True
                elif event.key == pygame.K_MINUS:
                    input_needed = True
                    d = str(d)+ '-'
                    text_((d,"","",""))
                    end = False
                elif event.key == pygame.K_BACKSPACE:
                    if len(d) >= 1:
                        input_needed = True
                        d = d[:-1]
                        text_((d,"","",""))
                    else:
                        input_needed = True
                        d = d
                        text_((d,"","",""))
def user_name():
    global name
    global input_needed
    global enter
    global g
    end = False
    input_needed = True
    enter = False
    text_(("Please enter your name.","","",""))
    while end == False:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    input_needed = True
                    g = 'A'
                    name = str(name) + str(g)
                    text_((name,"","",""))
                elif event.key == pygame.K_b:
                    input_needed = True
                    g = 'B'
                    name = str(name) + str(g)
                    text_((name,"","",""))
                elif event.key == pygame.K_c:
                    input_needed = True
                    g = 'C'
                    name = str(name) + str(g)
                    text_((name,"","",""))
                elif event.key == pygame.K_d:
                    input_needed = True
                    g = 'D'
                    name = str(name) + str(g)
                    text_((name,"","",""))
                elif event.key == pygame.K_e:
                    input_needed = True
                    g = 'E'
                    name = str(name) + str(g)
                    text_((name,"","",""))
                elif event.key == pygame.K_f:
                    input_needed = True
                    g = 'F'
                    name = str(name) + str(g)
                    text_((name,"","",""))
                elif event.key == pygame.K_g:
                    input_needed = True
                    g = 'G'
                    name = str(name) + str(g)
                    text_((name,"","",""))
                elif event.key == pygame.K_h:
                    input_needed = True
                    g = 'H'
                    name = str(name) + str(g)
                    text_((name,"","",""))
                elif event.key == pygame.K_i:
                    input_needed = True
                    g = 'I'
                    name = str(name) + str(g)
                    text_((name,"","",""))
                elif event.key == pygame.K_j:
                    input_needed = True
                    g = 'J'
                    name = str(name) + str(g)
                    text_((name,"","",""))
                elif event.key == pygame.K_k:
                    input_needed = True
                    g = 'K'
                    name = str(name) + str(g)
                    text_((name,"","",""))
                elif event.key == pygame.K_l:
                    input_needed = True
                    g = 'L'
                    name = str(name) + str(g)
                    text_((name,"","",""))
                elif event.key == pygame.K_m:
                    input_needed = True
                    g = 'M'
                    name = str(name) + str(g)
                    text_((name,"","",""))
                elif event.key == pygame.K_n:
                    input_needed = True
                    g = 'N'
                    name = str(name) + str(g)
                    text_((name,"","",""))
                elif event.key == pygame.K_o:
                    input_needed = True
                    g = 'O'
                    name = str(name) + str(g)
                    text_((name,"","",""))
                elif event.key == pygame.K_p:
                    input_needed = True
                    g = 'P'
                    name = str(name) + str(g)
                    text_((name,"","",""))
                elif event.key == pygame.K_q:
                    input_needed = True
                    g = 'Q'
                    name = str(name) + str(g)
                    text_((name,"","",""))
                elif event.key == pygame.K_r:
                    input_needed = True
                    g = 'R'
                    name = str(name) + str(g)
                    text_((name,"","",""))
                elif event.key == pygame.K_s:
                    input_needed = True
                    g = 'S'
                    name = str(name) + str(g)
                    text_((name,"","",""))
                elif event.key == pygame.K_t:
                    input_needed = True
                    g = 'T'
                    name = str(name) + str(g)
                    text_((name,"","",""))
                elif event.key == pygame.K_u:
                    input_needed = True
                    g = 'U'
                    name = str(name) + str(g)
                    text_((name,"","",""))
                elif event.key == pygame.K_v:
                    input_needed = True
                    g = 'V'
                    name = str(name) + str(g)
                    text_((name,"","",""))
                elif event.key == pygame.K_w:
                    input_needed = True
                    g = 'W'
                    name = str(name) + str(g)
                    text_((name,"","",""))
                elif event.key == pygame.K_x:
                    input_needed = True
                    g = 'X'
                    name = str(name) + str(g)
                    text_((name,"","",""))
                elif event.key == pygame.K_y:
                    input_needed = True
                    g = 'Y'
                    name = str(name) + str(g)
                    text_((name,"","",""))
                elif event.key == pygame.K_z:
                    input_needed = True
                    g = 'Z'
                    name = str(name) + str(g)
                    text_((name,"","",""))
                elif event.key == pygame.K_SPACE:
                    input_needed = True
                    g = ' '
                    name = str(name) + str(g)
                    text_((name,"","",""))
                elif event.key == pygame.K_MINUS:
                    input_needed = True
                    g = '-'
                    name = str(name) + str(g)
                    text_((name,"","",""))
                elif event.key == pygame.K_BACKSPACE:
                    if len(name) >= 1:
                        input_needed = True
                        name = name[:-1]
                        text_((name,"","",""))
                    else:
                        input_needed = True
                        name = name
                        text_((name,"","",""))
                elif event.key == pygame.K_RETURN:
                    input_needed = True
                    end = True
                    text_((name,"","",""))
    if end == True:
        pygame.display.flip()
def text_(x):
    global enter
    global input_needed
    global d
    global screen
    posx = 10*ratio[0]
    posy = 10*ratio[1]
    position = posx, posy
    p, q, r, s = x
    screen = pygame.display.set_mode()
    text1 = font.render(p, True, "Black")
    text2 = font.render(q, True, "Black")
    text3 = font.render(r, True, "Black")
    text4 = font.render(s, True, "Black")
    if input_needed == True:
        enter = False
    else:
        enter = True
    if enter == True:
        while enter == True:
            Screen()
            screen.blit(text1,(position[0],(int(position[1])+int(75*int(0)))))
            screen.blit(text2,(position[0],(int(position[1])+int(75*int(1)))))
            screen.blit(text3,(position[0],(int(position[1])+int(75*int(2)))))
            screen.blit(text4,(position[0],(int(position[1])+int(75*int(3)))))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        d = ' '
                        enter = False
                        pause(.2)
                        pygame.display.flip()
                        pause(.2)
    else:
        Screen()
        screen.blit(text1,(position[0],(int(position[1])+int(75*int(0)))))
        screen.blit(text2,(position[0],(int(position[1])+int(75*int(1)))))
        screen.blit(text3,(position[0],(int(position[1])+int(75*int(2)))))
        screen.blit(text4,(position[0],(int(position[1])+int(75*int(3)))))
        input_needed = False
        pause(.1)
        pygame.display.flip()
def pause(x):
    pygame.time.wait(int(x*1000))
def roll():
    global pick
    global Roll
    n = len(card)
    Roll = random.randrange(0,n)
    pick = card[Roll]
    if current_space == 0:
        if int(card_space[pick]) <= 0:
            roll()
        else:
            text_(("'" + card[Roll]+ "'","","",""))
            text_((card_description[pick]))
    else:
        text_(("'" + card[Roll]+ "'","","",""))
        text_((card_description[pick])) 
    pygame.display.flip()
def cash():
    global KangaCash
    y = card_money[pick]
    if hat == True:
        if lights == True:
            y *= 1.25
        else:
            y *= 1
    elif lights == True:
        y *=1.15
        y = int(y)
    else:
        pause(.1)
    if echidna == True:
        y += 5
    else:
        pause(.1)
    if y > 0:
        KangaCash += y
    else:
        if KangaCash <= abs(y):
            KangaCash = 0
        else:
            KangaCash += y
    pygame.display.flip()
def Tutorial(y):
    x = y
    global input_needed
    global tutorial
    while tutorial == True:
        input_needed = True
        if x == 1:
            user_input(("In Time-Traveling Kangaroo, the objective is","to reach the end of time (AKA the end of the board).","On your turn, you will press the 'enter' key on your keyboard.", "(Press 'c' to continue to the next page or 'enter' to exit tutorial)"))
            if d == 'c':
                Tutorial(2)
            else:
                tutorial = False
        if x == 2:    
            user_input(("You will also need to press 'enter' once you have","finished reading any text on the screen that does not have","other instructions. Once you have pressed 'enter' on your turn,","(Press 'c' to continue, 'a' to go back a page, or 'enter' to exit tutorial)"))
            if d == 'c':
                Tutorial(3)
            elif d == 'a':
                Tutorial(1)
            else:
                tutorial = False
        if x == 3:
            user_input(("you will receive an event card telling you how","many spaces to move in which direction, and how much KangaCash","you collect or lose. On spaces 7, 15, 27, and 32, you will encounter","(Press 'c' to continue, 'a' to go back a page, or 'enter' to exit tutorial)"))
            if d == 'c':
                Tutorial(4)
            elif d == 'a':
                Tutorial(2)
            else:
                tutorial = False
        if x == 4:
            user_input(("the shop, where you can purchase items. Most items","are single-use and will disappear after their effect has been triggered.","Decorations, pets, and headwear are game-long items, but only one","(Press 'c' to continue, 'a' to go back a page, or 'enter' to exit tutorial)"))
            if d == 'c':
                Tutorial(5)
            elif d == 'a':
                Tutorial(3)
            else:
                tutorial = False
        if x == 5:
            user_input(("of each may be equipped at any given time. If you","choose to change one of these game-long items, you must first discard","the item you currently have equipped. You may only have 3 items in your","(Press 'c' to continue, 'a' to go back a page, or 'enter' to exit tutorial)"))
            if d == 'c':
                Tutorial(6)
            elif d == 'a':
                Tutorial(4)
            else:
                tutorial = False
        if x == 6:
            user_input(("inventory at a time (this does not include equipped","items).","","(Press 'a' to go back a page or 'enter' to exit tutorial)"))
            if d == 'a':
                Tutorial(5)
            else:
                tutorial = False
def BG():
    global background1
    global background2
    global background3
    global background4
    global background5
    global background6
    global background7
    global current_space_abs
    global background
    global location
    global reset_screen
    global reset_scrn
    num = (size[0]/12)
    background1 = pygame.image.load('background1.jpg').convert_alpha()
    background2 = pygame.image.load('background2.jpg').convert_alpha()
    background3 = pygame.image.load('background3.jpg').convert_alpha()
    background4 = pygame.image.load('background4.jpg').convert_alpha()
    background5 = pygame.image.load('background5.jpg').convert_alpha()
    background6 = pygame.image.load('background6.jpg').convert_alpha()
    background7 = pygame.image.load('background7.jpg').convert_alpha()
    if current_space <= 5:
        current_space_abs = current_space
        background = background1
        location = (-500*ratio[0], -500*ratio[1])
    elif current_space <= 11:
        current_space_abs = current_space -6
        background = background2
        location = (num,200*ratio[1])
    elif current_space <= 17:
        current_space_abs = current_space -12
        background = background3
        location = (num*5,200*ratio[1])
    elif current_space <= 23:
        current_space_abs = current_space -18
        background = background4
        location = (-500*ratio[0],-500*ratio[1])
    elif current_space <= 29:
        current_space_abs = current_space -24
        background = background5
        location = (num*5,200*ratio[1])
    elif current_space <= 35:
        current_space_abs = current_space -30
        background = background6
        location = (num*5,200*ratio[1])
    else:
        current_space_abs = current_space -36
        background = background7
        location = (-500*ratio[0],-500*ratio[1])
    if current_space_abs == 0:
        reset_screen = True
    elif current_space_abs == 5:
        reset_scrn = True
    background = pygame.transform.scale(background, (1536*ratio[0],846*ratio[1]))
def hopping():
    global current_space
    global reset_screen
    Shop = pygame.image.load('shop.png').convert_alpha()
    Shop = pygame.transform.scale(Shop,((500*ratio[0]),(500*ratio[1])))
    num = (size[0]/12)
    BG()
    if bow == True:
        kangaroo1base = pygame.image.load('Kangaroo1Bow.png').convert_alpha()
        kangaroo2base = pygame.image.load('Kangaroo2Bow.png').convert_alpha()
    elif hat == True:
        kangaroo1base = pygame.image.load('Kangaroo1Hat.png').convert_alpha()
        kangaroo2base = pygame.image.load('Kangaroo2Hat.png').convert_alpha()
    else:
        kangaroo1base = pygame.image.load('Kangaroo1.png').convert_alpha()
        kangaroo2base = pygame.image.load('Kangaroo2.png').convert_alpha()
    kangaroo1 = pygame.transform.scale(kangaroo1base,((300*ratio[0]),(300*ratio[1])))
    kangaroo2 = pygame.transform.scale(kangaroo2base,((300*ratio[0]),(300*ratio[1])))
    x = ((current_space_abs*num*2)-(100*ratio[0]))
    BG()
    screen.blit(background,(0,-23))
    if echidna == True:
        screen.blit(Echidna,(((x*ratio[0])-20*ratio[0]),(600*ratio[1])))
    screen.blit(Shop,location)
    screen.blit(kangaroo1,((x),(400*ratio[1])))
    x += num
    pygame.display.flip()
    pause(.2)
    screen.blit(background,(0,-23))
    if echidna == True:
        screen.blit(Echidna,(((x*ratio[0])-20*ratio[0]),(600*ratio[1])))
    screen.blit(Shop,location)
    screen.blit(kangaroo2,((x),(400*ratio[1])))
    pygame.display.flip()
    pause(.2)
    current_space += 1
    BG()
    if reset_screen == True:
        x = ((current_space_abs*num*2)-(100*ratio[0]))
        reset_screen = False
    else:
        x += num
    screen.blit(background,(0,-23))
    if echidna == True:
        screen.blit(Echidna,(((x*ratio[0])-20*ratio[0]),(600*ratio[1])))
    screen.blit(Shop,location)
    screen.blit(kangaroo1,((x),(400*ratio[1])))
    pygame.display.flip()
    pause(1)
def flopping():
    global current_space
    global reset_scrn
    Shop = pygame.image.load('shop.png').convert_alpha()
    Shop = pygame.transform.scale(Shop,((500*ratio[0]),(500*ratio[1])))
    num = (size[0]/24)
    BG()
    if bow == True:
        kangaroo1base = pygame.image.load('Kangaroo1Bow.png').convert_alpha()
        kangaroo3base = pygame.image.load('Kangaroo3Bow.png').convert_alpha()
        kangaroo4base = pygame.image.load('Kangaroo4Bow.png').convert_alpha()
        kangaroo5base = pygame.image.load('Kangaroo5Bow.png').convert_alpha()
    elif hat == True:
        kangaroo1base = pygame.image.load('Kangaroo1Hat.png').convert_alpha()
        kangaroo3base = pygame.image.load('Kangaroo3Hat.png').convert_alpha()
        kangaroo4base = pygame.image.load('Kangaroo4Hat.png').convert_alpha()
        kangaroo5base = pygame.image.load('Kangaroo5Hat.png').convert_alpha()
    else:
        kangaroo1base = pygame.image.load('Kangaroo1.png').convert_alpha()
        kangaroo3base = pygame.image.load('Kangaroo3.png').convert_alpha()
        kangaroo4base = pygame.image.load('Kangaroo4.png').convert_alpha()
        kangaroo5base = pygame.image.load('Kangaroo5.png').convert_alpha()
    kangaroo1 = pygame.transform.scale(kangaroo1base,((300*ratio[0]),(300*ratio[1])))
    kangaroo3 = pygame.transform.scale(kangaroo3base,((300*ratio[0]),(300*ratio[1])))
    kangaroo4 = pygame.transform.scale(kangaroo4base, ((300*ratio[0]),(300*ratio[1])))
    kangaroo5 = pygame.transform.scale(kangaroo5base, ((300*ratio[0]),(300*ratio[1])))
    x = ((current_space_abs*num*4)-(100*ratio[0]))
    screen.blit(background,(0,-23))
    if echidna == True:
        screen.blit(Echidna,(((x*ratio[0])-20*ratio[0]),(600*ratio[1])))
    screen.blit(Shop,location)
    screen.blit(kangaroo1,((x*ratio[0]),(400*ratio[1])))
    x -= num
    pygame.display.flip()
    pause(.2)
    screen.blit(background,(0,-23))
    if echidna == True:
        screen.blit(Echidna,(((x*ratio[0])-20*ratio[0]),(600*ratio[1])))
    screen.blit(Shop,location)
    screen.blit(kangaroo3,((x*ratio[0]),(400*ratio[1])))
    x -= num
    pygame.display.flip()
    pause(.2)
    screen.blit(background,(0,-23))
    if echidna == True:
        screen.blit(Echidna,(((x*ratio[0])-20*ratio[0]),(600*ratio[1])))
    screen.blit(Shop,location)
    screen.blit(kangaroo4,((x*ratio[0]),(400*ratio[1])))
    x -= num
    pygame.display.flip()
    pause(.2)
    current_space -= 1
    BG()
    if reset_scrn == True:
        x = ((current_space_abs*num*4)-(100*ratio[0]))
        reset_scrn = False
    else:
        x -= num
    screen.blit(background,(0,-23))
    if echidna == True:
        screen.blit(Echidna,(((x*ratio[0])-20*ratio[0]),(600*ratio[1])))
    screen.blit(Shop,location)
    screen.blit(kangaroo5,((x*ratio[0]),(400*ratio[1])))
    x -= num
    pygame.display.flip()
    pause(1)
def hop():
    x = abs(card_space[pick]) 
    global current_space
    global shinypetrol
    global KangaCash
    q = 0
    if shinypetrol == True:
        x *= 2
        shinypetrol = False
    else:
        x *= 1
    if bow == True:
        h = random.randrange(0,100)
        if h <= 14:
            x += 1
        else:
            pause(.1)
    if perry == True:
        h = random.randrange(0,10)
        if h == 7:
            x += 1
        else:
            pause(.1)
    if x == 1:
        text_(("Kangaroo moves " + str(x) + " space forward.","","",""))
    else:
        text_(("Kangaroo moves " + str(x) + " spaces forward.","","",""))
    while q < x:
        hopping()
        q +=1
        shop()
    pygame.display.flip()
def flop():
    x = card_space[pick]
    global current_space
    global KangaCash
    global shinypetrol
    global reinforceddoors
    global sonicwifi
    global wipers
    q = 0
    if shinypetrol == True:
        x *= 2
        shinypetrol = False
    else:
        pause(.1)
    if reinforceddoors == True:
        x += 1
        reinforceddoors = False
    else:
        pause(.1)
    if sonicwifi == True:
        x -= 1
        sonicwifi = False
    else:
        pause(.1)
    if wipers == True:
        hop()
        x = 0
        wipers = False
    else:
        pause(.1)
    if x == -1:
        text_(("Kangaroo falls " + str(abs(x)) + " space back.","","",""))
    elif x >= 0:
        text_(("Active items have prevented the time machine from going","back in time.","",""))
    else:
        text_(("Kangaroo falls " + str(abs(x)) + " spaces back.","","",""))
    if current_space >= abs(x):
        while q < abs(x):
            flopping()
            q += 1
            shop()
    elif x >= 0:
        pause(.1)
    else:
        while current_space > 0:
            flopping()
            shop()
    pause(1)
def shop():
    global input_needed
    global your_inventory
    global a
    global b
    global c
    global d
    global picka
    global pickb
    global pickc
    global KangaCash
    if current_space == 7 or current_space == 15 or current_space == 27 or current_space == 32:
        a = random.randrange(0,11)
        b = random.randrange(0,11)
        while b == a:
            b = random.randrange(0,11)
        c = random.randrange(0,11)
        while c == a:
            c = random.randrange(0,11)
            while c == b:
                c = random.randrange(0,11)
        while c == b:
            c = random.randrange(0,11)
            while c == a:
                c = random.randrange(0,11)
        picka = Shop[a]
        pickb = Shop[b]
        pickc = Shop[c]
        input_needed = True
        user_input(("Welcome to the shop. Would you like to look around?","","","Enter 'y' for yes, or press 'enter' to continue on."))
        if d == 'y':
            display()
        else:
            text_(("Okay, maybe next time!","","",""))
def equip(x):
    global input_needed
    global your_inventory
    global equipped_item
    global headwear
    global active_item
    x = str(your_inventory[x])
    if x == "Pretty Lights" or x == "A Platypus Poster?":
        if len(equipped_item) == 1:
            input_needed = True
            user_input(("Sorry, you may only have one decoration in use at a time.","You currently are using " + equipped_item[0] + ".","Press 'y' to discard this item and equip " + x + ",","or press 'enter' to continue without equipping this item."))
            if d == 'y':
                equipped_item[0] = x
                your_inventory.remove(x)
                text_((("You have successfully equipped " + equipped_item[0] + "."),"","",""))
            else:
                text_(("Okay, maybe next time.","","",""))
        else:
            equipped_item.append(x)
            your_inventory.remove(x)
            text_((("You have successfully equipped " + equipped_item[0] + "."),"","",""))
    elif x == "A Cool Hat" or x == "A Pretty Bow":
        if len(headwear) == 1:
            input_needed = True
            user_input(("Sorry, your head isn't big enough for two accessories.","You are currently wearing " + headwear[0] + ".","Press 'y' to discard this item and equip " + x + ",", "or press 'enter' to continue without equipping this item."))
            if d == 'y':
                headwear[0] = x
                your_inventory.remove(x)
                text_(("You have successfully equipped " + headwear[0] + ".","","",""))
            else:
                text_(("Okay, maybe next time.","","",""))
        else:
            headwear.append(x)
            your_inventory.remove(x)
            text_(("You have successfully equipped " + headwear[0] + ".","","",""))
    else:
        active_item.append(x)
        your_inventory.remove(x)
        text_(("You have successfully equipped " + active_item[0] + ".","","",""))
    item_active()
def item_active():
    global reinforceddoors
    global shinypetrol
    global pick
    global active_item
    global sonicwifi
    global wipers
    global wheel
    global hat
    global bow
    global perry
    global lights
    if len(active_item) == 1:
        if active_item[0] == "Overcharged Space Canons":
            pick = "Wombat Encounter"
            hop()
            active_item.clear()
        elif active_item[0] == "Reinforced Doors":
            reinforceddoors = True
            active_item.clear()
        elif active_item[0] == "Shiny Petrol":
            shinypetrol = True
            active_item.clear()          
        elif active_item[0] == "Sonic Speed WiFi":
            sonicwifi = True
            active_item.clear()
        elif active_item[0] == "New Windshield Wipers":
            wipers = True
            active_item.clear()
        elif active_item[0] == "Powered Steering Wheel":
            wheel = True
            active_item.clear()
    elif len(headwear) == 1:
        if headwear[0] == "A Cool Hat":
            hat = True
        else:
            bow = True
    elif len(equipped_item) == 1:
        if equipped_item[0] == "A Platypus Poster?":
            perry = True
        else:
            lights = True
def Pet():
    global your_inventory
    global pet
    global echidna
    global Echidna
    if "Pet Echidna" in your_inventory:
        if len(pet) == 1:
            your_inventory.remove("Pet Echidna")
            echidna = True
            text_(("You may not have more than one pet at a time, so", "your Pet Echidna has been removed from your inventory.","",""))
        else:
            your_inventory.remove("Pet Echidna")
            pet.append("Pet Echidna")
            echidna = True
            text_(("Your Pet Echidna has been moved to your pet slot.","","",""))
        Echidna = pygame.image.load('echidna.png').convert_alpha()
        Echidna = pygame.transform.scale(Echidna, (100*ratio[0], 100*ratio[1]))
    else:
        pause(.1)
def display():
    global your_inventory
    global d
    global KangaCash
    text_(("Hi, " + name + "! Here are today's goods:","","",""))
    text_((picka, pickb, pickc,""))
    description_ask()
def description_ask():
    global your_inventory
    global input_needed
    global d
    global KangaCash
    input_needed = True
    user_input(("Press 'a' to view or purchase '" + picka + "',","'b' to view or purchase '" + pickb + "', ","'c' to view or purchase '" + pickc + "', or ","'enter' to continue on."))
    if d == 'a' or d == 'b' or d == 'c':
        description()
    else:
        text_(("Okay, maybe next time!","","",""))
def description(): 
    global input_needed
    global your_inventory  
    global d
    global KangaCash
    if d == 'a':
        text_(Shop_Descriptions[picka])
        text_(("Cost: " + str(Shop_Prices[picka]) + " KangaCash","","",""))
        if KangaCash < Shop_Prices[picka]:
            text_(("Sorry, you do not have enough KangaCash for this item.","","",""))
            description_ask()
        else:
            input_needed = True
            user_input(("Would you like to purchase " + Shop[a] + "?","Press 'y' for yes, or press 'enter' to see other options.","",""))
            if d == 'y':
                if len(your_inventory) == 3:
                    text_(("Sorry, you cannot have more than three items in your ","inventory at a time. Please discard one.","",""))
                    input_needed = True
                    user_input(("Press 'a' to discard " + your_inventory[0] + ",","'b' to discard " + your_inventory[1] + ",","'c' to discard " + your_inventory[2] + ", or ","'enter' to cancel your purchase."))
                    if d == 'a':
                        your_inventory.remove(0)
                        KangaCash -= Shop_Prices[picka]
                        your_inventory.append(picka)
                        text_(("You now have " + picka + " in your inventory.","","",""))
                    elif d == 'b':
                        your_inventory.remove(1)
                        KangaCash -= Shop_Prices[picka]
                        your_inventory.append(picka)
                        text_(("You now have " + picka + " in your inventory.","","",""))
                    elif d == 'c':
                        your_inventory.remove(2)
                        KangaCash -= Shop_Prices[picka]
                        your_inventory.append(picka)
                        text_(("You now have " + picka + " in your inventory.","","",""))
                    else:
                        text_(("Okay, maybe next time!","","",""))
                else:
                    KangaCash -= Shop_Prices[picka]
                    your_inventory.append(picka)
                    text_(("You now have " + picka + " in your inventory.","","","")) 
            else:
                description_ask()
    elif d == 'b':
        text_(Shop_Descriptions[pickb])
        text_(("Cost: " + str(Shop_Prices[pickb]) + " KangaCash","","",""))
        if KangaCash < Shop_Prices[pickb]:
            text_(("Sorry, you do not have enough KangaCash for this item.","","",""))
            description_ask()
        else:
            text_(("Would you like to purchase " + Shop[b] + "?","","",""))
            input_needed = True
            user_input(("Enter 'y' for yes, or press 'enter' to see other options.","","",""))
            if d == 'y':
                if len(your_inventory) == 3:
                    text_(("Sorry, you cannot have more than three items in your ","inventory at a time. Please discard one.","",""))
                    input_needed = True
                    user_input(("Press 'a' to discard " + your_inventory[0] + ", ","'b' to discard " + your_inventory[1] + ", ","'c' to discard " + your_inventory[2] + ", or ","'enter' to cancel your purchase."))
                    if d == 'a':
                        your_inventory.remove(0)
                        KangaCash -= Shop_Prices[pickb]
                        your_inventory.append(pickb)
                        text_(("You now have " + pickb + " in your inventory.","","",""))
                    elif d == 'b':
                        your_inventory.remove(1)
                        KangaCash -= Shop_Prices[pickb]
                        your_inventory.append(pickb)
                        text_(("You now have " + pickb + " in your inventory.","","",""))
                    elif d == 'c':
                        your_inventory.remove(2)
                        KangaCash -= Shop_Prices[pickb]
                        your_inventory.append(pickb)
                        text_(("You now have " + pickb + " in your inventory.","","",""))     
                    else:
                        text_(("Okay, maybe next time!","","",""))
                else:
                    KangaCash -= Shop_Prices[pickb]
                    your_inventory.append(pickb)
                    text_(("You now have " + pickb + " in your inventory.","","",""))
            else:
                description_ask()
    else:
        text_(Shop_Descriptions[pickc])
        text_(("Cost: " + str(Shop_Prices[pickc]) + " KangaCash","","",""))
        if KangaCash < Shop_Prices[pickc]:
            text_(("Sorry, you do not have enough KangaCash for this item.","","",""))
            description_ask()
        else:
            text_(("Would you like to purchase " + Shop[c] + "?","","",""))
            input_needed = True
            user_input(("Enter 'y' for yes, or press 'enter' to see other options.","","",""))
            if d == 'y':
                if len(your_inventory) == 3:
                    text_(("Sorry, you cannot have more than three items in your ","inventory at a time. Please discard one.","",""))
                    input_needed = True
                    user_input(("Press 'a' to discard " + your_inventory[0] + ", ","'b' to discard " + your_inventory[1] + ", ","'c' to discard " + your_inventory[2] + ", or ","'enter' to cancel your purchase."))
                    if d == 'a':
                        your_inventory.remove(0)
                        KangaCash -= Shop_Prices[pickc]
                        your_inventory.append(pickc)
                        text_(("You now have " + pickc + " in your inventory.","","",""))
                    elif d == 'b':
                        your_inventory.remove(1)
                        KangaCash -= Shop_Prices[pickc]
                        your_inventory.append(pickc)
                        text_(("You now have " + pickc + " in your inventory.","","",""))
                    elif d == 'c':
                        your_inventory.remove(2)
                        KangaCash -= Shop_Prices[pickc]
                        your_inventory.append(pickc)
                        text_(("You now have " + pickc + " in your inventory.","","",""))   
                    else:
                        text_(("Okay, maybe next time!","","",""))
                else:
                    KangaCash -= Shop_Prices[pickc]
                    your_inventory.append(pickc)
                    text_(("You now have " + pickc + " in your inventory.","","",""))  
            else:
                description_ask()
    Pet()
def item():
    pygame.display.flip()
    global your_inventory
    global input_needed
    global KangaCash
    global current_space
    global headwear
    global equipped_item
    if len(your_inventory) == 0:
        text_(("You currently have no items to use.","","",""))
    else:
        input_needed = True
        user_input(("Would you like to use or equip an item?","Press 'y' to access your items or ","'enter' to continue without using an item.",""))
        if d == 'y':
            text_(("You have: " + str(your_inventory),"","",""))
            if len(your_inventory) == 1:
                input_needed = True
                user_input(("Would you like to view or use your items?","Press 'y' to view or use " + your_inventory[0] + " or ","'enter' to continue on without using items.",""))
                if d == 'y':
                    text_((Shop_Descriptions[your_inventory[0]]))
                    input_needed = True
                    user_input(("Press 'y' to use this item, or ","'enter' to continue without using an item.","",""))
                    if d == 'y':
                        equip(0)
                    else:
                        text_(("Okay, maybe next time!","","",""))
            elif len(your_inventory) == 2:
                input_needed = True
                user_input(("Press 'a' to view or use " + your_inventory[0] + ", ","'b' to view or use " + your_inventory[1] + ", or ","'enter' to continue on without using items.",""))
                if d == 'a':
                    text_(Shop_Descriptions[your_inventory[0]],3)
                    input_needed = True
                    user_input(("Press 'y' to use this item, ","'b' to view or use " + your_inventory[1] + ", or ","'enter' to continue without using an item.",""))
                    if d == 'y':
                        equip(0)
                    elif d == 'b':
                        text_(Shop_Descriptions[your_inventory[1]])
                        input_needed = True
                        user_input(("Press 'y' to use this item, ","'a' to equip " + your_inventory[0] + ", or ","'enter' to continue without using an item.",""))
                        if d == 'y':
                            equip(1)
                        elif d == 'a':
                            equip(0)
                        else:
                            text_(("Okay, maybe next time!","","",""))
                    else:
                        text_(("Okay, maybe next time!","","",""))
                elif d == 'b':
                    text_(Shop_Descriptions[your_inventory[1]])
                    input_needed = True
                    user_input(("Press 'y' to use this item, ","'a' to view " + your_inventory[0] + ", ","or 'enter' to continue without using an item.",""))
                    if d == 'y':
                        equip(1)
                    elif d == 'a':
                        text_(Shop_Descriptions[your_inventory[0]])
                        input_needed = True
                        user_input(("Press 'y' to use this item, ","'b' to equip " + your_inventory[1] + ", "," or 'enter' to continue without using an item.",""))
                        if d == 'y':
                            equip(0)
                        elif d == 'b':
                            equip(1)
                        else:
                            text_(("Okay, maybe next time!","","",""))
                    else:
                        text_(("Okay, maybe next time!","","",""))
                else:
                    text_(("Okay, maybe next time!","","",""))
            else:
                input_needed = True
                user_input(("Press 'a' to view or use " + your_inventory[0] + ", ","'b' to view or use " + your_inventory[1] + ", ","'c' to view or use " + your_inventory[2] + ", or ","'enter' to continue on without using items."))
                if d == 'a':
                    text_(Shop_Descriptions[your_inventory[0]])
                    input_needed = True
                    user_input(("Press 'y' to use this item, ","'b' to view or use " + your_inventory[1] + ", ","'c' to view or use " + your_inventory[2] + ", or ","'enter' to continue without using an item."))
                    if d == 'y':
                        equip(0)
                    elif d == 'b':
                        text_(Shop_Descriptions[your_inventory[1]])
                        input_needed = True
                        user_input(("Press 'y' to use this item, ","'a' to equip " + your_inventory[0] + ", ","'c' to view or use " + your_inventory[2] + ", or ","'enter' to continue without using an item."))
                        if d == 'y':
                            equip(1)
                        elif d == 'a':
                            equip(0)
                        elif d == 'c':
                            text_(Shop_Descriptions[your_inventory[2]])
                            input_needed = True
                            user_input(("Press 'y' to use this item, ","'a' to equip " + your_inventory[0] + ", ","'b' to equip " + your_inventory[1] + ", or ","'enter' to continue without using an item."))
                            if d == 'y':                                
                                equip(2)   
                            elif d == 'a':
                                equip(0)
                            elif d == 'b':
                                equip(1)     
                            else:
                                text_("Okay, maybe next time!","","","")
                        else:
                            text_("Okay, maybe next time!","","","")
                    else:
                        text_(("Okay, maybe next time!","","",""))
                elif d == 'b':
                    text_(Shop_Descriptions[your_inventory[1]])
                    input_needed = True
                    user_input(("Press 'y' to use this item, ","'a' to view or use " + your_inventory[0] + ", ","'c' to view or use " + your_inventory[2] + ", or ","'enter' to continue without using an item."))
                    if d == 'y':
                        equip(1)                        
                    elif d == 'a':
                        text_(Shop_Descriptions[your_inventory[0]])
                        input_needed = True
                        user_input(("Press 'y' to use this item, ","'b' to equip " + your_inventory[1] + ", ","'c' to view or use " + your_inventory[2] + ", or ","'enter' to continue without using an item."))
                        if d == 'y':
                            equip(0)
                        elif d == 'b':
                            equip(1)
                        elif d == 'c':
                            text_(Shop_Descriptions[your_inventory[2]])
                            input_needed = True
                            user_input(("Press 'y' to use this item, ","'a' to equip " + your_inventory[0] + ", ","'b' to equip " + your_inventory[1] + ", or ","'enter' to continue without using an item."))
                            if d == 'y':
                                equip(2)
                            elif d == 'a':
                                equip(1)
                            elif d == 'b':
                                equip(2)
                            else:
                                text_(("Okay, maybe next time!","","",""))
                        else:
                            text_(("Okay, maybe next time!","","",""))
                    elif d == 'c':
                        text_(Shop_Descriptions[your_inventory[2]])
                        input_needed = True
                        user_input(("Press 'y' to use this item, ","'a' to view or use " + your_inventory[0] + ", ","'b' to equip " + your_inventory[1] + ", or ","'enter' to continue without using an item."))
                        if d == 'y':
                            equip(2)
                        elif d == 'a':
                            text_(Shop_Descriptions[your_inventory[0]])
                            input_needed = True
                            user_input(("Press 'y' to use this item, ","'b' to equip " + your_inventory[1] + ", ","'c' to equip " + your_inventory[2] + ", or ","'enter' to continue without using an item."))
                            if d == 'y':
                                equip(0)
                            elif d =='b':
                                equip(1)
                            elif d == 'c':
                                equip(2)
                            else:
                                text_(("Okay, maybe next time!","","",""))
                        elif d == 'b':
                            equip(1)
                        else:
                            text_(("Okay, maybe next time!","","",""))            
                    else:
                        text_(("Okay, maybe next time!","","",""))
                elif d == 'c':
                    text_(Shop_Descriptions[your_inventory[2]])
                    input_needed = True
                    user_input(("Press 'y' to use this item, ","'a' to view or use " + your_inventory[0] + ", ","'b' to view or use " + your_inventory[1] + ", or ","'enter' to continue without using an item."))
                    if d == 'y':
                        equip(2)
                    elif d == 'a':
                        text_(Shop_Descriptions[your_inventory[0]])
                        input_needed = True
                        user_input(("Press 'y' to use this item, ","'b' to view or use " + your_inventory[1] + ", ","'c' to equip " + your_inventory[2] + ", or ","'enter' to continue without using an item."))
                        if d == 'y':
                            equip(1)
                        elif d == 'b':
                            text_(Shop_Descriptions[your_inventory[1]])
                            input_needed = True
                            user_input(("Press 'y' to use this item, ","'a' to equip " + your_inventory[0] + ", ","'c' to equip " + your_inventory[2] + ", or ","'enter' to continue without using an item."))
                            if d == 'y':
                                equip(1)
                            elif d == 'a':
                                equip(0)
                            elif d == 'c':
                                equip(2)
                            else:
                                text_(("Okay, maybe next time!","","",""))
                        elif d == 'c':
                            equip(2)
                        else:
                            text_(("Okay, maybe next time!","","",""))
                    elif d == 'b':
                        text_(Shop_Descriptions[your_inventory[1]])
                        input_needed = True
                        user_input(("Press 'y' to use this item, ","'a' to view or use " + your_inventory[0] + ", ","'c' to equip " + your_inventory[2] + ", or ","'enter' to continue without using an item."))
                        if d == 'y':
                            equip(1)
                        elif d == 'a':
                            text_(Shop_Descriptions[your_inventory[0]])
                            input_needed = True
                            user_input(("Press 'y' to use this item, ","'b' to equip " + your_inventory[1] + ", ","'c' to equip " + your_inventory[2] + ", or ","'enter' to continue without using an item."))
                            if d == 'y':
                                equip(0)
                            elif d == 'b':
                                equip(1)
                            elif d == 'c':
                                equip(2)
                            else:
                                text_(("Okay, maybe next time!","","",""))
                    else:
                        text_(("Okay, maybe next time!","","",""))
                else:
                    text_(("Okay, maybe next time!","","",""))
        else:
            text_(("Okay, maybe next time!","","",""))
def startgame():
    global d
    global gamestart
    global input_needed
    global name
    global g
    global screen
    global font
    global start
    global ratio
    global size
    global center
    global tutorial
    pygame.init()
    screen = pygame.display.set_mode()
    size = pygame.display.get_window_size()
    ratio = []
    ratio.append(int(size[0]/1536))
    ratio.append(int(size[1]/846))
    center = []
    center.append(int(size[0]/2))
    center.append(int(size[1]/2))
    font = pygame.font.SysFont(None, (60*ratio[1]))
    input_needed = False
    text_((("Welcome to Time-Traveling Kangaroo","","","Press 'enter' at any time to continue")))
    user_name()
    input_needed = False
    text_(("Welcome, " + str(name) + "!","","","Press 'enter' at any time to continue"))
    input_needed = True
    user_input(("Would you like to view the tutorial?","","Press 'a' to to view tutorial,","or press 'enter' to start the game"))
    if d == ' ':
        gamestart = True
        playgame()
    elif d == 'a':
        tutorial = True
        Tutorial(1)
        gamestart = True
        playgame()
def playgame():
    global current_space
    global d
    global input_needed
    while current_space <=40:
        item()
        if wheel == True:
            q = 0
            input_needed = True
            num_input()
            if d > 0:
                if d == 1:
                    text_(("Kangaroo moves " + str(d) + " space forward."),"","","")
                else:
                    text_(("Kangaroo moves " + str(d) + " spaces forward."),"","","")
                while q < d:
                    current_space += 1
                    q += 1
                    shop()
            if d < 0:
                d = abs(d)
                if d == 1:
                    text_(("Kangaroo moves " + str(d) + " space back."),"","","")
                else:
                    text_(("Kangaroo moves " + str(d) + " spaces back."),"","","")
                while q < d:
                    current_space -= 1
                    q += 1
                    shop()
        input_needed = False
        text_(("Press 'enter' to pick a card.","","",""))
        roll()
        cash()
        if card_space[pick] < 0:
            flop()
        elif card_space[pick] > 0:
            hop()
        else:
            text_(("You do not move.","","",""))
        text_(("You are now on space " + str(current_space) + ".","","",""))
    endgame()
def endgame():
    global input_needed
    text_(("Whoohoo! You finished! You made it to the end of time. ","Now you can sit back, relax, and watch the world burn.","",""))
    input_needed = True
    user_input(("Would you like to play again?","","To play again, press 'y'.","To end the game, press the 'enter' key."))
    if d == 'y':
        global current_space
        global KangaCash
        global your_inventory
        current_space = 0
        KangaCash = 20
        your_inventory = {}
        playgame()
    else:
        text_(("Goodbye! See you next time!","","",""))
startgame()