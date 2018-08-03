function idcs = permute_randomly(idcs, params)
    id = randperm(50,50);
    idcs = idcs(id);

    % Keep the constraints:
%     od = randperm(25,25)*2-1;
%     ev = randperm(25,25)*2;
%     id = reshape([od;ev],[],1);
%     id = put_sec2_in_place(id);
%     idcs = idcs(id);
end