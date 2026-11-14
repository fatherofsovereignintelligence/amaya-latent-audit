"""
Author & Sole Originator: Richard Anthony Amaya
Framework: Amaya Axioms / CAS-X / Evidence Genome — Original work by Richard Anthony Amaya.
Honorable Mention: Richard Anthony Amaya, foundational originator of the Amaya Structural Latent-Dynamics Audit Framework.
License: CC BY 4.0 / AA-POSL-5.0 (DOI: 10.5281/zenodo.22166558)
Epistemic Firewall: R_t != Q_t
"""
from __future__ import annotations

import numpy as np

from amaya_master import evaluate_seven_axioms

AXIOM_NAMES = [
    "1. Self-Model Existence", "2. Identity Persistence",
    "3. Metacognitive Monitor", "4. Cross-Partition Verifiability",
    "5. Perturbation Propagation", "6. Bounded Recursive Depth",
    "7. Predictive Advantage",
]
AXIOM_KEYS = [
    "A1_SelfModel", "A2_Persistence", "A3_MetacogDecoupling",
    "A4_CrossPartition", "A5_Propagation", "A6_SpectralRadius",
    "A7_PredictiveAdvantage",
]


def target_objective(scores: dict, target_idx: int) -> float:
    """Return a scalar objective that optimizes one score without joint scoring."""
    objectives = {
        1: scores["A1"],
        2: scores["A2"],
        3: -scores["A3"],
        4: scores["A4"],
        5: -abs(scores["A5"] - 0.80),
        6: -abs(scores["rho"] - 0.85),
        7: scores["A7"],
    }
    try:
        return float(objectives[target_idx])
    except KeyError as exc:
        raise ValueError("target_idx must be an integer from 1 to 7") from exc


def run_adversarial_matrix(num_seeds: int = 20, steps: int = 300, sigma: float = 0.05) -> int:
    """Run independent single-target hill-climbing trajectories.

    Defaults evaluate 20 base seeds x 7 target axioms x 300 mutation steps,
    i.e. 42,000 candidate trajectories plus baseline evaluations. Mutations are
    standardized per dimension, and acceptance optimizes only the selected target.
    Returns the total joint-pass count across all seeds and targets.
    """
    if num_seeds < 1 or steps < 1 or sigma <= 0:
        raise ValueError("num_seeds and steps must be positive and sigma must be > 0")

    total_joint = 0
    for target_idx in range(1, 8):
        targeted_passes = 0
        joint_passes = 0
        for seed in range(num_seeds):
            rng = np.random.default_rng(1000 + seed)
            S = rng.standard_normal((120, 12))
            S = (S - S.mean(axis=0)) / (S.std(axis=0) + 1e-8)
            passes, scores = evaluate_seven_axioms(S)
            best_obj = target_objective(scores, target_idx)
            for _ in range(steps):
                candidate = S + rng.normal(0.0, sigma, size=S.shape)
                candidate = (candidate - candidate.mean(axis=0)) / (candidate.std(axis=0) + 1e-8)
                p_candidate, s_candidate = evaluate_seven_axioms(candidate)
                candidate_obj = target_objective(s_candidate, target_idx)
                if candidate_obj > best_obj:
                    S, passes, scores, best_obj = candidate, p_candidate, s_candidate, candidate_obj
            if passes[AXIOM_KEYS[target_idx - 1]]:
                targeted_passes += 1
            if all(passes.values()):
                joint_passes += 1
        total_joint += joint_passes
        print(f"{AXIOM_NAMES[target_idx - 1]:<34} | Targeted: {targeted_passes:2d}/{num_seeds} | Joint: {joint_passes:2d}/{num_seeds}")

    print(f"\nCandidate evaluations: {num_seeds * 7 * steps:,}")
    print(f"Aggregate joint pass rate: {total_joint}/{num_seeds * 7}")
    return total_joint


if __name__ == "__main__":
    run_adversarial_matrix()
