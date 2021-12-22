import numpy as np


def calculate(list1):
    if len(list1) < 9:
        raise ValueError('List must contain nine numbers.')

    list_array = np.array(list1)
    a = list_array.reshape(3, 3)

    calculations = dict()
    columns_means = []
    row_means = []

    row_variances = []
    column_variances = []

    row_std = []
    column_std = []

    row_max = []
    col_max = []

    col_min = []
    row_min = []

    row_sum = []
    col_sum = []

    for i in range(3):
        row_means.append(a[:, i].mean())
        columns_means.append(a[i].mean())

        row_variances.append(a[:, i].var())
        column_variances.append(a[i].var())

        row_std.append(a[:, i].std())
        column_std.append(a[i].std())

        row_max.append(a[:, i].max())
        col_max.append(a[i].max())

        row_min.append(a[:, i].min())
        col_min.append(a[i].min())

        row_sum.append(a[:, i].sum())
        col_sum.append(a[i].sum())

    calculations['mean'] = [row_means, columns_means, list_array.mean()]
    calculations['variance'] = [row_variances, column_variances, list_array.var()]
    calculations['standard deviation'] = [row_std, column_std, list_array.std()]
    calculations['max'] = [row_max, col_max, list_array.max()]
    calculations['min'] = [row_min, col_min, list_array.min()]
    calculations['sum'] = [row_sum, col_sum, list_array.sum()]

    return calculations
