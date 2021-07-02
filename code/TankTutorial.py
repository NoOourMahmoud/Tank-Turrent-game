import pygame
import random

pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (200,0,0)
light_red = (255,0,0)
yellow = (200,200,0)
light_yellow = (255,255,0)
green = (0,155,0)
light_green = (0,255,0)		

display_width = 800
display_hight = 600
gameDisplay = pygame.display.set_mode((display_width,display_hight))

pygame.display.set_caption('Tanks')

fire_sound = pygame.mixer.Sound("ray_gun-Mike_Koenig-1169060422.wav")		
explosion_sound = pygame.mixer.Sound("Fire Crackers-SoundBible.com-1716803209.wav")		
power_sound = pygame.mixer.Sound("Ball_Bounce-Popup_Pixels-172648817.wav")
win_sound = pygame.mixer.Sound("Kids Cheering-SoundBible.com-681813822.wav")
lose_sound = pygame.mixer.Sound("Sad_Trombone-Joe_Lamb-665429450.wav")

pygame.mixer.music.load("Ta Da-SoundBible.com-1884170640.wav")			
pygame.mixer.music.play(1)															

clock = pygame.time.Clock()
		
tankWidth = 40		
tankHeight = 20		

turretWidth = 5		
wheelWidth = 5

ground_height = 35	

FPS = 15


smallfont = pygame.font.SysFont("comicsansms" , 25)   
medfont = pygame.font.SysFont("comicsansms" , 50) 
semimedfont = pygame.font.SysFont("comicsansms" , 35) 
largefont = pygame.font.SysFont("comicsansms" , 80) 

def text_to_button(msg , color , buttonx , buttony , buttonwidth , buttonheight , size = "small"): 
	if size == "small":	
    		textSurface = smallfont.render(msg, True , color)
	if size == "med":	
    		textSurface = medfont.render(msg, True , color)
    	if size == "large":	
    		textSurface = largefont.render(msg, True , color)
    	if size == "semimed":	 			
    		textSurface = semimedfont.render(msg, True , color)
    	textRect = textSurface.get_rect()
    	textRect.center = ((buttonx+(buttonwidth/2)) , (buttony+(buttonheight/2)))
    	gameDisplay.blit(textSurface , textRect)

def message_to_screen(msg,color,y_displace = 0,size = "small"):
	if size == "small":	
    		textSurface = smallfont.render(msg, True , color)
	if size == "med":	
	    	textSurface = medfont.render(msg, True , color)
	if size == "large":	
	    	textSurface = largefont.render(msg, True , color)
	if size == "semimed":	 			
	    	textSurface = semimedfont.render(msg, True , color)
	textRect = textSurface.get_rect()
	textRect.center = (display_width / 2) , (display_hight / 2) + y_displace 
	gameDisplay.blit(textSurface , textRect)

def tank(x,y, turPos):		
	x = int(x)		
	y = int(y)
	
	possibleTurrets = [(x-27,y-2), (x-26,y-5), (x-25,y-8), (x-23,y-12),	
	(x-20,y-14), (x-18,y-15), (x-15,y-17), (x-13,y-19), (x-11,y-21)]
			
	pygame.draw.circle(gameDisplay, black, (x,y), tankHeight/2)			
	pygame.draw.rect(gameDisplay, black , (x-tankHeight, y, tankWidth, tankHeight))	
	pygame.draw.line(gameDisplay, black, (x,y), possibleTurrets[turPos] , turretWidth)			
	
	startX = 15
	for i in range(7):
		pygame.draw.circle(gameDisplay, black, (x-startX, y+20), wheelWidth)
		startX -= 5
		
	return possibleTurrets[turPos]


def enemy_tank(x,y, turPos):
	x = int(x)		
	y = int(y)
	
	possibleTurrets = [(x+27,y-2), (x+26,y-5), (x+25,y-8), (x+23,y-12),	
	(x+20,y-14), (x+18,y-15), (x+15,y-17), (x+13,y-19), (x+11,y-21)] 
			
	pygame.draw.circle(gameDisplay, black, (x,y), tankHeight/2)			
	pygame.draw.rect(gameDisplay, black , (x-tankHeight, y, tankWidth, tankHeight))	
	pygame.draw.line(gameDisplay, black, (x,y), possibleTurrets[turPos] , turretWidth)			
	
	startX = 15
	for i in range(7):
		pygame.draw.circle(gameDisplay, black, (x-startX, y+20), wheelWidth)
		startX -= 5
		
	return possibleTurrets[turPos]


