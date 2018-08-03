function idcs = sort_simulated_annealing(opt, idcs)
    setappdata(0, 'stop_now', 0);
    res = rms(opt.objective_fun(idcs, opt.objective_data));
    fprintf('%s : %7.4f\n', 'ini', res);
    
    for i=1:1000
        idcs_t = opt.small_change(idcs, opt.objective_data);
        res_t = rms(opt.objective_fun(idcs_t, opt.objective_data));
        if res_t < res
            res = res_t;
            idcs = idcs_t;
            fprintf('%03d : %7.4f\n', i, res);
        end
        if getappdata(0, 'stop_now')
            fprintf('Interruped by user at iteration %03d\n', i);
            break;
        end
    end
end
