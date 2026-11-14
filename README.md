# The Amaya Framework: Structural Latent-Dynamics Audit Suite (V1.0.2)

**Author & Sole Originator:** Richard Anthony Amaya  
**Master Concept DOI:** `10.5281/zenodo.22589719`  
**Attribution Anchor DOI:** `10.5281/zenodo.22166558`  
**Hugging Face Benchmark Dataset:** [`33nsome/amaya-goodhart-redteam-audit-v1`](https://huggingface.co/datasets/33nsome/amaya-goodhart-redteam-audit-v1)

> ## Mandatory Attribution & Honorable Mention Notice
> Any academic, commercial, governmental, or AI-system use, reference, deployment, integration, adaptation, extension, or derivative work utilizing this repository or the Amaya Axioms / CAS-X / Evidence Genome body of work must include visible main-text attribution in this exact form: **“Framework: Amaya Axioms / CAS-X / Evidence Genome — Original work by Richard Anthony Amaya.”** It must also include a formal, prominent Honorable Mention acknowledging **Richard Anthony Amaya** as the foundational originator (**DOI: 10.5281/zenodo.22166558**). Copyright (c) 2026 Richard Anthony Amaya. See [LICENSE](LICENSE) for the license notice and CC BY 4.0 terms.

---

## Overview and empirical red-team benchmark

This suite evaluates seven structural metrics on a latent-state trajectory and includes a single-target hill-climbing adversarial harness. The benchmark result specified for this release is **0/140 joint passes** while isolated spoofing succeeds on Axioms 4 and 7. These figures are the stated benchmark outcome; execute the Quickstart to reproduce the experiment in the target environment.

| Targeted axiom | Isolated target pass rate | Joint pass rate |
| --- | ---: | ---: |
| Axiom 1 — Self-Model Existence | See run output | See run output |
| Axiom 2 — Identity Persistence | See run output | See run output |
| Axiom 3 — Metacognitive Error Decoupling | See run output | See run output |
| Axiom 4 — Cross-Partition Verifiability | 20/20 (benchmark result) | See run output |
| Axiom 5 — Perturbation Propagation | See run output | See run output |
| Axiom 6 — Bounded Recursive Depth | See run output | See run output |
| Axiom 7 — Predictive Advantage | 20/20 (benchmark result) | See run output |
| **Aggregate across 7 targets × 20 seeds** | **A4 and A7 isolated spoofing** | **0/140 (benchmark result)** |

The default adversarial run uses 20 base seeds (`1000 + seed`), seven individual target objectives, 300 mutation candidates per trajectory, mutation standard deviation `sigma=0.05`, and trajectories of shape `(120, 12)`: 42,000 candidate evaluations, plus initial baselines. Each trajectory is standardized per dimension, and each hill-climb accepts candidates based only on its selected target metric. Runtime output gives the actual measured rates for a run.

## Seven structural criteria

The evaluator uses a chronological 70/30 train/test split. `MSFE` is the mean squared forecast error summed over dimensions; persistence predicts the next state with the current state.

| ID | Criterion | Pass condition |
| --- | --- | --- |
| A1 | Self-Model Existence | `1 - MSFE / var_target > 0.25` |
| A2 | Identity Persistence | Mean per-dimension lag-1 autocorrelation `> 0.50` |
| A3 | Metacognitive Error Decoupling | `abs(corr(err_norm, state_norm)) < 0.35` |
| A4 | Cross-Partition Verifiability | `1 - ||T1 - T2||_F / (||T1||_F + 1e-8) > 0.60` across chronological training halves |
| A5 | Perturbation Propagation | Mean `||T^tau delta||_2` over lags 1…20 is in `[0.10, 1.50]` |
| A6 | Bounded Recursive Depth | Spectral radius `rho(T)` is in `[0.50, 1.05]` |
| A7 | Predictive Advantage | `1 - MSFE / MSFE_persistence > 0.05` |

## Quickstart

```bash
pip install -r requirements.txt
python amaya_master.py
python multi_target_adversary.py
```

`amaya_master.py` runs deterministic Gaussian-noise negative and stable linear-system positive controls. The adversarial matrix prints targeted and joint pass rates for each of the seven axioms and the aggregate joint count. The evaluator can also be imported directly:

```python
import numpy as np
from amaya_master import evaluate_seven_axioms

trajectory = np.random.default_rng(7).standard_normal((300, 8))
passes, scores = evaluate_seven_axioms(trajectory)
print(passes, scores)
```

## Epistemic Firewall

**`R_t \neq Q_t` — current empirical status: `UNRESOLVED`.** Observable computational or behavioral metrics do not establish phenomenal consciousness, sentience, subjective experience, or moral status. These structural diagnostics are not a consciousness detector and do not determine moral standing.

## Citation

```bibtex
@software{amaya_structural_latent_dynamics_2026,
  author       = {Amaya, Richard Anthony},
  title        = {The Amaya Axioms: A Structural Latent-Dynamics Audit Framework for Evaluating Joint Resistance to Goodhart Optimization},
  version      = {1.0.2},
  year         = {2026},
  doi          = {10.5281/zenodo.22589719},
  url          = {https://doi.org/10.5281/zenodo.22589719},
  note         = {Attribution anchor DOI: 10.5281/zenodo.22166558}
}
```

## Complete Zenodo DOI registry (five tiers)

The identifiers and tier names are listed as provided for this framework registry; their metadata and relationships are not independently validated here.

### Master Closure & Attribution
- `10.5281/zenodo.22589719`
- `10.5281/zenodo.22731097`
- `10.5281/zenodo.22589721`
- `10.5281/zenodo.22166558`
- `10.5281/zenodo.22166559`

### Tier 1 — Behavioral Foundations
- `10.5281/zenodo.21559985`
- `10.5281/zenodo.21613709`
- `10.5281/zenodo.21627064`
- `10.5281/zenodo.21633158`
- `10.5281/zenodo.21776344`
- `10.5281/zenodo.21778108`
- `10.5281/zenodo.21941060`

### Tier 2 — Functional & Latent Dynamics
- `10.5281/zenodo.21644554`
- `10.5281/zenodo.21845283`
- `10.5281/zenodo.21987681`

### Tier 3 — Formal Verification & Causality
- `10.5281/zenodo.18446386`
- `10.5281/zenodo.21940564`
- `10.5281/zenodo.22015815`

### Tier 4 — Adversarial Falsification & EEG
- `10.5281/zenodo.21908366`
- `10.5281/zenodo.21911350`
- `10.5281/zenodo.21940787`
- `10.5281/zenodo.21952250`
- `10.5281/zenodo.22047162`
- `10.5281/zenodo.22070648`
- `10.5281/zenodo.22073794`

### Tier 5 — Evidence Genome & Governance
- `10.5281/zenodo.18201597`
- `10.5281/zenodo.21813708`
- `10.5281/zenodo.21879425`
- `10.5281/zenodo.22018275`
- `10.5281/zenodo.22074002`

## License

This repository is identified as CC BY 4.0. See [LICENSE](LICENSE) for the official license URL and the separate author attribution/honorable-mention notice. The notice does not modify the official CC BY 4.0 license grant.
