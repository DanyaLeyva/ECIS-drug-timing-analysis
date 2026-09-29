# Project Status: ECIS Drug Timing Analysis

## Current Stage

The project is currently at the completed pilot/feasibility analysis stage with an initial physics-based modeling validation.

The completed notebook includes descriptive ECIS analysis, multifrequency comparison, baseline quality control, clean simulated physics-based fitting, and noisy simulation robustness testing.

## Completed Work

### 1. Data Loading and Setup

The pilot ECIS data and metadata were loaded successfully in Python using JupyterLab. File paths were checked, and the workflow was organized to analyze individual wells and treatment conditions.

### 2. ECIS Preprocessing

The workflow filters impedance data by frequency and normalizes each well to its baseline value. This makes wells comparable across different starting impedance values.

### 3. Technical Replicate Comparison

Technical replicates were compared visually and quantitatively. The replicate curves showed similar overall trends, suggesting that the pilot dataset was stable enough for initial feature extraction and condition comparison.

### 4. Feature Extraction

The following response features were extracted for each well:

- Maximum normalized impedance
- Time of maximum response
- Final normalized impedance
- Approximate growth slope

These features were used to summarize treatment-response patterns.

### 5. Condition-Level Comparison

Treatment conditions were compared at 500 Hz. The normalized impedance curves generally increased over time. The control and single-drug conditions showed higher normalized impedance responses, while lagged combination conditions showed lower responses.

This suggests that drug timing and treatment order may affect the ECIS response, although the results should be interpreted as preliminary because this is a pilot dataset.

### 6. Multifrequency Comparison

The condition-level comparison was extended across:

- 500 Hz
- 4000 Hz
- 16000 Hz

The same general trend appeared across frequencies. Control and single-drug conditions remained relatively high, while lagged combination treatments were generally lower. This suggests that the observed condition-level differences were not limited to only one frequency.

### 7. Baseline Quality Control

Baseline stability was evaluated using the first 120 minutes of each well-frequency signal. For each well and frequency, the baseline mean, standard deviation, and coefficient of variation were calculated.

All well-frequency combinations passed the baseline stability check:

| Frequency | QC Result | Count |
|---:|---|---:|
| 500 Hz | Pass | 18 |
| 4000 Hz | Pass | 18 |
| 16000 Hz | Pass | 18 |

This supports the use of baseline normalization and suggests that later impedance changes are more likely related to treatment-response behavior rather than unstable baseline measurements.

### 8. Physics-Based ECIS Modeling

A physics-based ECIS simulation was created using known latent parameter trajectories:

- Rb
- alpha
- Cm

An inverse-fitting routine was tested to determine whether these known parameters could be recovered from simulated multifrequency impedance data.

### 9. Clean Simulation Results

Under clean simulated conditions with no added noise, the inverse-fitting routine successfully recovered the known Rb, alpha, and Cm trajectories. The true and estimated parameter curves overlapped closely, and the estimation errors were very small.

This confirms that the fitting routine works under ideal simulated conditions.

### 10. Noisy Simulation Results

Noise was added to the simulated impedance data to test robustness. Although the optimizer still reported successful convergence, the estimated parameter trajectories became unstable, especially for Rb and alpha.

The noisy simulation produced much larger errors than the clean simulation. This shows that optimizer success does not necessarily mean the estimated parameters are accurate.

## Main Findings

1. The descriptive ECIS analysis pipeline is functioning.
2. Baseline normalization is supported by stable baseline QC results.
3. Treatment conditions show preliminary differences in normalized impedance response.
4. Control and single-drug conditions generally show higher normalized impedance responses.
5. Lagged combination conditions generally show lower normalized impedance responses.
6. The physics-based inverse-fitting routine works on clean simulated data.
7. The physics-based fitting method becomes unstable when noise is added.
8. More robustness improvements are needed before applying the physics-based model to real experimental ECIS data.

## Work Not Yet Completed

The larger project workflow includes additional stages that are not completed yet:

- Full parameter-finding screen across larger dose, lag, and treatment-order grids
- Focused schedule-optimization experiments with dense sampling
- Full integration with flow cytometry and viability measurements
- Full PINN-SSM or temporal classifier model development
- Prospective confirmation of optimized schedules in held-out biological replicates

These require additional experimental data and further model development.

## Next Steps

The next stage should focus on improving the physics-based fitting workflow and expanding the experimental analysis.

Potential next steps include:

- Testing smaller noise levels
- Adding smoothing or regularization
- Using previous time-point estimates as starting values for the next fit
- Applying the fitting method to real ECIS data after robustness improves
- Adding statistical testing across conditions
- Integrating flow cytometry and viability data when available
- Expanding toward schedule optimization experiments

## Current Conclusion

The pilot ECIS analysis workflow is complete for this stage. The project successfully loads, normalizes, visualizes, and summarizes ECIS time-series data across treatment conditions and frequencies. The baseline QC results support the reliability of the preprocessing workflow.

The physics-based modeling workflow is promising because it can recover known ECIS parameters under clean simulated conditions. However, the noisy simulation results show that the current inverse-fitting method is sensitive to noise and requires additional development before being used for real experimental interpretation.
