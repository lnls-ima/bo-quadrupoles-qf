function multi_objective_constraint(data, idcs0)
    setappdata(0, 'stop_now', 0);
    param.ring0 = sirius_bo_lattice();
    param.twi0 = calctwiss(param.ring0);
    param.nus = [param.twi0.mux(end)/2/pi, param.twi0.muy(end)/2/pi];
    param.data = data.M2;
    param.idcs_ref = data.james_sorting;
    
    param.fam_data = sirius_bo_family_data(param.ring0);
    param.orbit.bpm_idx = param.fam_data.BPM.ATIndex(:);
    param.orbit.hcm_idx = param.fam_data.CH.ATIndex(:);
    param.orbit.vcm_idx = param.fam_data.CV.ATIndex(:);
    param.orbit.max_nr_iter = 20;
    param.orbit.svs = 'all';
    r = calc_respm_cod(param.ring0, param.orbit.bpm_idx, param.orbit.hcm_idx, param.orbit.vcm_idx);
    param.orbit.respm = r.respm;
        
    Nid = 20;
    Ncut = 15;
    NG = 200;
    Gn = zeros(size(idcs0,1), Nid);
    Gn(:,1) = idcs0;
    Gn(:,2) = data.james_sorting;
    for i=3:size(Gn, 2)
%         Gn(:,i) = permute_randomly(idcs0);
        Gn(:,i) = change_order(idcs0);
    end
    resn = zeros(2, Nid);
    for i=1:size(Gn, 2)
        resn(:,i) = calc_residue(Gn(:,i), param);
    end
    id_keep = save_best_and_kill_worst(resn, Ncut);
    G = Gn(:,id_keep);
    res = resn(:,id_keep);
    save('G001.mat', 'Gn', 'resn');
    fprintf('finish G001 with %03d individuals\n', size(G,2));
   
    
    for i=2:NG
        sz = size(G,2);
        Gn = zeros(size(G,1), Nid);
        resn = zeros(2, Nid);
        Gn(:,1:sz) = G;
        resn(:,1:sz) = res;
        for ii=sz+1:Nid
            ind = G(:, randi(sz));
            Gn(:, ii) = change_order(ind);
            resn(:, ii) = calc_residue(Gn(:, ii), param);
        end
        id_keep = save_best_and_kill_worst(resn, Ncut);
        G = Gn(:,id_keep);
        res = resn(:,id_keep);
        st = sprintf('G%03d', i);
        save([st, '.mat'], 'Gn', 'resn');
        fprintf('finish %s with %03d individuals. beta = %5.3f, dist=%3d\n', ...
                st, size(G,2), min(res(1,:)), min(res(2,:)));
        if getappdata(0, 'stop_now')
            fprintf('Interruped by user at generation %03d\n', i);
            break;
        end
    end
end

function id_keep = save_best_and_kill_worst(res, Ncut)
    [~, id1] = sort(res(1,:));
    [~, id2] = sort(res(2,:));
    id_keep = unique([id1(1:Ncut),id2(1:Ncut)]);
end

function idcs = put_sec2_in_place(idcs, id)
    if ~exist('id', 'var'), id = 2; end
    idcs = circshift(idcs, [-find(idcs==id)+2, 0]);
end

function idcs = permute_randomly(idcs)
    od = randperm(25,25)*2-1;
    ev = randperm(25,25)*2;
    id = reshape([od;ev],[],1);
    id = put_sec2_in_place(id);
    idcs = idcs(id);
end

function idcs = change_order(idcs)
    id = idcs(2);
    prm = randperm(25, 2)*2 - randi([0,1]); %permute odd with odd and even with even
    idcs(prm) = idcs(fliplr(prm));
    idcs = put_sec2_in_place(idcs, id);
end

function ring = do_corrections(ring, nus, orbit)
    [ring, ~] = cod_sg(orbit, ring);
%     [ring, ~] = lnls_correct_tunes(ring, nus, {'QF', 'QD'}, 'svd', 'add');
end

function res = calc_residue(indcs, param)
    ring = insert_quads(param.ring0, param.data, param.fam_data, indcs);
    ring = do_corrections(ring, param.nus, param.orbit);
    [TD, ~] = twissring(ring, 0, 1:length(ring));

    beta = cat(1, TD.beta);
    tw.betax = beta(:,1);
    tw.betay = beta(:,2);
%     co = cat(1,TD.ClosedOrbit);
%     tw.cox  = co(1:4:end);
%     tw.coy  = co(3:4:end);
    
    res(1) = (rms((tw.betax-param.twi0.betax)./param.twi0.betax) + ...
              rms((tw.betay-param.twi0.betay)./param.twi0.betay)) * 100;
    
    % measure how many changes they will have to make;
    res(2) = sum(indcs ~= param.idcs_ref);
%     % measure how long they will have to walk to change magnets;
%     [~, ia, ib] = intersect(param.idcs0, indcs);
%     vec = abs(ia-ib);
%     in = vec>25;
%     vec(in) = 50 - vec(in);
%     res(2) = sum(vec);
end