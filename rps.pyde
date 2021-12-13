import random

def setup():
    global lost, won, ultimate_winner, score, compscore, tie, intro, rock, paper, scissors, ring, rock_info, paper_info, scissors_info, rock_clicked, paper_clicked, scissors_clicked, scissorsplay, paperplay, rockplay, rockcomp, papercomp, scissorscomp, new_game, moves_comp, moves_human, compmove, humanmove, introimage
    
    size(800, 430)
    #sets screen size 
    
    introimage = loadImage("RPS.png")
    ring = loadImage("ring.png")
    rock = loadImage("rock.png")
    scissors = loadImage("scissors.png")
    rockplay = loadImage("rockplay.png")
    scissorsplay = loadImage("scissorsplay.png")
    paperplay = loadImage("paperplay.png")
    paper = loadImage("paper.png")
    rockcomp = loadImage("rockcomp.png")
    papercomp = loadImage("papercomp.png")
    scissorscomp = loadImage("scissorscomp.png")
    lost = loadImage("lost.png")
    won = loadImage("won.png")
    #loads all the images 
    
    ultimate_winner = 0
    compmove = random.randint(0,2)
    humanmove = None
    new_game = False
    intro = True
    compscore = 0
    score = 0 
    tie = 0
    #loads the varriables 
    moves_human = [rockplay, paperplay, scissorsplay]
    moves_comp = [rockcomp, papercomp, scissorscomp]
    rock_info = [ 120, 280, 100, 150] 
    paper_info = [ 250, 275, 100, 150] 
    scissors_info = [ 400, 275, 100, 150]
    #loads the nessecary lists 
   
def draw():
    global intro, ultimate_winner
    
    if intro == True:
        introscreen()
    #draws the intro screen if intro is set to true
    
    elif intro == False and ultimate_winner == 0:
        gameplay()
        scoreboard()
        showplay_hum()
        showplay_comp()
        nextbutton()
        whowon()
        #if intro isnt true and there is no winner play the game 
    
    elif ultimate_winner != 0:
        endscreen()
    #if there is a winner draw the end screen

    
def gameplay():
    global rock, paper, scissors, ring 
    fill(255)
    rect(0, 0, 800, 430)
    fill(0)
    textSize(32)
    text("You", 50, 30)
    text("Opponent", 500, 30)
    image(ring, 0, 40, 600, 250)
    image(rock, 120, 280, 100, 150)
    image(paper, 250, 275, 100, 150)
    image(scissors, 400, 275, 100, 150 )
    #draws the gampelay ( all the photos and everything you see when your playing)
    
    
def scoreboard():
    global score, xscore, tie
    fill(203,195,227)
    rect(600,0,800,430)
    fill(0)
    textSize(20)
    textAlign(CENTER)
    text("Your Score: %i" %(score), 690,150)
    text("Ties: %i" %(tie), 690,250)
    textSize(18)
    text("Computer Score: %i" %(compscore), 690,200)
    #draws the scoreboard that you see when your playing to the left of the screen
    
def endscreen():
    global ultimate_winner, lost, won
    
    if ultimate_winner != 0:
        fill(0)
        background(255,182,193)
        text("Press Space to Reset",400,400)
        textSize(40)
        fill(0)
        textAlign(CENTER)
    if ultimate_winner == 1:
        text("You Lost", 400,50)
        image(lost,250,150, width/3, height/2)
    #draws a screen that has a sad face and says you lost if the computer won the game
    
    elif ultimate_winner == 2:
        text("You Won", 400,50)
        image(won,200,100, width/2, height/2)
    #draws a screen that says you won and has a image if you won the whole game
        
            
    

def introscreen():
    global introimage
    background(255,182,193)
    #sets the background to pink

    
    fill(231,84,128)
    rect(550,370,225,50)
    textAlign(CENTER,CENTER)
    textSize(30)
    fill(0)
    text("Press to start",662.5,395)
    #draws the button that you can press to start the game 
    
    textSize(40)
    fill(0)
    textAlign(CENTER)
    text("Rock Paper Scissors", 400,50)
    textSize(20)
    text("First to 3 wins",400,260)
    text("Press Right Arrow To Start a New Round or Click The Button", 400, 300)
    text("Press Space to Reset the Whole Game", 400, 350)
    textSize(35)
    image(introimage, 255,75, width/3, height/3) 
    #draws intro screen with instructions 
    

