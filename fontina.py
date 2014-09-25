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
	eths = []
	drivers = []
	tires = []
	miles		= 0
	gallons		= 0
	actualGals = 0
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
	beginDate		= 0
	hybrid = 0
    
		
	def write(self):
		out = [self.miles,self.gallons,self.actualGals,self.dollars,self.days,self.octane,self.snowtires,self.make,self.model,self.year,self.engineIV,self.enginecyl,self.engineL,self.ethanol,self.driver,self.avgMileage,self.beginDate,self.hybrid]
		return out
	
	def clear(self):
		self.dols[:] = []
		self.dists[:] = []
		self.gals[:] = []
		self.octs[:] = []
		self.eths[:] = []
		self.drivers[:] = []
		self.tires[:] = []
		self.miles		= 0
		self.gallons		= 0
		self.actualGals = 0
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
		self.driver		= ""
		self.avgMileage	= 0
		self.beginDate		= 0
		self.hybrid     = 0


def wavg(series, weight):
	avg = 0
	if (weight[0] <= 0):
		weight = weight[1:]
	assert(len(series) == len(weight))
	for i in range(len(weight)):
		avg +=  float(series[i])*float(weight[i])/float(sum(weight))
	return avg

def octaneCode(inOct):
	if (inOct == 1):
		return 87;
	elif (inOct == 2):
		return 89;
	elif (inOct == 3):
		return 93;
	else:
		print "Unknown octane code", inOct
		assert(1 == 0)

def driverCode(driver):
	if (driver == "Mark"):
		return 0
	elif (driver == "Mary"):
		return 1
	elif (driver == "Andy"):
		return 2
	elif (driver == "Jeff"):
		return 3
	else:
		print "Unknown driver: ", driver
		assert(1 == 0)

def makeCode(make):
	if (make == "Chevrolet"):
		return 0
	elif (make == "Buick"):
		return 1
	elif (make == "Oldsmobile"):
		return 2
	elif (make == "Mercury"):
		return 3
	elif (make == "Plymouth"):
		return 4
	elif (make == "Volkswagen"):
		return 5
	elif (make == "Toyota"):
		return 6
	elif (make == "Honda"):
		return 7
	else:
		print "Unknown make: ", make
		assert(1 == 0)


def modelCode(model):
	if (model == "Concourse"):
		return 0
	elif (model == "Vega"):
		return 1
	elif (model == "Century"):
		return 2
	elif (model == "Cierra"):
		return 3
	elif (model == "Sable"):
		return 4
	elif (model == "Voyager"):
		return 5
	elif (model == "Highlander"):
		return 6
	elif (model == "CRV"):
		return 7
	elif (model == "Jetta"):
		return 8
	else:
		print "Unknown model: ", model
		assert(1 == 0)

def gasTank(model,year):
	if (model == "Concourse"):
		return 21.0
	elif (model == "Vega"):
		return 16.0
	elif (model == "Century"):
		return 15.0
	elif (model == "Cierra"):
		return 15.7
	elif (model == "Sable"):
		return 16.0
	elif (model == "Voyager"):
		return 20.0
	elif (model == "Highlander"):
		if (year == 2003):
			return 19.8
		elif (year == 2008):
			return 17.2
	elif (model == "CRV"):
		return 15.3
	elif (model == "Jetta"):
		return 14.5
	else:
		print "Unknown model: ", model
		assert(1 == 0)

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
	#ethanol

def checkTrip(a):
	a.miles = sum(a.dists)
	a.dollars = sum(a.dols)
	a.actualGals = sum(i for i in a.gals if i > 0) 
	a.gallons = sum(a.gals)
	a.octane = wavg(a.octs,a.gals)
	print "octane",a.octane
	a.ethanol = wavg(a.eths,a.gals)
	print "ethanol",a.ethanol
	a.snowtires = wavg(a.tires,a.dists)
	a.driver = sorted(a.drivers)[len(a.drivers)/2]
	print a.beginDate
	assert(min(a.dists) > 0)
	assert(min(a.dols) > 0)
	assert(a.days > 0)
	assert(a.miles > 0)
	assert(a.dollars > 0)
	assert(a.gallons > 0)

def checkInterTrip(a,b):
    print a.beginDate
    print "mpg:   ", a.miles/a.gallons, b.miles/b.gallons
    print "price: ", a.dollars/a.actualGals, b.dollars/b.actualGals
    if(abs((a.miles/a.gallons)/(b.miles/b.gallons) - 1) > 0.5):
        status = raw_input("Press Enter to continue... (mpg)")
    if(abs((a.dollars/a.actualGals)/(b.dollars/b.actualGals) - 1) > 0.2):
        status = raw_input("Press Enter to continue... (price)")
    print ""

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
				beginOctane = 87
				beginEthanol = 0
				if (year >= 1994):
					beginEthanol = 1	
				a.gals.append(gallons)
			else:
				#check and add to trip
				a.dols.append(dollars)
				a.gals.append(gallons)
				a.dists.append(odometer - beginMiles)
				a.octs.append(beginOctane)
				a.eths.append(beginEthanol)
				a.drivers.append(driverCode(driver))
				a.tires.append(snowtires)
				check(fill,gastype,driver,snowtires,ethanol,hybrid)	
				beginMiles = odometer
				#update gas contents
				tank = gasTank(model, year)
				beginOctane = (gallons * octaneCode(gastype) + (tank - gallons) * beginOctane) / tank
				beginEthanol = (gallons * ethanol + (tank - gallons) * beginEthanol) / tank 
				
			if (fill == 1):

				#end trip
				tripMiles = sum(a.dists)
				dateobj1 = datetime.datetime.strptime(beginDate,'%m/%d/%Y').date()
				dateobj2 = datetime.datetime.strptime(date,'%m/%d/%Y').date()
				tripDate = dateobj2 - dateobj1
				tripDays = tripDate.days

				if (tripDays == 0):
					tripDays += 1

				a.days = tripDays
				a.make		= makeCode(make)
				a.model		= modelCode(model)
				a.year		= year
				a.engineIV	= engineIV
				a.enginecyl	= enginecyl
				a.engineL		= engineL
				a.beginDate = beginDate
				a.hybrid = hybrid
				a.avgMileage = odometer - 0.5*tripMiles
				
				#check and save trip
				checkTrip(a)
				if (len(trips) > 0):
					checkInterTrip(a,trips[-1])
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
