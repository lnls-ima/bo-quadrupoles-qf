function ring = insert_quads(ring, data, fam_data, idcs, add_offset)
    if ~exist('add_offset', 'var')
        add_offset = false;
    end
    Q_idx = fam_data.QF.ATIndex;

    if add_offset
        ring = lnls_add_misalignmentX(data.x0(idcs), Q_idx, ring);
        ring = lnls_add_misalignmentY(data.y0(idcs), Q_idx, ring);
    end
    ring = lnls_add_excitation(data.exc_err(idcs), Q_idx, ring);
