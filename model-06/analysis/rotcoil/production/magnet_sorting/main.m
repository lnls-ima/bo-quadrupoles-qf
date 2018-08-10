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
%     opt = specifics.get_params();
%     indcs.anneal = multiobjective.simulated_annealing_run(opt);

    %% Do multi-objective optimization;
%     multiobjective.run(opt);
end
