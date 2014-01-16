#!/usr/bin/python

import csv
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
	#price
	#mpg
	#miles
	#date
	print "ok"

def main(dir,outfile):

	fo = open(outfile,'wb')

	for file in os.listdir(dir):

		if not file.endswith('.csv'):
			continue

		print file
		f = open(dir+file,'rU')
		datareader = csv.reader(f, dialect = csv.excel_tab)
		lineNum = 0
		
		for row in datareader:
			lineNum += 1
			if (lineNum == 1):
				continue
			line = str(row)
			line = line[2:-2].split(',')
			print row
			date = str(line[0])
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
			print line	


dir = './raw/'
outfile = './car_data.csv'
main(dir,outfile)
