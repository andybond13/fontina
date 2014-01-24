%fontina-matlab interpreter
clear all;
close all;

% format:
% [miles,gallons,actualGals,dollars,days,octane,snowtires,make,model,...
%   year,engineIV,enginecyl,engineL,ethanol,driver,avgMileage,beginDate]
A=read_mixed_csv('car_data.csv',',');

%define variables (cell arrays)
miles =         A(:,1);
gallons =       A(:,2);
actualGals =    A(:,3);
dollars =       A(:,4);
days =          A(:,5);
octane =        A(:,6);
snowtires =     A(:,7);
make =          A(:,8);
model =         A(:,9);
year =          A(:,10);
engineIV =      A(:,11);
enginecyl =     A(:,12);
ethanol =       A(:,13);
driver =        A(:,14);
avgMileage =    A(:,15);
beginDate =     A(:,16);
