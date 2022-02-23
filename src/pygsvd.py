#!/usr/bin/env python

import numpy as np
from scipy.linalg import cossin


def pygsvd(a, b):
    """
    Generalized singular value decomposition.

    generalized singular value decomposition of matrices a(m, k) and b(n, k) as follows.

        a = ua @ da @ xt
        b = ub @ db @ xt

    where
        - (m + n) > k
        - ua, ub and xt are unitary
        - da and db is diagonal
        - da.T@da + db.T@da = I

    Parameters
    ----------
    a : (m, k) array_like
        An array with ``a.ndim == 2``.
    b : (n, k) array_like
        An array with ``a.ndim == 2``.

    Returns
    -------
    ua : (m, m) array
        Unitary array.
    ub : (n, n) array
        Unitary array.
    da : (m, k) array
        Diagonal array.
    db : (n, k) array
        Diagonal array.
    xt : (k, k) array
        Unitary array.

    Notes
    -----
    Required (m + n) > k

    Examples
    --------
    >>> a = np.arange(1, 13).reshape(4, 3)
    >>> b = np.arange(1, 16).reshape(5, 3)
    >>> print(a, b)
    (array([[ 1,  2,  3],
            [ 4,  5,  6],
            [ 7,  8,  9],
            [10, 11, 12]]),
     array([[ 1,  2,  3],
            [ 4,  5,  6],
            [ 7,  8,  9],
            [10, 11, 12],
            [13, 14, 15]]))
    >>> ua, ub, da, db, xt = pygsvd(a, b)
    >>> print(ua, ub, da, db, xt)
    (array([[-0.97128949, -0.06170639, -0.06241143, -0.22111957],
            [-0.15525278, -0.49259305,  0.53533804,  0.66832765],
            [ 0.17675467, -0.65858828,  0.28581634, -0.67329658],
            [ 0.03537077, -0.56551382, -0.79235536,  0.2260885 ]]),
     array([[-0.62229245, -0.11179979, -0.14217887, -0.45874262,  0.60794185],
            [ 0.60275866,  0.14278928, -0.65309333, -0.38825427,  0.19753719],
            [ 0.26576721,  0.41573534,  0.6829672 , -0.52715394,  0.1104375 ],
            [ 0.14935937, -0.81263935,  0.13667008, -0.45265433, -0.30616075],
            [-0.3955928 ,  0.36591453, -0.26101986, -0.39500204, -0.69674595]]),
     array([[0.96810387, 0.        , 0.        ],
            [0.        , 0.62489981, 0.        ],
            [0.        , 0.        , 0.3604233 ],
            [0.        , 0.        , 0.        ]]),
     array([[0.        , 0.        , 0.        ],
            [0.        , 0.        , 0.        ],
            [0.25054919, 0.        , 0.        ],
            [0.        , 0.78070495, 0.        ],
            [0.        , 0.        , 0.93278885]]),
     array([[-1.35341649e-03, -9.45897551e-01, -1.89044168e+00],
            [-1.96788902e+01, -2.25247889e+01, -2.53706876e+01],
            [-1.06649556e+01, -1.07582137e+01, -1.08514718e+01]]))
    >>> ua@da@xt
    array([[ 1.,  2.,  3.],
           [ 4.,  5.,  6.],
           [ 7.,  8.,  9.],
           [10., 11., 12.]])
    >>> ub@db@xt
    array([[ 1.,  2.,  3.],
           [ 4.,  5.,  6.],
           [ 7.,  8.,  9.],
           [10., 11., 12.],
           [13., 14., 15.]])
    >>> da.T@da + db.T@db
    array([[1., 0., 0.],
           [0., 1., 0.],
           [0., 0., 1.]])
    """
   
    m = np.vstack([a, b])
   
    # SVD(m)
    q, s, zt = np.linalg.svd(m)
   
    # CSD(q)
    u, cs, vdh = cossin(q, p=a.shape[0], q=a.shape[1], separate=False)
   
    xt = vdh.dot(np.vstack([np.diag(s), np.tile(0, [m.shape[0] - m.shape[1], m.shape[1]])])).dot(zt)[:m.shape[1], :m.shape[1]]
   
    ua = u[:a.shape[0], :a.shape[0]]
    da = cs[:a.shape[0], :a.shape[1]]
   
    ub = u[a.shape[0]:, a.shape[0]:]
    db = cs[a.shape[0]:, :a.shape[1]]
                                                                                                     
    return ua, ub, da, db, xt

if __name__ == "__main__":
    pass