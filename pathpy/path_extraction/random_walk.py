# -*- coding: utf-8 -*-

#    pathpy is an OpenSource python package for the analysis of time series data
#    on networks using higher- and multi order graphical models.
#
#    Copyright (C) 2016-2018 Ingo Scholtes, ETH Zürich/Universität Zürich
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program. If not, see <http://www.gnu.org/licenses/>.
#
#    Contact the developer:
#
#    E-mail: scholtes@ifi.uzh.ch
#    Web:    http://www.ingoscholtes.net

import collections as _co
import random

import numpy as _np

from pathpy.utils import Log, Severity
from pathpy.classes.network import Network
from pathpy.classes.paths import Paths
from pathpy import algorithms

def random_walk(network, l, n=1, start_node=None):
    """
    [DEPRECATED]
    Generates n paths of a random walker in the given network
    and returns them as a paths object.
    Each path has a length of l steps.
    Parameters
    ----------
    network: Network, TemporalNetwork, HigherOrderNetwork
        The network structure on which the random walks will be simulated.
    int: l
        The (maximum) length of each random walk path. A path will
        terminate if a node with outdegree zero is reached.
    int: n
        The number of random walk paths to generate.
    """
    Log.add('The path_extraction.random_walk function is deprecated. Please use paths_from_random_walk instead.', Severity.WARNING)
    return paths_from_random_walk(network, l, n, start_node)


def paths_from_random_walk(network, l, n=1, start_node=None):
    """
    Generates n paths of a random walker in the given network
    and returns them as a paths object.
    Each path has a length of l steps.
    Parameters
    ----------
    network: Network, TemporalNetwork, HigherOrderNetwork
        The network structure on which the random walks will be simulated.
    int: l
        The (maximum) length of each random walk path. A path will
        terminate if a node with outdegree zero is reached.
    int: n
        The number of random walk paths to generate.
    """
    p = Paths()
    for i in range(n):
        path = algorithms.random_walk.generate_walk(network, l, start_node)
        p.add_path(tuple(path))
    return p

def random_paths(network, p):
    """
    Generates Markovian paths of a random walker in a given network
    and returns them as a paths object.
    Parameters
    ----------
    network: Network
        The network structure on which the random walks will be simulated.
    paths: Paths
        ...
    """
    p_rnd = Paths()
    for l in p.paths:
        for path in p.paths[l]:
            if p.paths[l][path][1] > 0:
                p_rnd += paths_from_random_walk(network, l, int(p.paths[l][path][1]), path[0])
    return p_rnd