def game_controls():  
	gcont = True		
	gameDisplay.fill(white)
	
	
	message_to_screen("Controls" , green , -100 , "large")
	message_to_screen("Fire: Spacebar" , black , -30)
	message_to_screen("Move Turrent: Up and Down arrows" , black , 10)
	message_to_screen("Move Tank: Left and Right arrows" , black , 50) 
	message_to_screen("Pase: P" , black , 90)

	
	while gcont:	
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			
			
		cur = pygame.mouse.get_pos()	
	
		click = pygame.mouse.get_pressed()	
	
		if 350 > cur[0] > 150 and 535 > cur[1] > 500:	
			pygame.draw.rect(gameDisplay , light_yellow , (150,500,200,35)) 
			if click[0] == 1: 		
				game_intro()
		else:
			pygame.draw.rect(gameDisplay , yellow , (150,500,200,35))
		
		text_to_button("Main" , black , 150 , 500 , 200 , 35)
		pygame.display.update()
	

def button(text , x , y , width , height , inactive_color , active_color , action = None): 
	cur = pygame.mouse.get_pos()
	
	click = pygame.mouse.get_pressed()	
	
	if x+width > cur[0] > x and y+height > cur[1] > y:	
		pygame.draw.rect(gameDisplay , active_color , (x,y,width,height)) 
		if click[0] == 1 and action != None: 		
			if action == "play":		
				gameLoop()		
			elif action == "controls":	
				game_controls()			
			elif action == "quit":		
				pygame.quit()		
				quit()	
			elif action == "main":
				game_intro()	
	else:
		pygame.draw.rect(gameDisplay , inactive_color , (x,y,width,height))
		
	text_to_button(text , black , x , y , width , height)

def barrier(xlocation, randomHeight, barrier_width):
	pygame.draw.rect(gameDisplay, black, [xlocation, display_hight-randomHeight, barrier_width, randomHeight])
	

def explosion(x , y):
	pygame.mixer.Sound.play(explosion_sound)		
	explode = True
	
	while explode:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		startPoint = x,y
		
		colorChoices = [red, light_red, yellow, light_yellow]
		
		magnitude = 1
		while magnitude < 50:
			exploding_bit_x = x +random.randrange(-1*magnitude, magnitude)
			exploding_bit_y = y +random.randrange(-1*magnitude, magnitude)
			pygame.draw.circle(gameDisplay, colorChoices[random.randrange(0,4)] , (exploding_bit_x, exploding_bit_y), random.randrange(1, 5))
			magnitude+= 1
			
			pygame.display.update()
			clock.tick(100)
			
		explode = False

def fireSell(xy, tankX, tankY, turPos, gun_power, xlocation, barrier_width, randomHeight, enemyTankX, enemyTankY): 
	pygame.mixer.Sound.play(fire_sound)			
	fire = True
	damage = 0	
	
	startingSell = list(xy)
	
	while(fire):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		pygame.draw.circle(gameDisplay, green,(startingSell[0], startingSell[1]), 5)
		
		startingSell[0] -= (12-turPos)*2 

		startingSell[1] += int((((startingSell[0]-xy[0]) * 0.015/(gun_power/50.0)) ** 2) - (turPos+turPos/(12-turPos))) 
		
		if startingSell[1] > display_hight - ground_height: 			
			hit_x = int((startingSell[0]))
			hit_y = int(display_hight - ground_height)
			
			
			if enemyTankX + 10 > hit_x > enemyTankX - 10:	
				damage = 25 
			elif enemyTankX + 15 > hit_x > enemyTankX - 15:	
				damage = 18 
			elif enemyTankX + 25 > hit_x > enemyTankX - 25:	
				damage = 10
			elif enemyTankX + 35 > hit_x > enemyTankX - 35:	
				damage = 5
			
			
			explosion(hit_x, hit_y)	
			  
			fire = False
			
		check_x_1 = startingSell[0] >= xlocation		
		check_x_2 = startingSell[0] <= xlocation+barrier_width	
		
		check_y_1 = startingSell[1] >= display_hight-randomHeight	
		check_y_2 = startingSell[1] <= display_hight			
		
		if check_x_1 and check_x_2 and check_y_1 and check_y_2:
			
			hit_x = int(startingSell[0])
			hit_y = int(startingSell[1])
			
			explosion(hit_x, hit_y)	
			  
			fire = False
		
		pygame.display.update()
		clock.tick(60)
		
	return damage		


