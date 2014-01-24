% convert cell array to numerical array
function arrayOut = cell2num(array)

arrayOut = zeros(size(array));
for i = 1:length(array)
    out = '';
    for j=1:length(array{i})
        out = strcat(out,num2str(array{i}(j)));
    end
    arrayOut(i) = str2double(out);
end