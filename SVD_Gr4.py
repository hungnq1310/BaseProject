import math

import numpy as np


def find_eigenvectors(A):
    m, n = A.shape
    k = 0
    if m < n:
        eigenValues, eigenVectors = np.linalg.eig(np.dot(A.T, A))
        k = m
    else:
        eigenValues, eigenVectors = np.linalg.eig(np.dot(A, A.T))
        k = n
    idx = eigenValues.argsort()[::-1]  # sort the eigen in descending order
    eigenValues = eigenValues[idx]
    eigenVectors = eigenVectors[:, idx]  #
    return eigenVectors, eigenValues[:k]


def find_singular_value_matrix(eigenvalues):
    sigma_values = np.sqrt(eigenvalues)
    return np.array([i for i in sigma_values if math.isnan(i) == False])


def find_normalized_eigenvectors(A, greater_size_vector, sigma_values):
    m = A.shape[0]
    n = A.shape[1]
    if m < n:
        smaller_size_vetor = np.zeros((m, m))
        for i in range(len(sigma_values)):
            smaller_size_vetor[:, i] = np.dot(A, greater_size_vector[:, i]) / sigma_values[i]
    else:
        smaller_size_vetor = np.zeros((n, n))
        for i in range(len(sigma_values)):
            smaller_size_vetor[:, i] = np.dot(A.T, greater_size_vector[:, i]) / sigma_values[i]
    return smaller_size_vetor


def svd(A):
    m = A.shape[0]
    n = A.shape[1]
    if m < n:
        V, eigenvalues = find_eigenvectors(A)
        sigma_values = find_singular_value_matrix(eigenvalues)
        U = find_normalized_eigenvectors(A, V, sigma_values)
    else:
        U, eigenvalues = find_eigenvectors(A)
        sigma_values = find_singular_value_matrix(eigenvalues)
        V = find_normalized_eigenvectors(A, U, sigma_values)
    return U, sigma_values, np.transpose(V)


def approximate_matrix(A, rank):
    U, sigma, Vh = svd(A)
    new_A = np.zeros(A.shape)
    new_A = U[:, :rank] @ np.diag(sigma[:rank]) @ Vh[:rank, :]
    error = np.sum(np.power(sigma[:rank], 2)) / np.sum(np.square(sigma))
    return new_A, error


def find_matrix_probability_error_2_norm(A, percent):
    _, eigenvalues = find_eigenvectors(A)
    sigma_values = find_singular_value_matrix(eigenvalues)
    print(sigma_values)
    rank = len(sigma_values)
    print(rank)
    for i in range(len(sigma_values)):
        if sigma_values[i] <= percent:
            rank = i - 1
            break
    print(rank)
    return approximate_matrix(A, rank)


if __name__ == '__main__':
    A = np.array([[1, 2, 3],
                  [4, 5, 6]])
    sigma = find_singular_value_matrix(find_eigenvectors(A)[1])
    print(np.diag(sigma))
