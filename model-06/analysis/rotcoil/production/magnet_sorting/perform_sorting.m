function [indcs, data, ring] = perform_sorting()
    % sirius('BO.V04.01');
    ring.bare = sirius_bo_lattice();
    fam_data = sirius_bo_family_data(ring.bare);

    % data = import_readme(fullfile('../', 'README-110A.md'));
    data = import_readme(fullfile('../', 'README-4A.md'));

    %%
    indcs.unsorted = 1:length(data.x0);
    ring.unsorted = insert_quads(ring.bare, data, fam_data);
    
    meth = {'exc_err'};
    for i=1:length(meth)
        m = meth{i};
        indcs.(m) = sort_simple(data, m);
    %     idcs_s = sort_by_phase_advance(data, m);
        ring.(m) = insert_quads(ring.bare, data, fam_data, indcs.(m));
    end

    orbit.bpm_idx = fam_data.BPM.ATIndex(:);
    orbit.hcm_idx = fam_data.CH.ATIndex(:);
    orbit.vcm_idx = fam_data.CV.ATIndex(:);
    orbit.max_nr_iter = 20;
    orbit.svs = 'all';
    r = calc_respm_cod(ring.bare, orbit.bpm_idx, orbit.hcm_idx, orbit.vcm_idx);
    orbit.respm = r.respm;

    indcs.anneal = sort_simulated_annealing(ring.bare, data, fam_data, orbit, indcs.exc_err);
    ring.anneal = insert_quads(ring.bare, data, fam_data, indcs.anneal);

    fs = fieldnames(ring);
    for i=1:length(fs)
        m = fs{i};
        [ring.(m), ~] = cod_sg(orbit, ring.(m));
    end
