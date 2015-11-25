#!/usr/bin/env python
import numpy
import pandas
import os

Location = r'registeredpets.csv'
pets = pandas.read_csv(Location, names=['suburb','breed','type','colour','registered','age','name'])


while True:
	rnd = numpy.random.random_integers(1,46181)
	print pets['name'][rnd]
	guess = raw_input("Dog or Cat or Clue?")

	if guess ==  pets['type'][rnd]:
		print "Correct!"
		print pets['name'][rnd]+" is a "+pets['colour'][rnd]+" "+pets['breed'][rnd]+" "+pets['type'][rnd]+" living in "+pets['suburb'][rnd]


	elif guess == 'Clue':
		print pets['colour'][rnd]
		guess2 = raw_input("Dog or Cat?")
	
		if guess2 == pets['type'][rnd]:
			print "Correct!"
			print pets['name'][rnd]+" is a "+pets['colour'][rnd]+" "+pets['breed'][rnd]+" "+pets['type'][rnd]+" living in "+pets['suburb'][rnd]
		else:
			print "Wrong!"
			print pets['name'][rnd]+" is a "+pets['colour'][rnd]+" "+pets['breed'][rnd]+" "+pets['type'][rnd]+" living in "+pets['suburb'][rnd]
	
	else:
		print "Wrong!"
		print pets['name'][rnd]+" is a "+pets['colour'][rnd]+" "+pets['breed'][rnd]+" "+pets['type'][rnd]+" living in "+pets['suburb'][rnd]
