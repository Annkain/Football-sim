#Football Menager Game
from random import randint
from time import sleep
from os import system, name
def PitchClearGraph():
  global line1, line2, line3, line4, line5, line6, line7, line8, line9, line10, line11, line12, line13, line14, line15, line16, line17
  line1 =  ('------------------------------------------------------------------------------------')
  line2 =  ('|                                        |                                         |')
  line3 =  ('|                                        |                                         |')
  line4 =  ('|----------                              |                               ----------|')
  line5 =  ('|         |                            --|--                             |         |')
  line6 =  ('|         |                         -    |    -                          |         |')
  line7 =  ('|-        |-                      -      |      -                       -|        -|')
  line8 =  ('| |       | -                   -        |        -                    - |       | |')
  line9 =  ('| |       |  -                 -         o         -                  -  |       | |')
  line10 = ('| |       | -                   -        |        -                    - |       | |')
  line11 = ('|-        |-                      -      |      -                       -|        -|')
  line12 = ('|         |                         -    |    -                          |         |')
  line13 = ('|         |                            --|--                             |         |')
  line14 = ('|----------                              |                               ----------|')
  line15 = ('|                                        |                                         |')
  line16 = ('|                                        |                                         |')
  line17 = ('------------------------------------------------------------------------------------')
PitchClearGraph()
def Print_Pitch():
  print ('                 ',teamHome, scoreHome,'         :       ',scoreAway, teamAway)
  if ballPosesion == teamHome:
    print(' =======================================')
  else:
    print('                                           =======================================')
  print('                                      ',timer,'min')
  print(line1)       #football pitch
  print(line2)
  print(line3)
  print(line4)
  print(line5)
  print(line6)
  print(line7)
  print(line8)
  print(line9)
  print(line10)
  print(line11)
  print(line12)
  print(line13)
  print(line14)
  print(line15)
  print(line16)
  print(line17)   


teamRatingHome = 0  # home team odds f.e. from livescore.com

teamRatingAway = 15  # away team odds f.e. from livescore.com
teamHomeScore = (15 - teamRatingHome) *2
teamAwayScore = (15 - teamRatingAway) *2
shootChance = 50  #percentage chanc e to hoot
hitChance = 50
shootAttempt = None  # randomize chance to shoot from your position, if > than shootChance then footballer shoots
saveChance = 40  # percentage chance to save a shoot
saveAttempt = None  # randomize chance to save a shoot, if > than saveChance than shoot is saved
textWhere = ''
textZone = ''
text3 = ''
textTimer = ''
text = 0
ballMove = 2
startingBallMove = 2
matchHalfLenght = 45  #first half time
timeSecondHalf = 45  #second thalf time
teamHome = 'Real Madryt'
teamAway = 'Liverpol FC'
ballPosesion = teamHome
ballNotPossesion = teamAway
playTest = None
extraTime = randint(2,4)
extraTime2 = randint(3,8)
pitchZone = [
    teamHome+' Penalty area', 'Defensive third of '+teamHome, teamHome+' Half', 'Middle third', teamAway+' Half', 'Defensive thirf of '+teamAway, teamAway+' Penalty area'
]
secondHalf = False
timer = 0
ballPosition = 3
playChance = 85
scoreHome = 0
scoreAway = 0
possesionChange = None
goalScored = False
firstHalf = True
goals = [] 
ballGraph = '@'
skipSomeIf = False # this variable helps to skip loops after goal
skipFirstIf = False


def clear():
  _ = system('clear')

def time():
  global timer, matchHalfLenght
  
  #sleep(1)
  timer += 1
  #clear()
  matchHalfLenght -= 1
def Goal():
  global line1, line2, line3, line4, line5, line6, line7, line8, line9, line10, line11, line12, line13, line14, line15, line16, line17
  line1 =  ('------------------------------------------------------------------------------------')
  line2 =  ('|                                        |                                         |')
  line3 =  ('|           ggggggg            ooooo     |  AAAAAAAAA       L              ##      |')
  line4 =  ('|---------g         g        o       o   | A         A      L            --##------|')
  line5 =  ('|        g|                o           o-|-A         A      L            | ##      |')
  line6 =  ('|       g |                o        -  o | A  -      A      L            | ##      |')
  line7 =  ('|-      g |-               o      -    o | A    -    A      L           -| ##     -|')
  line8 =  ('| |     g | -              o    -      o | A      -  A      L          - | ##    | |')
  line9 =  ('| |     g |  -             o   -       o o AAAAAAAAAAA      L         -  | ##    | |')
  line10 = ('| |     g | - gggggggg     o    -      o | A      -  A      L          - | ##    | |')
  line11 = ('|-      g |-         g     o      -    o | A    -    A      L           -|        -|')
  line12 = ('|       g |         g      o        -  o | A  -      A      L            |         |')
  line13 = ('|         g        g        o        o --|-A         A      L            | ##      |')
  line14 = ('|---------- gggggg            ooooooo    | A         A      LLLLLLLLLLLL --##------|')
  line15 = ('|                                        |                                         |')
  line16 = ('|                                        |                                         |')
  line17 = ('------------------------------------------------------------------------------------')
  return


