function res = calc_residue(indcs, params, add_offset)
    if ~exist('add_offset', 'var')
        add_offset = false;
    end
    
    res(1) = specifics.calc_betabeating(params, params.data_LE, indcs, add_offset);
    res(2) = specifics.calc_betabeating(params, params.data_HE, indcs, add_offset);
    
    % measure how many changes they will have to make;
    res(3) = sum(indcs ~= params.data_LE.james_sorting);
%     % measure how long they will have to walk to change magnets;
%     [~, ia, ib] = intersect(param.data_LE.james_sorting, indcs);
%     vec = abs(ia-ib);
%     in = vec>25;
%     vec(in) = 50 - vec(in);
%     res(3) = sum(vec);

end