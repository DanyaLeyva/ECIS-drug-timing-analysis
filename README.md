# ECIS Drug Timing Analysis

This project analyzes Electric Cell-Substrate Impedance Sensing (ECIS) time-series data to study how cellular behavior changes under different drug timing conditions. The long-term goal is to build a reproducible workflow for preprocessing ECIS data, extracting quantitative features, comparing treatment conditions, and supporting later drug schedule optimization.

## Objectives

- Load and preprocess ECIS datasets
- Normalize impedance signals to baseline
- Compare technical replicates
- Extract quantitative ECIS features
- Compare experimental conditions and drug timing strategies
- Visualize ECIS time-series behavior
- Support later physics-based and schedule-optimization analysis

## Current Progress

The project currently includes:

- Pilot ECIS preprocessing in Python/JupyterLab
- Frequency filtering for initial 500 Hz analysis
- Baseline normalization
- Replicate comparison and variability checks
- Quantitative feature extraction:
  - maximum normalized impedance
  - time of maximum impedance
  - final normalized impedance
  - approximate growth slope
- Condition-level comparison across pilot wells
- Summary plots and overlaid mean ECIS curves by condition

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

The project is currently in the **pilot condition-comparison stage**.  
Next steps include extending the same analysis to additional ECIS frequencies and later connecting the results to physics-based ECIS modeling.

## Author

Danya Leyva  
California State University, Dominguez Hills  
Computer Science