xMin = 41
xMax = 41
yMin = 9
yMax = 9
goalkeeperCatched = False
while matchHalfLenght > 0:
  skipSomeIf = False # means that no goal yet
  if timer == 0 and firstHalf or timer == 45 and secondHalf:
    line9 =  ('| |       |  -                  -        @         -                  -  |       | |')
    Print_Pitch()
    line9 =  ('| |       |  -                  -        o         -                  -  |       | |')
    if firstHalf:
      print('We start the match between ',teamHome,' and ',teamAway,'!')
      print('The match will be started by the host team')
    if secondHalf:
      print(teamAway,' starts the second half!')
      ballPosesion = teamAway
      ballNotPossesion = teamHome
    sleep(5)
      
  clear()
  
  
 

  
  
  
  
  
  playTest = randint(1,100)
  
  if ballPosesion == teamHome:
    teamsRating = teamHomeScore
    ballNotPossesion = teamAway
  else:
    ballNotPossesion = teamHome
    teamsRating = teamAwayScore
  #print(playChance,teamsRating, playTest)
  
                                            #rozgrywka

 
  if goalScored is True:
    print(ballPosesion,' starts the game from the middle')
    possesionChange = True
    goalScored = False
    skipFirstIf = True
    skipSomeIf = True
    time()
  #print(ballPosition,'                                 POZYCJA')
  if (ballPosition == 0 and ballPosesion == teamAway) or (ballPosition == 6 and ballPosesion == teamHome) and skipFirstIf is False:
      Print_Pitch()
      if (shootChance + teamsRating) >= playTest:
        print(ballPosesion,'Shooooooots!')
        sleep(1)
        playTest = randint(1,100)
        if (hitChance + teamsRating) >= playTest:
          playTest = randint(1,100)
          
          if ballPosesion == teamHome :
            saveChance += teamHomeScore
          else:
            saveChance += teamAwayScore
          #print('je??li ',saveChance,' jest wi??ksze od ',playTest,' to gol')      shoot test
          if saveChance >= playTest:
            for blink in range(10):
              clear()
              Goal()
              Print_Pitch()
              sleep(0.3)
              clear()
              PitchClearGraph()
              Print_Pitch()
              Goal()
              sleep(0.3)
              
            PitchClearGraph()
            clear()
            
            goal = ballPosesion +'',str(timer)
            
            goals.append(goal)
            goalScored = True
            ballPosition = 3
            skipSomeIf = True # skips next if's from 120 line
            saveChance = 40
            if ballPosesion == teamHome:
              scoreHome += 1
             
            else:
              scoreAway += 1
              
            
            ballPosesion = ballNotPossesion
            
            
            
            time()
            
              
          else:
            print('Goalkeeper of',ballNotPossesion,'catches the ball')
            print('The goalkeeper starts with a goal kick')
            sleep(3)
            goalkeeperCatched = True
            ballPosition = 3
            skipSomeIf = True
            time()
        else:
          print('Ball misses the goal')
          print('The goalkeeper starts with a goal kick')
          sleep(3)
          ballPosition = 3
          skipSomeIf = True
          time()
          
            
      else:
        playTest = randint(1,100)
        if playTest > 50 :
          text3 = (ballNotPossesion,' kicks the ball away!' )
          ballPosition = 3
        elif playTest <= 50 :
          textZone = (ballPosesion,'loses the ball,',ballNotPossesion,' takes it')
          ballPosesion = ballNotPossesion
          
          
          possesionChange = True
          skipSomeIf = True
          playChance = 85 
          
          time()
  #print(teamsRating+playChance, teamHomeScore, teamAwayScore)
  clear()
  if (playChance + teamsRating) >= playTest and skipSomeIf is False and skipFirstIf is False:
    if ballPosition == 3:
      playChance = 85
    elif ballPosition == 2 or ballPosition == 4:
      playChance = 65
    elif ballPosition == 1 or ballPosition == 5:
      playChance = 40
    elif possesionChange is True:
      playChance = 70
    possesionChange = False
    if ballPosesion == teamAway:
      ballPosition -= 1
    else:
      ballPosition += 1
    
    

      
    textZone = (ballPosesion,'moves to',pitchZone[ballPosition])
    playChance -= 20
    playTest = randint(1,100)
    time()
  
  else :
    if skipSomeIf is False:
      textZone = (ballPosesion,'loses the ball,',ballNotPossesion,' takes it')
      ballPosesion = ballNotPossesion
      
      
      possesionChange = True
      playChance = 85
      time()
  
  
  

  
                                              #ball movement
  while ballMove > 1:
    #sleep(2)
    
    if ballPosition == 3 :
      xMin = 35
      xMax = 47
    elif ballPosition == 2:
      xMin = 20
      xMax = 35
    elif ballPosition == 1:
      xMin = 11
      xMax = 20
    elif ballPosition == 0:
      xMin = 3
      xMax = 11
    elif ballPosition == 4:
      xMin = 45
      xMax = 62
    elif ballPosition == 5:
      xMin = 63
      xMax = 73
    elif ballPosition == 6:
      xMin = 74
      xMax = 78
    if ballMove == startingBallMove:
      xx = randint(xMin,xMax)
      yy = randint(yMin,yMax)
    if goalScored is True or (secondHalf and timer == 45) :
      x = 41
      y = 9
    else:
      x = randint(xx-2,xx+2)
      y = randint(yy-5,yy+5)
    
      
    
    if y > 17: 
      y = 15
    if y < 2:
      y = 3
  
    
    if goalkeeperCatched == True :
      x = 80
      y = 9
  
  
  
    if y == 2:
      line2 = line2[:x] + ballGraph + line2[x+1:]
    elif y == 3:
      line3 = line3[:x] + ballGraph + line3[x+1:]
    elif y == 4:
      line4 = line4[:x] + ballGraph + line4[x+1:]
    elif y == 5:
      line5 = line5[:x] + ballGraph + line5[x+1:]
    elif y == 6:
      line6 = line6[:x] + ballGraph + line6[x+1:]
    elif y == 7:
      line7 = line7[:x] + ballGraph + line7[x+1:]
    elif y == 8:
      line8 = line8[:x] + ballGraph + line8[x+1:]
    elif y == 9:
      line9 = line9[:x] + ballGraph + line9[x+1:]
    elif y == 10:
      line10 = line10[:x] + ballGraph + line10[x+1:]
    elif y == 11:
      line11 = line11[:x] + ballGraph + line11[x+1:]
    elif y == 12:
      line12 = line12[:x] + ballGraph + line12[x+1:]
    elif y == 13:
      line13 = line13[:x] + ballGraph + line13[x+1:]
    elif y == 14:
      line14 = line14[:x] + ballGraph + line14[x+1:]
    elif y == 15:
      line15 = line15[:x] + ballGraph + line15[x+1:]
    elif y == 16:
      line16 = line16[:x] + ballGraph + line16[x+1:]
    ballMove -= 1
    #sleep(10)
    clear()
    Print_Pitch()
    if goalScored is True:
      print(ballPosesion,' starts the game from the center of the pitch')
    if timer == 45 and firstHalf:
    
      matchHalfLenght += extraTime
      print("We gonna play for ",extraTime,'minutes more!')
    if timer == 45+extraTime and firstHalf:
      print('First half result:\n ',teamHome, scoreHome,'\n',teamAway, scoreAway)
      print(goals)
      sleep(3)
      print('Lets start the second half')
      sleep(1)
      clear()
      secondHalf = True
      firstHalf = False
      timer = 45
      matchHalfLenght = 45
    
    
    if timer == 90:
      matchHalfLenght += extraTime2
      print("We gonna play for ",extraTime,'minutes more!')
    
    #if goalkeeperCatched is False and goalScored is False and skipFirstIf is False
    if timer != (45 and secondHalf) or timer != (timer+extraTime and firstHalf): 
      if not goalScored:
        print(' '.join(textZone))
    #if skipFirstIf is False and goalScored is False:
      print('Current ball position:',pitchZone[ballPosition])
      print(' '.join(text3))
    if timer == 0:
      print(teamHome,'starts the game from the center of the pitch')
    
    
    PitchClearGraph()
    if ballMove != 1:
      clear()
  ballMove = startingBallMove
  text3 = ''
  goalkeeperCatched = False
  skipFirstIf = False
  
  #Print_Pitch()
  sleep(0.5)

print("The referee's last whistle!!! ")
print('Final result:\n ',teamHome, scoreHome,'\n',teamAway, scoreAway)
print(goals)
 

