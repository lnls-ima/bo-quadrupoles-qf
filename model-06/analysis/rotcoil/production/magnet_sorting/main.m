function indcs = main(M, energy)
    if ~exist('M', 'var')
        M = 'M1';
    end
    if ~exist('energy', 'var')
        energy = 'LE';
    end
    
    % sirius('BO.V04.01');
    data = load_data(energy);

    %%
    indcs.james = data.M2.james_sorting;
    
    meth = {'exc_err'};
    for i=1:length(meth)
        m = meth{i};
        indcs.([m,'c']) = sort_simple(data.(M), m, indcs.james);
    %     idcs_s = sort_by_phase_advance(data.M1, m);
    end

    %% Do Simulated annealing around the sorted solution.
%     indcs.anneal = sort_simulated_annealing(data.(M), indcs.exc_errc);

    %% Do multi-objective optimization;
%     opt = specifics.get_params();
%     multiobjective.run(opt);
end
