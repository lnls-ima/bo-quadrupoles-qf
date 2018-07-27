function ring = insert_quads(ring, data, fam_data, idcs)
    Q_idx = fam_data.QF.ATIndex;

    ring = lnls_add_misalignmentX(data.x0(idcs), Q_idx, ring);
    ring = lnls_add_misalignmentY(data.y0(idcs), Q_idx, ring);
    ring = lnls_add_excitation(data.exc_err(idcs), Q_idx, ring);
