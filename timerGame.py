#!/usr/bin/python

import os
import pickle
import datetime
from time import sleep
from random import randit
from operator import itemgetter

selection = ''
players = []
high_scores = []

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

while selection != '6':

	clear()
	menu()

	selection = input('Selection: ')

	if selection == '1':
		clear()
		if len(players) < 2:
			print ('There must be at least 2 players')

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
