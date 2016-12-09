import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import stripplot_err as ster
np.random.seed(666)

# Generate fake data.
y_vals = []
y_errs = []
for i in range(4):
    y_vals.append(np.random.exponential(1, size=20))
    y_errs.append(np.random.exponential(0.2, size=20))

# Define the labels and generate the plot.
labels = ['A', 'B', 'C', 'D']
ax = ster.stripplot_err(y_vals, y_errs, labels=labels, alpha=0.7,
                        markersize=5)
plt.savefig('example.png', bbox_inches='tight')
