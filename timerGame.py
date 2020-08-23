#!/usr/bin/python

import os
import pickle
import datetime
from time import sleep
from random import randint
from operator import itemgetter

selection = ''
players = []
globalHighScores = []
currentScores = []

def clear():
	os.system('clear')

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

	selection = input('Selection: ')

	if selection == '1':
		clear()
		if len(players) < 2:
			print ('There must be at least 2 players')
			sleep (2)
			menu()

		else:
			for x in range (len(players)):
				print ("""

		**********************{}************************
				""".format(players[x]))

				sleep (randint(1, 10))
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

				print (players[x] + ':' + diffStr)
				currentScores.append((players[x], diffStr))
				globalHighScores.append((players[x], diffStr))

				currentScores = sorted(currentScores, key=itemgetter(1), reverse=False)
				globalHighScores = sorted(globalHighScores, key=itemgetter(1), reverse=False)[:10]
				print (globalHighScores)
				sleep(5)
				clear()

		winnerName = currentScores[0][0]
		winnerTime = currentScores[0][1]
		print ('The winner of this round is {} with a time of {}'.format(winnerName,winnerTime))
		sleep(5)

	if selection == '2':
		clear()
		playerName = input('Player name: ')
		players.append(playerName)

	if selection == '3':
		clear()
		exitPlayer = input('Player to remove: ')
		try:
			players.remove(exitPlayer)
		except:
			print ('Player does not exist')

	if selection == '4':
		clear()
	if selection == '5':
		clear()
