function sorted_idcs = sort_simple(data, param)

if ~exist('param', 'var')
    param = 'x0';
end

[~, sorted_idcs] = sort(data.(param));
sorted_idcs = [flipud(sorted_idcs(2:2:end)); sorted_idcs(1:2:end)];
