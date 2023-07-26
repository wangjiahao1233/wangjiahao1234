import numpy as np

def kalman_filter(T, Y):
    X = np.zeros_like(Y)
    X[0] = Y[0]

    P = np.zeros_like(Y)
    P[0] = 1

    Q = 1e-5

    R = 0.1

    for i in range(1, len(Y)):

        X[i] = X[i-1]
        P[i] = P[i-1] + Q

        if i % T == 0:

            K = P[i] / (P[i] + R)
            X[i] = X[i] + K * (Y[i] - X[i])
            P[i] = (1 - K) * P[i]

    return X

T = 0.1
Y = np.array([1, 2, 3, 4, 5, 6, np.nan, np.nan, np.nan, 20])


X = kalman_filter(int(1/T), Y)


print(X)