def e_fireSell(xy, tankX, tankY, turPos, gun_power, xlocation, barrier_width, randomHeight, ptankx, ptanky): 	
	pygame.mixer.Sound.play(fire_sound)			
	damage = 0				
	currentPower = 1
	power_found = False
	
	
	while not power_found:
		if currentPower > 100:	
			power_found = True
			
		currentPower += 1
		

		fire = True
		startingSell = list(xy)
	
		while(fire):
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					quit()
		
			startingSell[0] += (12-turPos)*2 

			startingSell[1] += int((((startingSell[0]-xy[0]) * 0.015/(currentPower/50.0)) ** 2) - (turPos+turPos/(12-turPos)))       	
		
			if startingSell[1] > display_hight - ground_height: 
				hit_x = int((startingSell[0]))
				hit_y = int(display_hight - ground_height)  

				if ptankx+30 > hit_x > ptankx-20:		
					power_found = True 
				fire = False
			
			check_x_1 = startingSell[0] >= xlocation		
			check_x_2 = startingSell[0] <= xlocation+barrier_width	
		
			check_y_1 = startingSell[1] >= display_hight-randomHeight	
			check_y_2 = startingSell[1] <= display_hight			
		
			if check_x_1 and check_x_2 and check_y_1 and check_y_2:
				hit_x = int(startingSell[0])
				hit_y = int(startingSell[1])

				fire = False
			
	
	fire = True
	startingSell = list(xy)
	
	while(fire):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

		pygame.draw.circle(gameDisplay, green,(startingSell[0], startingSell[1]), 5)
		
		
		startingSell[0] += (12-turPos)*2 

		gun_power = random.randrange(int(currentPower*0.9), int(currentPower*1.1))
		
		startingSell[1] += int((((startingSell[0]-xy[0]) * 0.015/(gun_power/50.0)) ** 2) - (turPos+turPos/(12-turPos))) 
		
		if startingSell[1] > display_hight - ground_height: 
			hit_x = int((startingSell[0]))
			hit_y = int(display_hight - ground_height)  
			
			
			
			if ptankx + 10 > hit_x > ptankx - 10:		
				damage = 25 
			elif ptankx + 15 > hit_x > ptankx - 15:			
				damage = 18 
			elif ptankx + 25 > hit_x > ptankx - 25:			
				damage = 10
			elif ptankx + 35 > hit_x > ptankx - 35:			
				damage = 5
		
				
			explosion(hit_x, hit_y)	
			  
			fire = False
			
		check_x_1 = startingSell[0] >= xlocation		
		check_x_2 = startingSell[0] <= xlocation+barrier_width	
		
		check_y_1 = startingSell[1] >= display_hight-randomHeight	
		check_y_2 = startingSell[1] <= display_hight			
		
		if check_x_1 and check_x_2 and check_y_1 and check_y_2:
			
			hit_x = int(startingSell[0])
			hit_y = int(startingSell[1])
			
			explosion(hit_x, hit_y)	
			  
			fire = False
		
		pygame.display.update()
		clock.tick(60)

	return damage			


def power(level):
	text = smallfont.render("Power: "+str(level)+"%", True, black)
	gameDisplay.blit(text, [display_width/2, 0])

		
def game_intro():  
	
	intro = True
	gameDisplay.fill(white)
	
	message_to_screen("Welcom to Tanks" , green , -100 , "large")
	message_to_screen("The objective is to shoot and distroy" , black , -30)
	message_to_screen("The the enemy befor they destroy you" , black , 10)
	message_to_screen("The more enemies you distroy, the harder they get" , black , 50) 
	
	while intro:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_q:
					pygame.quit()
					quit()
				if event.key == pygame.K_c:
					intro = False
		
		button("Play" , 150,500,100,50 , green , light_green , "play")			
		button("Controls" ,350,500,100,50 , yellow , light_yellow , "controls")		
		button("Quit" , 550,500,100,50 , red , light_red , "quit")
		
		pygame.display.update()


def game_over():  
	
	pygame.mixer.Sound.play(lose_sound)
	game_over = True   
	gameDisplay.fill(white)
	
	message_to_screen("Game Over" , green , -100 , "large")			
	message_to_screen("You died." , black , -30)					
	
	while game_over:		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		
		button("Play Again" , 150,500,100,50 , green , light_green , "play")			
		button("Controls" ,350,500,100,50 , yellow , light_yellow , "controls")		
		button("Quit" , 550,500,100,50 , red , light_red , "quit")
		
		pygame.display.update()


def you_win(): 
	
	pygame.mixer.Sound.play(win_sound)
	win = True   		
	gameDisplay.fill(white)
	
	message_to_screen("You won!" , green , -100 , "large")		
	message_to_screen("Congratulations ^^" , black , -30)	
	
	while win:				
		for event in pygame.event.get():
                	if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			
		
		button("Play Again" , 150,500,100,50 , green , light_green , "play")			
		button("Controls" ,350,500,100,50 , yellow , light_yellow , "controls")		
		button("Quit" , 550,500,100,50 , red , light_red , "quit")
		
		pygame.display.update()


