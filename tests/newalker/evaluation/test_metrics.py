# -*- coding: utf-8 -*-

import pytest

import numpy as np
from inferbeddings.evaluation import metrics


def scoring_function(args):
    Xr, Xe = args[0], args[1]
    d = {
        (1, 1, 1): 1.0,
        (1, 1, 2): 2.0,
        (1, 1, 3): 3.0,
        (2, 1, 1): 0.7,
        (2, 1, 2): 0.9,
        (2, 1, 3): 1.1,
        (3, 1, 1): 1.3,
        (3, 1, 2): 1.5,
        (3, 1, 3): 1.7,

        (4, 1, 1): 0.0,
        (4, 1, 2): 0.0,
        (4, 1, 3): 0.0,
        (4, 1, 4): 0.0,
        (1, 1, 4): 0.0,
        (2, 1, 4): 0.0,
        (3, 1, 4): 0.0,
    }
    values = []
    for i in range(Xr.shape[0]):
        subj, pred, obj = Xe[i, 0], Xr[i, 0], Xe[i, 1]
        values += [d[(subj, pred, obj)]]
    return np.array(values)


def test_ranking_score():
    ranker = metrics.Ranker(scoring_function, 4)

    err_subj, err_obj = ranker([(1, 1, 1)])
    assert(err_subj[0] == 2 and err_obj[0] == 3)

    err_subj, err_obj = ranker([(1, 1, 2)])
    assert(err_subj[0] == 1 and err_obj[0] == 2)

    err_subj, err_obj = ranker([(2, 1, 1)])
    assert(err_subj[0] == 3 and err_obj[0] == 3)


if __name__ == '__main__':
    pytest.main([__file__])