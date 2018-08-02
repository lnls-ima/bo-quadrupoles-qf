function sorted_indcs = sort_simple_constraint(data, param, indcs)
    dt = data.(param)(indcs);
    [~, sorted_indcs_odd] = sort(dt(1:2:end));
    [~, sorted_indcs_even] = sort(dt(2:2:end));
    indcs_odd = indcs(1:2:end);
    indcs_even = indcs(2:2:end);
    
    sorted_indcs_odd = indcs_odd(sorted_indcs_odd);
    sorted_indcs_odd = [flipud(sorted_indcs_odd(2:2:end)); sorted_indcs_odd(1:2:end)];
        
    sorted_indcs_even = indcs_even(sorted_indcs_even);
    sorted_indcs_even = [flipud(sorted_indcs_even(2:2:end)); sorted_indcs_even(1:2:end)];
    
    sorted_indcs = [sorted_indcs_odd'; sorted_indcs_even'];
    sorted_indcs = reshape(sorted_indcs,[],1);
    sorted_indcs = put_sec2_in_place(sorted_indcs, indcs(2));
end

function idcs = put_sec2_in_place(idcs, id)
    if ~exist('id', 'var'), id = 2; end
    idcs = circshift(idcs, [-find(idcs==id)+2, 0]);
end
