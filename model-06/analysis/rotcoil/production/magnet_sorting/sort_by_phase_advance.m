function sorted_idcs = sort_by_phase_advance(data, param)

if ~exist('param', 'var')
    param = 'x0';
end

fig_mer = data.(param);
fig_mer = fig_mer - median(fig_mer);
[~, idcs] = sort(fig_mer);

off = 13;  % at each 13 dipoles, the phase advance is 10*pi and
           % at each 26 dipoles, the phase advance is 20*pi

idcs1 = idcs(1:2:end);
idcs2 = flipud(idcs(2:2:end));

idcs11 = idcs1(1:off-2);
idcs12 = idcs1(off-1);
idcs13 = idcs1(off:end);
idcs21 = idcs2(1:off);
idcs22 = idcs2(off+1);
idcs23 = idcs2(off+2:end);

sorted_idcs = [idcs13; idcs21; idcs12; idcs22; idcs23; idcs11];