import numpy as np


def _transform(data: np.ndarray, mean: np.ndarray, std: np.ndarray, inverse: bool = False) -> np.ndarray:
    """A transformation function to normalize or denormalize data

    Author: Jiangtao Liu

    Parameters
    ----------
    data : np.ndarray
        The data to be transformed
    mean : np.ndarray
        The mean of the data
    std : np.ndarray
        The standard deviation of the data
    inverse : bool, optional
        A flag to indicate if the transformation is inverse, by default False

    Returns
    -------
    np.ndarray
        The transformed data
    """
    if inverse:
        return data * std + mean
    else:
        return (data - mean) / std


def _calc_stats(data: np.ndarray, axis: int = 0) -> tuple[np.ndarray, np.ndarray]:
    """A function to calculate the mean and standard deviation of the data

    Author: Jiangtao Liu

    Parameters
    ----------
    data : np.ndarray
        The data to calculate stats from
    axis : int, optional
        The axis to calculate the stats, by default 0

    Returns
    -------
    tuple[np.ndarray, np.ndarray]
        The mean and standard deviation of the data
    """
    mean = np.nanmean(data, axis=axis).astype(float)
    std = np.nanstd(data, axis=axis).astype(float)
    std = np.maximum(std, 0.001)  # Ensuring std is not too small
    return mean, std
