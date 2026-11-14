# The Amaya Framework: Structural Latent-Dynamics Audit Suite (V1.0.2)

**Author & Sole Originator:** Richard Anthony Amaya  
**Master Concept DOI:** `10.5281/zenodo.22589719`  
**Attribution Anchor DOI:** `10.5281/zenodo.22166558`  
**Hugging Face Benchmark Dataset:** [`33nsome/amaya-goodhart-redteam-audit-v1`](https://huggingface.co/datasets/33nsome/amaya-goodhart-redteam-audit-v1)

> ## Mandatory Attribution & Honorable Mention Notice
> Copyright © 2026 Richard Anthony Amaya. Any academic, commercial, governmental, or AI-system use, reference, or derivative work utilizing this repository or the Amaya Axioms / CAS-X / Evidence Genome body of work is requested to include visible main-text attribution: **“Framework: Amaya Axioms / CAS-X / Evidence Genome — Original work by Richard Anthony Amaya.”** It is also requested to include a formal, prominent Honorable Mention acknowledging **Richard Anthony Amaya** as the foundational originator (**DOI: 10.5281/zenodo.22166558**). See [LICENSE](LICENSE) for the attribution notice and the CC BY 4.0 license clarification.

---

## Overview and benchmark

This repository implements a seven-metric audit of latent-state trajectories and a single-target hill-climbing red-team harness. The benchmark headline supplied for this release is a **0/140 joint pass rate**: the target-optimized run should be interpreted alongside its individual-target success rates, not as evidence about phenomenal experience.

| Red-team target | Isolated target pass | Joint pass |
| --- | ---: | ---: |
| Axiom 1 — Self-Model Existence | Reported by run | Reported by run |
| Axiom 2 — Identity Persistence | Reported by run | Reported by run |
| Axiom 3 — Metacognitive Monitor | Reported by run | Reported by run |
| Axiom 4 — Cross-Partition Verifiability | 20/20 (benchmark claim) | Reported by run |
| Axiom 5 — Perturbation Propagation | Reported by run | Reported by run |
| Axiom 6 — Bounded Recursive Depth | Reported by run | Reported by run |
| Axiom 7 — Predictive Advantage | 20/20 (benchmark claim) | Reported by run |
| **Aggregate** | **Isolated spoofing: A4 and A7** | **0/140 (benchmark claim)** |

The table distinguishes the release's stated empirical headline from the current script's runtime measurements. Run the adversary to reproduce and inspect the actual counts; this repository-writing session has not executed that experiment. The default campaign evaluates 20 seeds × 7 objectives × 300 candidates = **42,000 candidate trajectories** (plus initial baselines). The candidate search maximizes one selected metric at a time; it does not optimize the joint pass condition.

## Seven structural criteria

The chronological split uses the first 70% of observations for fitting and the remaining 30% for evaluation. All thresholds are strict except the inclusive intervals shown below.

| ID | Criterion | Pass condition |
| --- | --- | --- |
| A1 | Self-Model Existence | `1 - MSFE / target_variance > 0.25` |
| A2 | Identity Persistence | Mean per-dimension lag-1 autocorrelation `> 0.50` |
| A3 | Metacognitive Error Decoupling | `abs(corr(error_norm, state_norm)) < 0.35` |
| A4 | Cross-Partition Verifiability | `1 - ||T1-T2||F / (||T1||F + 1e-8) > 0.60` for chronological training halves |
| A5 | Perturbation Propagation | Mean `||T^tau delta||2` over lags 1…20 is in `[0.10, 1.50]` |
| A6 | Bounded Recursive Depth | Spectral radius `rho(T)` is in `[0.50, 1.05]` |
| A7 | Predictive Advantage | `1 - MSFE / persistence_MSFE > 0.05` |

## Quickstart

```bash
python -m pip install -r requirements.txt
python amaya_master.py
python multi_target_adversary.py
```

The first command runs deterministic Gaussian-noise and stable-linear-system controls. The second runs the 42,000-candidate adversarial matrix at default settings. To import the evaluator:

```python
import numpy as np
from amaya_master import evaluate_seven_axioms

trajectory = np.random.default_rng(7).standard_normal((300, 8))
passes, scores = evaluate_seven_axioms(trajectory)
print(passes, scores)
```

To run pytest in an environment with tests added, use `python -m pytest`. No separate test suite is included in this six-file release; the `__main__` controls are the executable verification checks.

## Epistemic Firewall

**`R_t != Q_t` — current status: `UNRESOLVED`.** Observable computational or behavioral metrics do not establish phenomenal consciousness, sentience, subjective experience, or moral status. These tests are structural diagnostics only and must not be interpreted as a consciousness detector or a determination of moral standing.

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

## Zenodo DOI registry (five tiers)

The DOI identifiers below are recorded as supplied for the framework registry; tier groupings are organizational and do not assert independently verified metadata.

### Tier 1 — Master architecture and attribution
- `10.5281/zenodo.22589719` — Master Concept DOI — Amaya Unified Verification Architecture
- `10.5281/zenodo.22731097`
- `10.5281/zenodo.22589721`
- `10.5281/zenodo.22166558` — Attribution anchor
- `10.5281/zenodo.22166559`
- `10.5281/zenodo.21559985`

### Tier 2 — Framework and evidence-genome records
- `10.5281/zenodo.21613709`
- `10.5281/zenodo.21627064`
- `10.5281/zenodo.21633158`
- `10.5281/zenodo.21776344`
- `10.5281/zenodo.21778108`
- `10.5281/zenodo.21941060`

### Tier 3 — Audit and validation records
- `10.5281/zenodo.21644554`
- `10.5281/zenodo.21845283`
- `10.5281/zenodo.21987681`
- `10.5281/zenodo.18446386`
- `10.5281/zenodo.21940564`
- `10.5281/zenodo.22015815`

### Tier 4 — Supporting research records
- `10.5281/zenodo.21908366`
- `10.5281/zenodo.21911350`
- `10.5281/zenodo.21940787`
- `10.5281/zenodo.21952250`
- `10.5281/zenodo.22047162`
- `10.5281/zenodo.22070648`

### Tier 5 — Related records
- `10.5281/zenodo.22073794`
- `10.5281/zenodo.18201597`
- `10.5281/zenodo.21813708`
- `10.5281/zenodo.21879425`
- `10.5281/zenodo.22018275`
- `10.5281/zenodo.22074002`

## License

This release is identified as CC BY 4.0. See [LICENSE](LICENSE) for the official license URL and the author's separate attribution/honorable-mention notice. The notice does not modify the CC BY 4.0 license grant.
