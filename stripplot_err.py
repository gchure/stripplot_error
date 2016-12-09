import numpy as np
import matplotlib
import matplotlib.pyplot as plt

def stripplot_err(data, yerr, axis=None, labels=None, alpha=1.0, **kwargs):
    """
    Generates a stripplot with error bars.

    Parameters
    ----------
    data : nd-array
        Data to be plotted. This may be a 1d-array or a
        multid-array in which each entry is it's own sample.
    yerr : nd-array
        Error bars to be plotted. Must be the same size and shape
        as data.
    axis : matplotlib axis object
        Axis on which to generate the plot. If None is provided,
        a new figure will be made.
    labels : nd-array, string
        X-labels for data.
    alpha : float
        Transparency value for points.
    **kwargs : matplotlib.pyplot.errorbar keyword arguments
        Includes `alpha`, `markerstyle`, etc.

    Returns
    -------
    ax : matplotlib plotting axis
        The figure canvas. This may be manipulated as normal.
    """

    def plotvals(c, data, yerr, alpha):
        x = np.random.uniform(c - 0.1, c + 0.1, size=len(data))
        if axis is None:
            plt.errorbar(x, data, yerr=yerr, fmt='o', linestyle='none',
                         alpha=alpha, **kwargs)
            ax = plt.gca()
        else:
            ax.errorbar(x, data, yerr=yerr, fmt='o', linestyle='none',
                        alpha=alpha, **kwargs)
        return ax

    # Figure out what the shape of the data is.
    if type(data[0]) == np.ndarray:
        centers = np.arange(0, len(data), 1)
        for i, c in enumerate(centers):
            ax = plotvals(c, data[i], yerr[i], alpha=alpha)
        plt.xlim(centers[0] - .5, centers[-1] + .5)
        plt.xticks(centers)
    else:
        centers = 1
        ax = plotvals(centers, data, yerr, alpha=alpha)
        plt.xlim(0, 2)
        plt.xticks([centers])
        labels = [labels]
    if labels is not None:
        ax.set_xticklabels(labels)

    return ax
