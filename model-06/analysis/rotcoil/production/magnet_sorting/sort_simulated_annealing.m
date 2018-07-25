function idcs = sort_simulated_annealing(ring, data, fam_data, orbit, idcs)
    
    twi0 = calctwiss(ring);
    
    ring_t = insert_quads(ring, data, fam_data, idcs);
    [ring_t, ~] = cod_sg(orbit, ring_t);
    res = calc_residue(ring_t, twi0);
    
    for i=1:1000
        idcs_t = change_order(idcs);
        ring_t = insert_quads(ring, data, fam_data, idcs_t);
        [ring_t, ~] = cod_sg(orbit, ring_t);
        res_t = calc_residue(ring_t, twi0);
        if res_t < res
            res = res_t;
            idcs = idcs_t;
            fprintf('%03d : %7.4f\n', i, res);
        end
    end
end

function idcs = change_order(idcs)
    prm = randperm(50, 2);
    idcs(prm) = idcs(fliplr(prm));
end

function res = calc_residue(ring, twi0)
    tw = calctwiss(ring);
    res = (rms((tw.betax-twi0.betax)./twi0.betax) + ...
           rms((tw.betay-twi0.betay)./twi0.betay)) * 100;
end