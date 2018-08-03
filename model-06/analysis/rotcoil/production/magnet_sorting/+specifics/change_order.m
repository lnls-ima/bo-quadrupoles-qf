function idcs = change_order(idcs, params)
    prm = randperm(50, 2);
    idcs(prm) = idcs(fliplr(prm));
    
    % Keep the constraints
%     id = idcs(2);
%     prm = randperm(25, 2)*2 - randi([0,1]); %permute odd with odd and even with even
%     idcs(prm) = idcs(fliplr(prm));
%     idcs = put_sec2_in_place(idcs, id);
end