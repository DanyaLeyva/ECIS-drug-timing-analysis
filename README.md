# ECIS Drug Timing Analysis

This project analyzes Electric Cell-Substrate Impedance Sensing (ECIS) time-series data to study how cellular behavior changes under different drug timing conditions. The long-term goal is to build a reproducible workflow for preprocessing ECIS data, extracting quantitative features, comparing treatment conditions, and supporting later drug schedule optimization.

ECIS records impedance changes over time as cells attach, grow, divide, round up, detach, or die. This makes it useful for studying how cells respond to different drug schedules without needing labels or dyes.

## Objectives

- Load and preprocess ECIS datasets
- Normalize impedance signals to baseline
- Compare technical replicates
- Extract quantitative ECIS features
- Compare experimental conditions and drug timing strategies
- Visualize ECIS time-series behavior
- Evaluate baseline signal stability
- Begin physics-based ECIS parameter modeling
- Support later schedule-optimization analysis

## Current Progress

The project currently includes:

- Pilot ECIS preprocessing in Python/JupyterLab
- Frequency filtering and baseline normalization
- Replicate comparison and variability checks
- Quantitative feature extraction:
  - maximum normalized impedance
  - time of maximum impedance
  - final normalized impedance
  - approximate growth slope
- Condition-level comparison across pilot wells
- Summary plots and overlaid mean ECIS curves by condition
- Multifrequency comparison across 500 Hz, 4000 Hz, and 16000 Hz
- Cross-frequency summaries showing that the main treatment pattern remains consistent across the pilot ECIS frequencies
- Baseline quality-control analysis using the first 120 minutes of each well-frequency signal
- Physics-based ECIS simulation using latent parameters Rb, alpha, and Cm
- Inverse fitting to recover Rb, alpha, and Cm from simulated multifrequency impedance data
- Clean simulation validation
- Noisy simulation robustness testing
- Clean vs noisy estimation error comparison using MAE and RMSE

## Preliminary Findings

The descriptive ECIS analysis pipeline successfully processed the pilot dataset. The normalized impedance signals generally increased over time, and technical replicates showed similar overall trends.

Across 500 Hz, 4000 Hz, and 16000 Hz, the control and single-drug conditions generally showed higher normalized impedance responses, while the lagged combination treatment conditions showed lower responses. This suggests that drug timing and treatment order may affect the ECIS response in the pilot dataset.

The baseline quality-control step showed that all well-frequency combinations passed the baseline stability check. This supports the use of baseline normalization and suggests that later impedance changes are more likely related to treatment-response behavior rather than unstable baseline measurements.

The physics-based modeling workflow successfully recovered known Rb, alpha, and Cm parameter trajectories under clean simulated conditions. However, when noise was added to the simulated impedance data, the parameter estimates became unstable and the error increased. This suggests that the inverse-fitting method is promising but still needs robustness improvements before being applied to real experimental ECIS data.

## Current Limitations

This project is currently focused on the pilot/feasibility and early model-validation stage. The larger workflow still requires additional experimental data and further model development.

The following parts are not fully completed yet:

- Full parameter-finding screen across larger dose, lag, and treatment-order grids
- Focused schedule-optimization experiments with dense sampling
- Full integration with flow cytometry and viability measurements
- Full PINN-SSM or temporal classifier model development
- Prospective confirmation of optimized schedules in held-out biological replicates

## Next Steps

Future work should focus on:

- Testing smaller noise levels in the physics-based model
- Adding smoothing or regularization to improve noisy parameter recovery
- Using the previous time point's fitted parameters as the starting point for the next fit
- Applying the improved physics-based fitting method to real ECIS pilot data
- Adding statistical comparisons across treatment conditions
- Integrating flow cytometry and viability measurements when those datasets are available
- Expanding toward schedule optimization and prospective validation

## Tools

- Python
- Pandas
- NumPy
- Matplotlib
- JupyterLab
- Anaconda

## Repository Structure

- `data/` – pilot ECIS datasets and metadata
- `notebooks/` – Jupyter notebooks for preprocessing and analysis
- `scripts/` – reusable Python scripts for simulation and analysis
- `results/` – plots, summaries, and exported outputs

## Current Workflow Stage

The project has completed the initial pilot ECIS analysis workflow and an early physics-based modeling validation.

The descriptive analysis pipeline loads pilot ECIS files, filters signals by frequency, normalizes impedance to baseline, compares technical replicates, extracts quantitative features, and compares treatment conditions across 500 Hz, 4000 Hz, and 16000 Hz.

The physics-based modeling workflow simulates multifrequency ECIS data using Rb, alpha, and Cm. The inverse-fitting routine successfully recovered these parameters under clean simulated conditions, but noisy simulation testing showed that the method is sensitive to measurement noise.

The next step is to improve the stability of the physics-based fitting routine under noisy conditions and then expand toward the later stages of the full drug schedule-optimization workflow.

## One-Sentence Summary

This project uses ECIS time-series data to compare drug timing conditions and begins validating a physics-based modeling workflow for interpreting treatment-response behavior.

## Author

Danya Leyva  
California State University, Dominguez Hills  
Computer Science
