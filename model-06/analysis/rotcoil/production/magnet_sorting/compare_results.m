function compare_results(indcs, add_offset)
    if ~exist('add_offset', 'var')
        add_offset = false;
    end
    data_LE = load_data('LE');
    data_HE = load_data('HE');
    params = specifics.get_params();
    params = params.objective_data;
    
    Meds = {'M1', 'M2', 'M3'};
    fs = fieldnames(indcs);
    
    alin = @(x,y) strjust(sprintf(x, y), 'center');
    fprintf(alin('%15s', 'Indices'));
    fprintf('|%s', alin('%10s', 'Dist.'));
    for i=1:length(Meds)
        fprintf('|%s', alin('%14s', Meds{i}));
    end
    fprintf('\n');
    
    fmt = '| %5.3f  %5.3f ';
    for ii=1:length(fs)
        fprintf(alin('%15s', fs{ii}));
        for i=1:length(Meds)
            params.data_LE = data_LE.(Meds{i});
            params.data_HE = data_HE.(Meds{i});

            r = specifics.calc_residue(indcs.(fs{ii}), params, add_offset);
            if i==1
                fprintf('|%s', alin('%10s', sprintf('%03d', r(3))));
            end
            fprintf(fmt, r(1), r(2));
        end
        fprintf('\n');
    end
end