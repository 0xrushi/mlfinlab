"""
Implementation of hierarchical clustering algorithms.
"""
import numpy as np
import pandas as pd
from scipy.cluster import hierarchy

def optimal_hierarchical_cluster(mat: np.array, method: str = "ward") -> np.array:
    """
    Calculates the optimal clustering of a matrix.

    It calculates the hierarchy clusters from the distance of the matrix. Then it calculates
    the optimal leaf ordering of the hierarchy clusters, and returns the optimally clustered matrix.

    It is reproduced with modifications from the following blog post:
    `Marti, G. (2020) TF 2.0 DCGAN for 100x100 financial correlation matrices [Online].
    Available at: https://marti.ai/ml/2019/10/13/tf-dcgan-financial-correlation-matrices.html.
    (Accessed: 17 Aug 2020)
    <https://marti.ai/ml/2019/10/13/tf-dcgan-financial-correlation-matrices.html>`_

    This method relies and acts as a wrapper for the `scipy.cluster.hierarchy` module.
    `<https://docs.scipy.org/doc/scipy/reference/cluster.hierarchy.html>`_

    :param mat: (np.array/pd.DataFrame) Correlation matrix.
    :param method: (str) Method to calculate the hierarchy clusters. Can take the values
        ["single", "complete", "average", "weighted", "centroid", "median", "ward"].
    :return: (np.array) Optimal hierarchy cluster matrix.
    """

    # If input is a pandas DataFrame, convert it to a numpy array
    if isinstance(mat, pd.DataFrame):
        mat = mat.to_numpy()

    # Find the pairwise distances between the elements in the matrix
    pairwise_dists = hierarchy.distance.pdist(mat)

    # Perform hierarchical clustering using the specified method
    linkage_matrix = hierarchy.linkage(pairwise_dists, method=method)

    # Find the optimal leaf ordering
    optimal_leaf_order = hierarchy.leaves_list(hierarchy.optimal_leaf_ordering(linkage_matrix, pairwise_dists))

    # Reorder the matrix according to the optimal leaf ordering
    optimal_cluster_mat = mat[optimal_leaf_order, :][:, optimal_leaf_order]

    return optimal_cluster_mat
