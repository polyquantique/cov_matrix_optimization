## Code for computing the covariance matrix decomposition shown in ["Classical algorithm for simulating experimental Gaussian boson sampling"](https://arxiv.org/abs/2306.03709).

* `get_decompostion.py` contains the original code used by Changhun Oh et al.. This file uses the 'CVXOPT' solver by default.
* `opt_cov_example.py` contains a slight modification of the original code. In particular, it shows an error when using 'CVXOPT' for large covariance matrices. It also has the option to change the solver to 'SCS'.
* `cov_0.npy` contains an array of shape (200, 200). This array corresponds to the covariance matrix of the ground truth of the Jiuzhang 1.0 experiment.
* `requirements.txt` contains all the requirements to run these files.
