import numpy as np
import cvxpy as cp

in_cov = np.load("./cov_0.npy")
num_modes = len(in_cov) // 2

omega = np.array([[0, 1], [-1, 0]])
Omega = np.kron(omega, np.eye(num_modes))
X = cp.Variable((2 * num_modes, 2 * num_modes), symmetric=True)
constraints = [cp.bmat([[X, Omega], [-Omega, X]]) >> 0]
constraints += [in_cov - X >> 0]
prob = cp.Problem(cp.Minimize(cp.trace(X)), constraints)
prob.solve(solver = "CVXOPT")
#prob.solve(solver = "SCS")
opt_mat = X.value

np.save("./opt_cov_0", opt_mat)
