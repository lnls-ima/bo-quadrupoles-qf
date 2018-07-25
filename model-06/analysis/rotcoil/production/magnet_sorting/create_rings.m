function ring = create_rings(indcs, data)

    % sirius('BO.V04.01');
    ring.bare = sirius_bo_lattice();
    fam_data = sirius_bo_family_data(ring.bare);

    orbit.bpm_idx = fam_data.BPM.ATIndex(:);
    orbit.hcm_idx = fam_data.CH.ATIndex(:);
    orbit.vcm_idx = fam_data.CV.ATIndex(:);
    orbit.max_nr_iter = 20;
    orbit.svs = 'all';
    r = calc_respm_cod(ring.bare, orbit.bpm_idx, orbit.hcm_idx, orbit.vcm_idx);
    orbit.respm = r.respm;

    fs = fieldnames(indcs);
    for i=1:length(fs)
        ring.(fs{i}) = insert_quads(ring.bare, data, fam_data);
        [ring.(fs{i}), ~] = cod_sg(orbit, ring.(fs{i}));
    end
