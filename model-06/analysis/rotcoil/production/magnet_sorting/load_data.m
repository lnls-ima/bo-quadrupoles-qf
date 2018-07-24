% sirius('BO.V04.01');
ring.bare = sirius_bo_lattice();
fam_data = sirius_bo_family_data(ring.bare);

% data = import_readme(fullfile('../', 'README-110A.md'));
data = import_readme(fullfile('../', 'README-4A.md'));

%%
ring.unsorted = insert_quads(ring.bare, data, fam_data);

meth = {'exc_err'};
for i=1:length(meth)
    m = meth{i};
    idcs_s = sort_simple(data, m);
%     idcs_s = sort_by_phase_advance(data, m);
    ring.(m) = insert_quads(ring.bare, data, fam_data, idcs_s);
end

orbit.bpm_idx = fam_data.BPM.ATIndex(:);
orbit.hcm_idx = fam_data.CH.ATIndex(:);
orbit.vcm_idx = fam_data.CV.ATIndex(:);
orbit.max_nr_iter = 20;
orbit.svs = 'all';
r = calc_respm_cod(ring.bare, orbit.bpm_idx, orbit.hcm_idx, orbit.vcm_idx);
orbit.respm = r.respm;

idcs_s = sort_simulated_annealing(ring.bare, data, fam_data, orbit, idcs_s);
ring.sorted = insert_quads(ring.bare, data, fam_data, idcs_s);

fs = fieldnames(ring);
for i=1:length(fs)
    m = fs{i};
    [ring.(m), ~] = cod_sg(orbit, ring.(m));
    twi.(m) = calctwiss(ring.(m));
end

%%
% [ring_uc, ~] = lnls_correct_tunes(ring_u, [nux0, nuy0], {'QF', 'QD'}, 'svd', 'add');
% [ring_sc, ~] = lnls_correct_tunes(ring_s, [nux0, nuy0], {'QF', 'QD'}, 'svd', 'add');

%%
% close all;

figure('Position', [100, 10, 1200, 2000]);
axs(1) = subplot(4, 1, 1);
axs(2) = subplot(4, 1, 2);
axs(3) = subplot(4, 1, 3);
axs(4) = subplot(4, 1, 4);
for i=1:length(axs)
    ax = axs(i);
    hold(ax, 'all');
    grid(ax, 'on');
    box(ax, 'on');
    xlabel(ax, 'position [m]');
end

fmt = '%10s ->   nu = (%6.3f, %6.3f), xi = (%5.3f, %5.3f)\n';
for i=1:length(fs)
    tw = twi.(fs{i});
    plot(axs(1), tw.pos, tw.cox*1000, 'LineWidth', 3);
    plot(axs(2), tw.pos, tw.coy*1000, 'LineWidth', 3);
    plot(axs(3), tw.pos, 100*(tw.betax-twi.bare.betax)./twi.bare.betax, 'LineWidth', 3);
    plot(axs(4), tw.pos, 100*(tw.betay-twi.bare.betay)./twi.bare.betay, 'LineWidth', 3);

    nux = tw.mux(end)/2/pi;
    nuy = tw.muy(end)/2/pi;
    fprintf(fmt, fs{i}, nux, nuy, tw.chromx, tw.chromy);
end

ylabel(axs(1), 'Horizontal Orbit [mm]');
ylabel(axs(2), 'Vertical Orbit [mm]');
ylabel(axs(3), 'Horizontal beta beat [%]');
ylabel(axs(4), 'Vertical beta beat [%]');

legend(axs(2), 'best', fs);