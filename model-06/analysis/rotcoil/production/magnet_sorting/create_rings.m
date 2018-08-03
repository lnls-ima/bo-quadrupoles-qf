function ring = create_rings(indcs, data, add_offset)
    if ~exist('add_offset', 'var')
        add_offset = false;
    end
    
    params = specifics.get_params();
    params = params.objective_data;
    ring.bare = params.ring0;
    
    fs = fieldnames(indcs);
    for i=1:length(fs)
        m = fs{i};
        ring.(m) = insert_quads(ring.bare, data, params.fam_data, indcs.(m), add_offset);
        ring.(m) = specifics.do_corrections(ring.(m), params.nus, params.orbit);
    end
