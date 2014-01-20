#!/usr/bin/python

import csv
import datetime
import os
import copy

class Trip:
	dols = []
	dists = []
	gals = []
	octs = []
	drivers = []
	tires = []
	miles		= 0
	gallons		= 0
	days		= 0
	octane		= 0
	snowtires	= 0
	make		= 0
	model		= 0
	year		= 0
	engineIV	= 0
	enginecyl	= 0
	engineL		= 0
	ethanol		= 0
	driver		= 0
	avgMileage	= 0
	avgDate		= 0
		
	def write(self):
		out = [self.miles,self.gallons,self.days,self.octane,self.snowtires,self.make,self.model,self.year,self.engineIV,self.enginecyl,self.engineL,self.ethanol,self.driver,self.avgMileage]
		return out
	
	def clear(self):
		self.dols[:] = []
		self.dists[:] = []
		self.gals[:] = []
		self.octs[:] = []
		self.drivers[:] = []
		self.tires[:] = []
		self.miles		= 0
		self.gallons		= 0
		self.days		= 0
		self.octane		= 0
		self.snowtires	= 0
		self.make		= 0
		self.model		= 0
		self.year		= 0
		self.engineIV	= 0
		self.enginecyl	= 0
		self.engineL		= 0
		self.ethanol		= 0
		self.driver		= 0
		self.avgMileage	= 0
		self.avgDate		= 0


def wavg(series, weight):
	avg = 0
	assert(len(series) == len(weight))
	for i in [0]:#range(len(weight)):
		avg += series[i] * weight[i] / sum(weight)
	return avg

def dateMaker(date):
	start = 0
	while date.find("/",start) > -1:
		start = date.find("/",start) + 1
	year = date[start:]
	if len(year) == 2:
		if (int(year) > 50):
			year = 1900 + int(year)
		if (int(year) <= 50):
			year = 2000 + int(year)
	return date[0:start] + str(year)

def check(fill,gastype,driver,snowtires,ethanol,hybrid):
	assert(fill == 0 or fill == 1)
	assert(gastype == 1 or gastype == 2 or gastype == 3)
	assert(driver == "Andy" or driver == "Mark" or driver == "Mary" or driver == "Jeff")
	assert(snowtires == 0 or snowtires == 1)
	assert(ethanol == 0 or ethanol == 1)
	assert(hybrid == 0 or hybrid == 1)
	#price
	#mpg
	#miles
	#date
	#drivers
	#snowtires
	#ethanol
	#
	#print "ok"

def checkTrip(a):
	a.miles = sum(a.dists)
	a.dollars = sum(a.dols)
	a.gallons = sum(a.gals)
	a.octane = wavg(a.octs,a.gals)
	assert(a.time > 0)
	assert(a.miles > 0)
	assert(a.dollars > 0)
	assert(a.gallons > 0)

def main(dir,outfile):

	trips = []

	for file in os.listdir(dir):

		if not file.endswith('.csv'):
			continue

		print file
		f = open(dir+file,'rU')
		datareader = csv.reader(f, dialect = csv.excel_tab)
		lineNum = 0
		
		beginMiles = 0
		beginDate = 0
		
		for row in datareader:
			lineNum += 1
			line = str(row)
			line = line[2:-2].split(',')
			if (line[0] == "Date"):
				continue
			date = dateMaker(str(line[0]))
			odometer = int(line[1])
			fill = int(line[2])
			gastype = int(line[3])
			gallons = float(line[4])
			dollars = float(line[5])
			driver = str(line[6])
			snowtires = int(line[7])
			ethanol = int(line[8])
			make = str(line[9])
			model = str(line[10])
			year = int(line[11])
			engineL = float(line[12])
			enginecyl = int(line[13])
			engineIV = int(line[14])
			hybrid = int(line[15])

			if (fill == -1):
				#begin trip
				#make trip opject
				a = Trip()
				beginMiles = odometer
				beginDate = date
			else:
				#check and add to trip
				a.dols.append(dollars)
				a.gals.append(gallons)
				a.dists.append(dollars)
				a.octs.append(gastype)
				a.drivers.append(driver)
				a.tires.append(snowtires)
				check(fill,gastype,driver,snowtires,ethanol,hybrid)	
				
			if (fill == 1):

				#end trip
				tripMiles = odometer - beginMiles
				dateobj1 = datetime.datetime.strptime(beginDate,'%m/%d/%Y').date()
				dateobj2 = datetime.datetime.strptime(date,'%m/%d/%Y').date()
				tripDate = dateobj2 - dateobj1
				tripDays = tripDate.days

				if (tripDays == 0):
					tripDays += 1

				a.time = tripDays
				a.make		= make
				a.model		= model
				a.year		= year
				a.engineIV	= engineIV
				a.enginecyl	= enginecyl
				a.engineL		= engineL
				a.ethanol		= ethanol
				
				#check and save trip
				checkTrip(a)
				trips.append(copy.deepcopy(a))

				#reset dollars and gallons
				#make trip opject
				a.clear()
				beginDate = date
				beginMiles = odometer

	fo = open(outfile,'wb')	
	datareader = csv.writer(fo, delimiter=',')

	#print trips
	for thisTrip in trips:
		out = thisTrip.write()
		datareader.writerow(out)


dir = './raw/'
outfile = './car_data.csv'
main(dir,outfile)
