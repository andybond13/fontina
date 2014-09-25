%fontina-matlab interpreter
clear all;
close all;
clc;

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
hybrid =        cell2num(A(:,18));
begin = datenum(beginDate);
fprintf(' done\n');

% compute quantities of interest
mpg = miles ./ gallons;
price = dollars ./ actualGals;
mpd = miles ./ days;
carweight = ones(size(driver));  %curb weight, lbs
gastank = ones(size(driver));    %gas tank, gals
for i=1:length(driver)
    switch model(i)
        case 8
            carweight(i) = 3230;
        case 7
            carweight(i) = 3126;
        case 6
            if (year(i) == 2003)
                carweight(i) = 3880;
            elseif (year(i) == 2008)
                carweight(i) = 4508;
            end
        case 5
            carweight(i) = 3528;
        case 4
            carweight(i) = 3119;
        case 3
            carweight(i) = 2764;
        case 2
            if (year(i) == 1990)
                carweight(i) = 2769;
            elseif (year(i) == 1985)
                carweight(i) = 2850;
            end
        case 1
            carweight(i) = 2270;
        case 0
            carweight(i) = 3424;
    end
    assert(carweight(i) ~= 0);
end

% data = [days log(mpd) octane snowtires make model year engineIV enginecyl engineL ethanol...
%     (driver == 1) (driver == 2) (driver == 3)]; 
data = [days log(mpd) octane snowtires year log(carweight) engineIV enginecyl engineL ...
    ethanol avgMileage hybrid begin (driver == 1) (driver == 2) (driver == 3)];
%trainbr; 
%trainlm:
%trainscg
%trainrp
%traingdx
%trainbfg

%feedforward,cascadefeedforward,none

%variables; log or not; date, season/proj.temp

% MLS regression
fprintf('performing MLS regression...');
%ds = dataset(mpg,data);
[b,bint,r,rint,stats] = regress(mpg,[ones(length(data),1) data]);
fprintf('\n');
for i=1:length(b)
    if (bint(i,1)*bint(i,2) < 0 && i > 1)
        fprintf('*** coefficient %u insignificant!\n',i-1);
    end
end
fprintf('...done\n');
fprintf('  R^2 = %f\n',stats(1));

% k-means grouping
fprintf('performing grouping...');
kgroup =kmeans(data,4,'replicates',100);
figure
andrewsplot(data,'group',kgroup)
fprintf(' done\n');

% plot in 3d
figure
scatter3(driver,year,mpg,10,log(mpd))
title('MPG - colored by log(mpd)');
xlabel('driver'); ylabel('year'); zlabel('mpg');

figure
scatter3(driver,year,mpg,10,kgroup)
title('MPG - colored by k-group');
xlabel('driver'); ylabel('year'); zlabel('mpg');

% neural network model
fprintf('performing neural network model...');
inputs = data';
n_nodes = 12;
n_times = 2;
targets = mpg';
nnscript;
r = corrcoef(net(data')',mpg');
fprintf('...done\n');
fprintf('  R^2 = %f,    performance = %f\n',r(1,2),performance);