def showplay_hum():
    global humanmove, moves_human
    if humanmove != None:
        image(moves_human[humanmove],80, 40, 200, 150)
    #draws the players rock, paper or scissors based on what the player picks  
 
    
    
def showplay_comp():
    global moves_comp, compmove, humanmove
    if humanmove != None:
        image(moves_comp[compmove], 300, 40, 200, 150)
    #draws the computers pick once the player makes their choice 

def whowon():
    #checks who won each game and if anyone won the whole game 
    global tie,score, compscore, compmove, humanmove, new_game, ultimate_winner
    if new_game == False: 
        
        if humanmove == 0:
            if compmove == 0:
                tie += 1
                new_game = True
            elif compmove == 1:
                compscore += 1
                new_game = True
            else:
                score +=1
                new_game = True
        #check who won when player picked rock
        
                
        elif humanmove == 1:
            if compmove == 0:
                score +=1
                new_game = True
                
            elif compmove == 1:
                tie += 1
                new_game = True
                
            else:
                compscore += 1
                new_game = True
        #check who won when player picked paper

    
                
        elif humanmove == 2:
            if compmove == 0:
                compscore +=1
                new_game = True
                
            elif compmove == 1:
                score += 1
                new_game = True
            else:
                tie += 1
                new_game = True
        #check who won when player picked scissors
                
    if compscore == 3:
        ultimate_winner = 1
    if score == 3:
        ultimate_winner = 2 
#check if anyone has won the game(if anyone has 3 wins)
    
    
def reset():
    global new_game, compmove, humanmove
    compmove = random.randint(0,2)
    humanmove = None
    new_game = False
    #resets the gameboard and randomly selects a computer pick
    
    
def fullreset():
    global ultimate_winner, score, compscore, tie, intro, new_game, compmove, humanmove
    ultimate_winner = 0
    compmove = random.randint(0,2)
    humanmove = None
    new_game = False
    intro = True
    compscore = 0
    score = 0 
    tie = 0
    #resets everything for when you want to start a new game

    
def nextbutton():
    global humanmove
    if humanmove != None:
        fill(128,128,128)
        rect(620,325,150,75)
        fill(255)
        textAlign(CENTER,CENTER)
        textSize(15)
        text("Click for Next Game", 695,362.5)
    #draws a button you can click for the next round
        
def mousePressed():
    global rock_info, paper_info, scissors_info, scissorsplay, paperplay, rockplay, rockcomp, papercomp, scissorscomp, compmove,new_game, humanmove, ultimate_winner,intro
    #(550,370,225,50)
    if intro == True:
        if mouseX > 550 and mouseX<775 and mouseY>370 and mouseY<420:
            intro = False
    #makes the button on the intro screen clickable 
    
    if humanmove == None and intro == False and ultimate_winner == 0:
        if mouseX > rock_info[0] and mouseX < rock_info[0] + rock_info[2] and mouseY > rock_info[1] and mouseY < rock_info[1] + rock_info[3]:
            humanmove = 0
        #makes the rock button clickable
        
        if mouseX > paper_info[0] and mouseX < paper_info[0] + paper_info[2] and mouseY > paper_info[1] and mouseY < paper_info[1] + paper_info[3]:
            humanmove = 1
        #makes the paper button clickable
            
        if mouseX > scissors_info[0] and mouseX < scissors_info[0] + scissors_info[2] and mouseY > scissors_info[1] and mouseY < scissors_info[1] + scissors_info[3]:
            humanmove = 2
        #make the scissors button clickable 
        
        
    if humanmove != None and intro == False and ultimate_winner == 0:
        if mouseX>620 and mouseX<770 and mouseY>325 and mouseY<400:
            reset()
    #makes button on gameboard to go to the next game 
        

def keyPressed():
    global intro 

    if intro == True: 
        if key == CODED:
            if keyCode == RIGHT:
                intro = False 
    #if right arrow is clicked you move on from the intro
    elif intro == False:
        if key == CODED:
            if keyCode == RIGHT:
                reset()
    #if right arrow is clicked and introscrren isnt showing you move on to the next round
    if key == " ":
        fullreset()
    #if space is clicked a full reset happens 
