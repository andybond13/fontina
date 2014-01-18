#!/usr/bin/python

import csv
import datetime
import os

class Trip:
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
		
	def write():
		out = [miles,gallons,days,octane,snowtires,make,model,year,engineIV,enginecyl,engineL,ethanol,driver,beginmileage]
		return out

def check():
def dateMaker(date):
	start = 0
	while date.find("/",start) > -1:
		start = date.find("/",start) + 1
	year = date[start:]
	if len(year) == 2:
		if (year > 50):
			year = 1900 + int(year)
		if (year <= 50):
			year = 2000 + int(year)
	return date[0:start] + str(year)
	#price
	#mpg
	#miles
	#date
	print "ok"

def main(dir,outfile):


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
				beginMiles = odometer
				beginDate = date
			else:
				#check and add to trip
				check(fill,gastype,driver,snowtires,ethanol,hybrid)	
				
			if (fill == 1):
				#end trip
				tripMiles = odometer - beginMiles
				beginMiles = odometer
				dateobj1 = datetime.datetime.strptime(beginDate,'%m/%d/%Y').date()
				dateobj2 = datetime.datetime.strptime(date,'%m/%d/%Y').date()
				tripDate = dateobj2 - dateobj1

				if (tripDate == 0):
					tripDate += 1
				beginDate = date

				#check trip
				checkTrip(tripDate.days, tripMiles)

				#make trip opject
								
	
	fo = open(outfile,'wb')	
	#print trips


dir = './raw/'
outfile = './car_data.csv'
main(dir,outfile)
