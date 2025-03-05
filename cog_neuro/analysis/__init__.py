"""
Statistical and computational analysis methods for neuroscience data.

This module provides functions and classes for analyzing neuroscience data,
including functional connectivity, statistical analysis, and machine learning.
"""

from .functional_connectivity import compute_correlation_matrix, plot_matrix

__all__ = ["compute_correlation_matrix", "plot_matrix"]
