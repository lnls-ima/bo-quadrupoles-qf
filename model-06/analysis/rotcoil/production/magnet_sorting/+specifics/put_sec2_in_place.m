function idcs = put_sec2_in_place(idcs, id)
    if ~exist('id', 'var'), id = 2; end
    idcs = circshift(idcs, [-find(idcs==id)+2, 0]);
end
