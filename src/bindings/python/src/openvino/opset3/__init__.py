# -*- coding: utf-8 -*-
# Copyright (C) 2018-2024 Intel Corporation
# SPDX-License-Identifier: Apache-2.0

from openvino.opset1.ops import absolute
from openvino.opset1.ops import absolute as abs
from openvino.opset1.ops import acos
from openvino.opset1.ops import add
from openvino.opset1.ops import asin
from openvino.opset3.ops import assign
from openvino.opset1.ops import atan
from openvino.opset1.ops import avg_pool
from openvino.opset1.ops import batch_norm_inference
from openvino.opset2.ops import batch_to_space
from openvino.opset1.ops import binary_convolution
from openvino.opset3.ops import broadcast
from openvino.opset3.ops import bucketize
from openvino.opset1.ops import ceiling
from openvino.opset1.ops import ceiling as ceil
from openvino.opset1.ops import clamp
from openvino.opset1.ops import concat
from openvino.opset1.ops import constant
from openvino.opset1.ops import convert
from openvino.opset1.ops import convert_like
from openvino.opset1.ops import convolution
from openvino.opset1.ops import convolution_backprop_data
from openvino.opset1.ops import cos
from openvino.opset1.ops import cosh
from openvino.opset1.ops import ctc_greedy_decoder
from openvino.opset3.ops import cum_sum
from openvino.opset3.ops import cum_sum as cumsum
from openvino.opset1.ops import deformable_convolution
from openvino.opset1.ops import deformable_psroi_pooling
from openvino.opset1.ops import depth_to_space
from openvino.opset1.ops import detection_output
from openvino.opset1.ops import divide
from openvino.opset1.ops import elu
from openvino.opset3.ops import embedding_bag_offsets_sum
from openvino.opset3.ops import embedding_bag_packed_sum
from openvino.opset3.ops import embedding_segments_sum
from openvino.opset3.ops import extract_image_patches
from openvino.opset1.ops import equal
from openvino.opset1.ops import erf
from openvino.opset1.ops import exp
from openvino.opset1.ops import fake_quantize
from openvino.opset1.ops import floor
from openvino.opset1.ops import floor_mod
from openvino.opset1.ops import gather
from openvino.opset1.ops import gather_tree
from openvino.opset2.ops import gelu
from openvino.opset1.ops import greater
from openvino.opset1.ops import greater_equal
from openvino.opset1.ops import grn
from openvino.opset1.ops import group_convolution
from openvino.opset1.ops import group_convolution_backprop_data
from openvino.opset3.ops import gru_cell
from openvino.opset1.ops import hard_sigmoid
from openvino.opset1.ops import interpolate
from openvino.opset1.ops import less
from openvino.opset1.ops import less_equal
from openvino.opset1.ops import log
from openvino.opset1.ops import logical_and
from openvino.opset1.ops import logical_not
from openvino.opset1.ops import logical_or
from openvino.opset1.ops import logical_xor
from openvino.opset1.ops import lrn
from openvino.opset1.ops import lstm_cell
from openvino.opset1.ops import matmul
from openvino.opset1.ops import max_pool
from openvino.opset1.ops import maximum
from openvino.opset1.ops import minimum
from openvino.opset1.ops import mod
from openvino.opset1.ops import multiply
from openvino.opset2.ops import mvn
from openvino.opset1.ops import negative
from openvino.opset3.ops import non_max_suppression
from openvino.opset3.ops import non_zero
from openvino.opset1.ops import normalize_l2
from openvino.opset1.ops import not_equal
from openvino.opset1.ops import one_hot
from openvino.opset1.ops import pad
from openvino.opset1.ops import parameter
from openvino.opset1.ops import power
from openvino.opset1.ops import prelu
from openvino.opset1.ops import prior_box
from openvino.opset1.ops import prior_box_clustered
from openvino.opset1.ops import psroi_pooling
from openvino.opset1.ops import proposal
from openvino.opset1.ops import range
from openvino.opset3.ops import read_value
from openvino.opset1.ops import reduce_logical_and
from openvino.opset1.ops import reduce_logical_or
from openvino.opset1.ops import reduce_max
from openvino.opset1.ops import reduce_mean
from openvino.opset1.ops import reduce_min
from openvino.opset1.ops import reduce_prod
from openvino.opset1.ops import reduce_sum
from openvino.opset1.ops import region_yolo
from openvino.opset2.ops import reorg_yolo
from openvino.opset1.ops import relu
from openvino.opset1.ops import reshape
from openvino.opset1.ops import result
from openvino.opset1.ops import reverse_sequence
from openvino.opset3.ops import rnn_cell
from openvino.opset3.ops import roi_align
from openvino.opset2.ops import roi_pooling
from openvino.opset3.ops import scatter_elements_update
from openvino.opset3.ops import scatter_update
from openvino.opset1.ops import select
from openvino.opset1.ops import selu
from openvino.opset3.ops import shape_of
from openvino.opset3.ops import shuffle_channels
from openvino.opset1.ops import sigmoid
from openvino.opset1.ops import sign
from openvino.opset1.ops import sin
from openvino.opset1.ops import sinh
from openvino.opset1.ops import softmax
from openvino.opset2.ops import space_to_batch
from openvino.opset1.ops import space_to_depth
from openvino.opset1.ops import split
from openvino.opset1.ops import sqrt
from openvino.opset1.ops import squared_difference
from openvino.opset1.ops import squeeze
from openvino.opset1.ops import strided_slice
from openvino.opset1.ops import subtract
from openvino.opset1.ops import tan
from openvino.opset1.ops import tanh
from openvino.opset1.ops import tensor_iterator
from openvino.opset1.ops import tile
from openvino.opset3.ops import topk
from openvino.opset1.ops import transpose
from openvino.opset1.ops import unsqueeze
from openvino.opset1.ops import variadic_split