def score(score):
	text = smallfont.render("score: " + str(score) , True , black)
	gameDisplay.blit(text , [0,0])   
    

def health_bars(player_health, enemy_health):	
	if player_health > 75:
		player_health_color = green
	elif player_health > 50:
		player_health_color = yellow
	else:
		player_health_color = red
		
	if enemy_health > 75:
		enemy_health_color = green
	elif enemy_health > 50:
		enemy_health_color = yellow
	else:
		enemy_health_color = red
		
	pygame.draw.rect(gameDisplay, player_health_color, (600, 25, player_health, 25))
	pygame.draw.rect(gameDisplay, enemy_health_color, (20, 25, enemy_health, 25))
	
def gameLoop():    
	gameExit = False
    
	player_health = 100 
	enemy_health = 100	
   
	mainTankX = display_width * 0.9	
	mainTankY = display_hight * 0.9
    
	tankMove = 0
	currentTurPos = 0		
	changeTur = 0
	barrier_width = 50
    
	fire_power = 50   
	power_change = 0 
    
	enemyTankX = display_width * 0.1	
	enemyTankY = display_hight * 0.9 				


	xlocation = display_width/2 + random.randint(-0.1*display_width, 0.1*display_width)	
	randomHeight = random.randrange(display_hight*0.1, display_hight*0.6)
    
	while not gameExit:
		    
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				gameExit = True
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					tankMove = -5 			
				elif event.key == pygame.K_RIGHT:
					tankMove = 5			
				elif event.key == pygame.K_UP:
					changeTur = 1			
				elif event.key == pygame.K_DOWN:
					changeTur = -1			
				elif event.key == pygame.K_SPACE:
					damage = fireSell(gun, mainTankX, mainTankX, currentTurPos, fire_power, xlocation, barrier_width, randomHeight, enemyTankX, enemyTankY)		
					enemy_health -= damage 	
					
					if enemy_health > 0: 
						possibleMovement = ['f', 'r']		
						moveIndex = random.randrange(0,2)	
					
					
						for x in range(random.randrange(0,10)):
					
							if display_width*0.3 > 	enemyTankX > 0:
								if possibleMovement[moveIndex] == 'f':
									enemyTankX += 5
								elif possibleMovement[moveIndex] == 'r':
									enemyTankX -= 5
								
								gameDisplay.fill(white)
								health_bars(player_health, enemy_health)
								gun = tank(mainTankX , mainTankY , currentTurPos)
								enemy_gun = enemy_tank(enemyTankX , enemyTankY , 8)	
					
								fire_power += power_change      
								power(fire_power)        
				
								barrier(xlocation, randomHeight, barrier_width)
								gameDisplay.fill(green, rect=[0,display_hight - ground_height, display_width, ground_height])
	
								pygame.display.update()
								clock.tick(FPS)
								
					
						damage = e_fireSell(enemy_gun, enemyTankX, enemyTankY, 8, 50, xlocation, barrier_width, randomHeight, mainTankX, mainTankX) 		
						player_health -= damage 
				elif event.key == pygame.K_a:
					power_change = -1
					pygame.mixer.Sound.play(power_sound)
				elif event.key == pygame.K_d:
					power_change = 1
					pygame.mixer.Sound.play(power_sound)
				
		
			elif event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
					tankMove = 0
				if event.key == pygame.K_UP or event.key == pygame.K_DOWN:	
					changeTur = 0		
				if event.key == pygame.K_a or event.key == pygame.K_d:
					power_change = 0 	
		    
			mainTankX += tankMove
		    
			currentTurPos += changeTur
			if currentTurPos > 8:
				currentTurPos = 8
			elif currentTurPos < 0:
				currentTurPos = 0
	  
			if mainTankX - (tankWidth/2) < xlocation+barrier_width:
				mainTankX += 5
		    
		    
			gameDisplay.fill(white)
			health_bars(player_health, enemy_health)
			gun = tank(mainTankX , mainTankY , currentTurPos)
			enemy_gun = enemy_tank(enemyTankX , enemyTankY , 8)	
		    	
			fire_power += power_change  
			
			if fire_power > 100:
				fire_power = 100
			elif fire_power < 1:
				fire_power = 1
			  
			power(fire_power)        
		    
			barrier(xlocation, randomHeight, barrier_width)
			gameDisplay.fill(green, rect=[0,display_hight - ground_height, display_width, ground_height])
	
			pygame.display.update()
			
			if player_health < 1:
				game_over()
			elif enemy_health < 1:
				you_win()
			clock.tick(FPS)

	pygame.quit()  
	quit()    

if __name__ == "__main__":
	game_intro()
