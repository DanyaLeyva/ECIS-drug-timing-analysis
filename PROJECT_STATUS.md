# ECIS Drug Timing Analysis – Project Status

## Project Goal
This project uses Electric Cell-substrate Impedance Sensing (ECIS) data to study how drug timing affects cellular behavior over time.

## Current Workflow Stage
The project is currently in the pilot data preprocessing and validation stage.

## What Has Been Completed
- Set up the project environment using Python, JupyterLab, and Anaconda
- Organized the repository into data, notebooks, scripts, and results folders
- Loaded pilot ECIS datasets into Python
- Filtered data to a single frequency (500 Hz)
- Normalized impedance values to baseline
- Generated replicate plots for pilot analysis
- Wrote interpretation notes on signal consistency and preprocessing success

## What I Am Currently Doing, March 10th, 2026
I am reviewing the pilot analysis and preparing to move into quantitative analysis of the impedance curves. This includes checking that the notebook runs correctly after reopening, documenting progress, and planning the next analysis stage.

## What Is Left To Do
- Re-run the notebook from the top to reload data and variables
- Calculate mean impedance across replicates
- Measure replicate variability using standard deviation
- Compute quantitative metrics such as slope, maximum impedance, and plateau behavior
- Compare impedance behavior across experimental conditions
- Interpret results in the context of drug timing and cell behavior

## Workflow Position
1. Environment setup ✅
2. Data loading ✅
3. Frequency filtering ✅
4. Baseline normalization ✅
5. Pilot plotting ✅
6. Initial analysis notes ✅
7. Quantitative replicate analysis ⏳
8. Metric extraction ⏳
9. Condition comparison ⏳
10. Biological interpretation ⏳

## Summary
The preprocessing pipeline is functioning correctly, and the pilot ECIS datasets appear suitable for further analysis. The next phase of the project is quantitative analysis of replicate trends and comparison across conditions.