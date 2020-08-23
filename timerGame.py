#!/usr/bin/python

import os
import pickle
import datetime
from time import sleep
from random import randint
from operator import itemgetter

selection = 0
players = []
currentScores = []
globalHighScores = []

if os.path.isfile('highscores.txt'):
	with open('highscores.txt','rb') as f:
		globalHighScores = pickle.load(f)

def clear():
	os.system('clear')

def moveOn():
	input ('Enter to continue')

def menu():
	print ("""
***************************
			  *
 1. Start game		  *
 2. Enter players	  *
 3. Remove players	  *
 4. View current scores	  *
 5. View top scores	  *
 6. Exit		  *
			  *
***************************
	""")

while True:

	clear()
	menu()
	try:
		selection = int(input('Selection: '))
	except ValueError:
		clear()
		print ('Please enter a valid selection')
		moveOn()

	if selection > 6:
		clear()
		print ('Please enter a valid selection')
		moveOn()

	if selection == 1:
		clear()
		currentScores.clear()

		if len(players) < 2:
			print ('There must be at least 2 players')
			moveOn()
			continue

		else:
			for x in range (len(players)):
				clear()
				print ("""

		**********************{}**********************
				""".format(players[x]))

				sleep (randint(3, 13))
				startTime = datetime.datetime.now()

				input("""
		************************************************
		************************************************
		**********************Press*********************
		**********************Enter*********************
		************************************************
		************************************************
				""")
				endTime = datetime.datetime.now()
				timeDiff = endTime - startTime
				diffStr = str(timeDiff)

				print (players[x] + ' : ' + diffStr)
				currentScores.append((players[x], diffStr))
				globalHighScores.append((players[x], diffStr))

				currentScores = sorted(currentScores, key=itemgetter(1), reverse=False)
				globalHighScores = sorted(globalHighScores, key=itemgetter(1), reverse=False)[:10]
				#print (globalHighScores)
				moveOn()

		winnerName = currentScores[0][0]
		winnerTime = currentScores[0][1]
		print ('The winner of this round is {} with a time of {}'.format(winnerName,winnerTime))
		moveOn()

	if selection == 2:
		clear()
		playerName = input('Player name: ')
		players.append(playerName)
		print ('{} is now playing'.format(playerName))
		moveOn()

	if selection == 3:
		clear()
		exitPlayer = input('Player to remove: ')
		try:
			players.remove(exitPlayer)
		except:
			print ('Player does not exist')
			moveOn()
			continue

		print ('{} is no longer part of the game'.format(exitPlayer))
		moveOn()

	if selection == 4:
		clear()
		for x in range (len(currentScores)):
			print ('{}	{}'.format(currentScores[x][0],currentScores[x][1]))

		moveOn()

	if selection == 5:
		clear()
		for x in range (len(globalHighScores)):
			print ('{}	{}'.format(globalHighScores[x][0],globalHighScores[x][1]))
		moveOn()

	if selection == 6:
		clear()
		with open ('highscores.txt','wb') as f:
			pickle.dump(globalHighScores,f)

		print ('Thank you for playing!!!')
		sleep(3)
		break
