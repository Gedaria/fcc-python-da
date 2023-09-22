import numpy as np


def calculate(input_list):
    if len(input_list) < 9:
        raise ValueError("List must contain nine numbers.")

    input_matrix = np.reshape(input_list, (3, 3))

    calculations = {
        "mean": [
            np.mean(input_matrix, axis=0).tolist(),
            np.mean(input_matrix, axis=1).tolist(),
            np.mean(input_matrix),
        ],
        "variance": [
            np.var(input_matrix, axis=0).tolist(),
            np.var(input_matrix, axis=1).tolist(),
            np.var(input_matrix),
        ],
        "standard deviation": [
            np.std(input_matrix, axis=0).tolist(),
            np.std(input_matrix, axis=1).tolist(),
            np.std(input_matrix),
        ],
        "max": [
            np.max(input_matrix, axis=0).tolist(),
            np.max(input_matrix, axis=1).tolist(),
            np.max(input_matrix),
        ],
        "min": [
            np.min(input_matrix, axis=0).tolist(),
            np.min(input_matrix, axis=1).tolist(),
            np.min(input_matrix),
        ],
        "sum": [
            np.sum(input_matrix, axis=0).tolist(),
            np.sum(input_matrix, axis=1).tolist(),
            np.sum(input_matrix),
        ],
    }

    return calculations
