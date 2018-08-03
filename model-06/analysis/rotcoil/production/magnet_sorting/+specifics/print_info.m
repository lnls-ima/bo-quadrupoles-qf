function print_info(st, G, res)
    fmt = 'finish %s with %03d individuals. beta = (%5.3f, %5.3f), dist=%3d\n';
    fprintf(fmt, st, size(G,2), min(res(1,:)), min(res(2,:)), min(res(3,:)));
end