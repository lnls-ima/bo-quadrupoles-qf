function data = import_readme(filename)

%% Code generated by matlab
% Initialize variables.
delimiter = {' ','|'};
startRow = 6;
endRow = 55;

% Format for each line of text:
% For more information, see the TEXTSCAN documentation.
formatSpec = '%s%f%f%f%*s%*s%*s%*s%*s%*s%*s%*s%*s%*s%*s%[^\n\r]';

% Open the text file.
fileID = fopen(filename,'r');

% Read columns of data according to the format.
% This call is based on the structure of the file used to generate this
% code. If an error occurs for a different file, try regenerating the code
% from the Import Tool.
textscan(fileID, '%[^\n\r]', startRow(1)-1, 'WhiteSpace', '', 'ReturnOnError', false);
dataArray = textscan(fileID, formatSpec, endRow(1)-startRow(1)+1, 'Delimiter', delimiter, 'MultipleDelimsAsOne', true, 'ReturnOnError', false, 'EndOfLine', '\r\n');
for block=2:length(startRow)
    frewind(fileID);
    textscan(fileID, '%[^\n\r]', startRow(block)-1, 'WhiteSpace', '', 'ReturnOnError', false);
    dataArrayBlock = textscan(fileID, formatSpec, endRow(block)-startRow(block)+1, 'Delimiter', delimiter, 'MultipleDelimsAsOne', true, 'ReturnOnError', false, 'EndOfLine', '\r\n');
    for col=1:length(dataArray)
        dataArray{col} = [dataArray{col};dataArrayBlock{col}];
    end
end

% Close the text file.
fclose(fileID);

%% Adapted by Fernando
names = dataArray{:, 1};

for ii=1:length(names)
    name = names{ii};
    names{ii} = strip(name(1:end-1), '*');
end

data.names = names;
data.x0 = 1e-6*dataArray{:, 2};
data.y0 = 1e-6*dataArray{:, 3};
data.int_stren = dataArray{:, 4};
data.ave_int_stren = mean(data.int_stren);
data.exc_err = data.int_stren / data.ave_int_stren - 1;

