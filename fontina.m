%fontina-matlab interpreter
clear all;
close all;

% format:
% [miles,gallons,actualGals,dollars,days,octane,snowtires,make,model,...
%   year,engineIV,enginecyl,engineL,ethanol,driver,avgMileage,beginDate]
fprintf('reading data from csv...');
A=read_mixed_csv('car_data.csv',',');
fprintf(' done\n');

%define variables (cell arrays)
fprintf('converting to numerical arrays...');
miles =         cell2num(A(:,1));
gallons =       cell2num(A(:,2));
actualGals =    cell2num(A(:,3));
dollars =       cell2num(A(:,4));
days =          cell2num(A(:,5));
octane =        cell2num(A(:,6));
snowtires =     cell2num(A(:,7));
make =          cell2num(A(:,8));
model =         cell2num(A(:,9));
year =          cell2num(A(:,10));
engineIV =      cell2num(A(:,11));
enginecyl =     cell2num(A(:,12));
engineL =       cell2num(A(:,13));
ethanol =       cell2num(A(:,14));
driver =        cell2num(A(:,15));
avgMileage =    cell2num(A(:,16));
beginDate =              A(:,17);
fprintf(' done\n');

% compute quantities of interest
mpg = miles ./ gallons;
price = dollars ./ actualGals;
mpd = miles ./ days;
data = [days log(mpd) octane snowtires make model year engineIV enginecyl engineL ethanol...
    (driver == 1) (driver == 2) (driver == 3)];

% MLS regression
fprintf('performing MLS regression...');
ds = dataset(mpg,data);
fprintf(' done\n');

% k-means grouping
kgroup = kmeans(data,1);
andrewsplot(data,'group',kgroup)

% neural network model
inputs = [mpd,season,date,odo,gals,dol,trip,price];
n_nodes = 12;
targets = mpg;
nnscript;

