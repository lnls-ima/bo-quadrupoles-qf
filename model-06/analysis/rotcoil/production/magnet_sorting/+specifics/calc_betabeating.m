function rmst = calc_betabeating(params, data, indcs, add_offset)
    if ~exist('add_offset', 'var')
        add_offset = false;
    end
    
    ring = insert_quads(params.ring0, data, params.fam_data, indcs, add_offset);
    if add_offset
        ring = specifics.do_corrections(ring, params.nus, params.orbit);
    end
    [TD, ~] = twissring(ring, 0, 1:length(ring));

    beta = cat(1, TD.beta);
    tw.betax = beta(:,1);
    tw.betay = beta(:,2);
%     co = cat(1,TD.ClosedOrbit);
%     tw.cox  = co(1:4:end);
%     tw.coy  = co(3:4:end);
    
    bbx = (tw.betax-params.twi0.betax)./params.twi0.betax;
    rmsx = sqrt(trapz(params.twi0.pos, bbx.*bbx)/params.twi0.pos(end));
    bby = (tw.betay-params.twi0.betay)./params.twi0.betay;
    rmsy = sqrt(trapz(params.twi0.pos, bby.*bby)/params.twi0.pos(end));
    rmst = (rmsx + rmsy) * 100;
end