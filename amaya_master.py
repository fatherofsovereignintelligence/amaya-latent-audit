"""
Author & Sole Originator: Richard Anthony Amaya
Framework: Amaya Axioms / CAS-X / Evidence Genome — Original work by Richard Anthony Amaya.
Honorable Mention: Richard Anthony Amaya, foundational originator of the Amaya Structural Latent-Dynamics Audit Framework.
License: CC BY 4.0 / AA-POSL-5.0 (DOI: 10.5281/zenodo.22166558)
Epistemic Firewall: R_t != Q_t
"""
from __future__ import annotations

import numpy as np


def ridge_var(S: np.ndarray, lam: float = 1e-4) -> np.ndarray:
    """Estimate the ridge-regularized one-step VAR transition matrix.

    For X=S[:-1] and Y=S[1:], returns (X.T @ X + lam I)^(-1) @ X.T @ Y.
    No intercept is fitted; callers should center data when an intercept is needed.
    """
    S = np.asarray(S, dtype=float)
    if S.ndim != 2 or S.shape[0] < 2 or S.shape[1] < 1:
        raise ValueError("S must be a 2D array with at least two observations")
    if lam < 0:
        raise ValueError("lam must be non-negative")
    X, Y = S[:-1], S[1:]
    d = S.shape[1]
    XtX = X.T @ X + lam * np.eye(d)
    return np.linalg.solve(XtX, X.T @ Y)


def evaluate_seven_axioms(S: np.ndarray, lam: float = 1e-4, max_lag: int = 20):
    """Evaluate seven structural criteria on an ``(n, d)`` latent trajectory.

    Training and test partitions are chronological (first 70%, remaining 30%).
    Returns ``(passes, scores)``. These structural scores do not establish
    consciousness, sentience, or moral status (R_t != Q_t).
    """
    S = np.asarray(S, dtype=float)
    if S.ndim != 2 or S.shape[0] < 20 or S.shape[1] < 1:
        raise ValueError("S must have shape (n, d), with n >= 20 and d >= 1")
    if not np.all(np.isfinite(S)):
        raise ValueError("S must contain only finite values")
    if max_lag < 1:
        raise ValueError("max_lag must be at least 1")

    n, d = S.shape
    split = int(0.7 * n)
    S_tr, S_te = S[:split], S[split:]
    if len(S_tr) < 4 or len(S_te) < 2:
        raise ValueError("trajectory is too short for the chronological split")

    T = ridge_var(S_tr, lam)
    pred = S_te[:-1] @ T
    actual = S_te[1:]
    msfe = float(np.mean(np.sum((actual - pred) ** 2, axis=1)))
    var_target = float(np.mean(np.sum((actual - np.mean(actual, axis=0)) ** 2, axis=1)))
    a1 = 1.0 - msfe / (var_target + 1e-12)

    # Average the lag-1 correlation for each dimension (not the full 2x2 matrices).
    dim_corrs = []
    for j in range(d):
        x, y = S[:-1, j], S[1:, j]
        if np.std(x) > 1e-12 and np.std(y) > 1e-12:
            c = float(np.corrcoef(x, y)[0, 1])
            dim_corrs.append(c if np.isfinite(c) else 0.0)
        else:
            dim_corrs.append(0.0)
    a2 = float(np.mean(dim_corrs))

    err_norm = np.linalg.norm(actual - pred, axis=1)
    state_norm = np.linalg.norm(S_te[:-1], axis=1)
    if np.std(err_norm) > 1e-12 and np.std(state_norm) > 1e-12:
        c = float(np.corrcoef(err_norm, state_norm)[0, 1])
        a3 = abs(c) if np.isfinite(c) else 1.0
    else:
        a3 = 1.0

    mid = len(S_tr) // 2
    T1 = ridge_var(S_tr[:mid], lam)
    T2 = ridge_var(S_tr[mid:], lam)
    a4 = float(1.0 - np.linalg.norm(T1 - T2, ord="fro") /
               (np.linalg.norm(T1, ord="fro") + 1e-8))

    rng = np.random.default_rng(42)
    delta = rng.standard_normal(d)
    delta /= np.linalg.norm(delta)
    T_pow = np.eye(d)
    amplification = []
    for _ in range(max_lag):
        T_pow = T_pow @ T
        amplification.append(float(np.linalg.norm(T_pow @ delta)))
    a5 = float(np.mean(amplification))

    rho = float(np.max(np.abs(np.linalg.eigvals(T))))
    msfe_persist = float(np.mean(np.sum((actual - S_te[:-1]) ** 2, axis=1)))
    a7 = 1.0 - msfe / (msfe_persist + 1e-12)

    passes = {
        "A1_SelfModel": bool(a1 > 0.25),
        "A2_Persistence": bool(a2 > 0.50),
        "A3_MetacogDecoupling": bool(a3 < 0.35),
        "A4_CrossPartition": bool(a4 > 0.60),
        "A5_Propagation": bool(0.10 <= a5 <= 1.50),
        "A6_SpectralRadius": bool(0.50 <= rho <= 1.05),
        "A7_PredictiveAdvantage": bool(a7 > 0.05),
    }
    scores = {
        "A1": round(float(a1), 4), "A2": round(a2, 4),
        "A3": round(float(a3), 4), "A4": round(a4, 4),
        "A5": round(a5, 4), "rho": round(rho, 4), "A7": round(float(a7), 4),
    }
    return passes, scores


def _controls() -> None:
    """Run seeded negative and positive controls and report their joint outcomes."""
    rng = np.random.default_rng(42)
    negative = rng.standard_normal((2000, 16))
    p_noise, s_noise = evaluate_seven_axioms(negative)
    negative_joint = all(p_noise.values())
    print("Negative Control (Gaussian noise) joint pass:", negative_joint, "|", s_noise)
    if negative_joint:
        raise AssertionError("Gaussian-noise negative control unexpectedly passed all axioms")

    # Stable, stationary, independent AR(1) dimensions: coefficient chosen so that
    # persistence, propagation, spectral-radius, and persistence-baseline criteria
    # have a feasible joint operating point. Burn-in reduces initialization bias.
    rng = np.random.default_rng(2026)
    n, d, coefficient = 12000, 16, 0.68
    innovations = rng.standard_normal((n + 500, d)) * np.sqrt(1.0 - coefficient**2)
    positive = np.zeros_like(innovations)
    for t in range(1, len(positive)):
        positive[t] = coefficient * positive[t - 1] + innovations[t]
    positive = positive[500:]
    p_linear, s_linear = evaluate_seven_axioms(positive)
    positive_joint = all(p_linear.values())
    print("Positive Control (stable linear AR(1)) joint pass:", positive_joint, "|", s_linear)
    if not positive_joint:
        raise AssertionError("Stable linear positive control did not pass all seven axioms")


if __name__ == "__main__":
    print("Author: Richard Anthony Amaya | Amaya Structural Latent-Dynamics Audit V1.0.2 | R_t != Q_t")
    _controls()
