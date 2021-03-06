#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 1999-2018 Alibaba Group Holding Ltd.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import numpy as np

from .... import operands
from ..utils import infer_dtype
from .core import TensorUnaryOp


class TensorExp2(operands.Exp2, TensorUnaryOp):
    def __init__(self, casting='same_kind', err=None, dtype=None, sparse=False, **kw):
        err = err if err is not None else np.geterr()
        super(TensorExp2, self).__init__(_casting=casting, _err=err,
                                         _dtype=dtype, _sparse=sparse, **kw)

    @classmethod
    def _is_sparse(cls, x):
        return False


@infer_dtype(np.exp2)
def exp2(x, out=None, where=None, **kwargs):
    """
    Calculate `2**p` for all `p` in the input tensor.

    Parameters
    ----------
    x : array_like
        Input values.
    out : Tensor, None, or tuple of tensor and None, optional
        A location into which the result is stored. If provided, it must have
        a shape that the inputs broadcast to. If not provided or `None`,
        a freshly-allocated tensor is returned. A tuple (possible only as a
        keyword argument) must have length equal to the number of outputs.
    where : array_like, optional
        Values of True indicate to calculate the ufunc at that position, values
        of False indicate to leave the value in the output alone.
    **kwargs

    Returns
    -------
    out : Tensor
        Element-wise 2 to the power `x`.

    See Also
    --------
    power

    Examples
    --------
    >>> import mars.tensor as mt

    >>> mt.exp2([2, 3]).execute()
    array([ 4.,  8.])
    """
    op = TensorExp2(**kwargs)
    return op(x, out=out, where=where)
