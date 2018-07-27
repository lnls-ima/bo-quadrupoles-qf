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
    indcs.james = data.james_sorting;
    
    meth = {'exc_err'};
    for i=1:length(meth)
        m = meth{i};
        indcs.([m,'p']) = sort_simple(data.(M), m, indcs.james);
        indcs.([m,'c']) = sort_simple_constraint(data.(M), m, indcs.james);
    %     idcs_s = sort_by_phase_advance(data.M1, m);
    end

    %% Do Simulated annealing around the sorted solution.
%     indcs.anneal = sort_simulated_annealing_constraint(data.(M), indcs.exc_errc);

    %% make plots
    make_plots(indcs, data.(M));