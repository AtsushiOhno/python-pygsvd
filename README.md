# `python-pygsvd`

A python package of generalized singular value decomposition.

## Overview

`pygsvd` gives generalized singular value decomposition of matrices a(m, k) and b(n, k) as follows.

```
a = ua @ da @ xt
b = ub @ db @ xt

where
- (m + n) > k
- ua, ub and xt are unitary
- da and db is diagonal
- da.T@da + db.T@da = I
```

## Install

You can install `pygsvd` by executing one of the following.

```shell
 $ pip install git+https://github.com/AtsushiOhno/python-pygsvd
 ```

 ```shell
 $ pip install .
 ```

 ## Usage

Given a pair of numpy ndarrays 'a' and 'b', pygsvd computes its GSVD.

 ```python
from pygsvd import pygsvd

# GSVD of 'a' and 'b'.
ua, ub, da, db, xt = pygsvd(a, b)
 ```

## Example

```python
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
```