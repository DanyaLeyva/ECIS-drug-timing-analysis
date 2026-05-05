# ECIS Drug Timing Analysis – Project Status

## Project Goal

This project uses Electric Cell-substrate Impedance Sensing (ECIS) data to study how drug timing affects cellular behavior over time. The goal is to build a reproducible analysis workflow that can process ECIS data, visualize impedance trends, compare experimental conditions, and support later physics-based and biological interpretation of ECIS responses.

## Current Workflow Stage

The project is currently in the **early physics-based ECIS analysis stage**.

The workflow has now moved beyond preprocessing, condition comparison, and multifrequency comparison. The current focus is on testing whether multifrequency ECIS signals can be used to recover interpretable biophysical parameters such as **Rb**, **alpha**, and **Cm** through inverse fitting.

## What Has Been Completed

- Set up the project environment using Python, JupyterLab, and Anaconda
- Organized the repository into data, notebooks, scripts, and results folders
- Loaded pilot ECIS datasets into Python
- Fixed file path and notebook execution issues
- Cleaned and reorganized the notebook with markdown structure and clearer sections
- Filtered pilot ECIS data to a single frequency for initial analysis
- Normalized impedance values to baseline
- Generated replicate plots for pilot wells
- Confirmed that the preprocessing pipeline is functioning correctly
- Calculated mean normalized impedance across replicates
- Measured replicate variability using standard deviation
- Extracted quantitative features including:
  - maximum normalized impedance
  - time of maximum impedance
  - final normalized impedance
  - approximate growth slope
- Loaded metadata for all pilot wells
- Created readable condition labels for all pilot conditions
- Expanded the analysis from a single control-style well to all 18 pilot wells
- Compared all 6 pilot conditions at 500 Hz
- Repeated condition-level comparison at 4000 Hz
- Repeated condition-level comparison at 16000 Hz
- Combined summaries across 500 Hz, 4000 Hz, and 16000 Hz
- Confirmed that the overall treatment pattern remains consistent across frequencies
- Began the physics-based ECIS analysis stage
- Implemented the ECIS forward model and inverse-fitting functions in the notebook
- Simulated one physics-based pilot ECIS well with multifrequency complex impedance output
- Generated simulated ECIS data containing:
  - Zreal
  - Zimag
  - Zmag
  - Zphase
  - true latent Rb
  - true latent alpha
  - true latent Cm
- Attempted inverse fitting at one time point using multifrequency impedance values
- Extended inverse fitting across all time points
- Compared true versus estimated Rb, alpha, and Cm trajectories
- Computed estimation error using mean absolute error (MAE)

## Last Completed Work – May 5, 2026

The most recent work session focused on starting the physics-based ECIS analysis layer.

During this session, a physics-based ECIS simulator was used to generate one pilot well with multifrequency complex impedance data and known latent parameter trajectories for **Rb**, **alpha**, and **Cm**. An inverse-fitting routine was then applied to estimate those parameters back from the simulated ECIS signal.

This established the first full forward-model / inverse-fit workflow in the notebook.

## Current Physics-Based Result

The physics-based simulation step ran successfully, and the inverse-fitting routine executed without crashing. However, the parameter recovery was **not yet reliable**.

The estimated values frequently hit the fitting bounds instead of closely matching the true simulated parameter values. As a result:

- estimated **Rb** did not track the true Rb trajectory well
- estimated **alpha** did not track the true alpha trajectory well
- estimated **Cm** did not track the true Cm trajectory well

The resulting error values were still high, indicating that the inverse-fitting setup needs debugging before it can be used for meaningful interpretation.

This means the project has successfully entered the physics-based stage, but the inverse-fitting portion is still in a **debugging / validation phase**.

## Current Status

The preprocessing, feature extraction, condition comparison, and multifrequency comparison stages are complete.

The project has now successfully started the physics-based ECIS stage, but the inverse-fitting results are not yet accurate enough for interpretation. At this point, the notebook supports:

- multifrequency ECIS simulation
- latent parameter generation for Rb, alpha, and Cm
- inverse fitting at single time points
- inverse fitting across full time courses
- comparison of true and estimated parameter trajectories
- error quantification for parameter recovery

The main issue now is not running the workflow, but improving the quality of the recovered parameter estimates.

## What I Am Currently Doing

I have completed the first test of the physics-based ECIS workflow.

The current task is now to debug the inverse-fitting setup so that the estimated values for **Rb**, **alpha**, and **Cm** can recover the simulated latent trajectories more accurately.

## What Is Left To Do

- Debug the inverse-fitting routine
- Re-test the fitting workflow with lower-noise or no-noise simulated data
- Tighten or refine parameter bounds and starting values
- Confirm that the inverse-fitting method can recover parameters correctly on a simple clean example
- Improve parameter recovery before scaling the method further
- Once fitting is stable, apply the physics-based workflow more broadly across conditions
- Continue documenting analysis results in the notebook and repository
- Prepare updated figures and summaries for discussion or presentation
- Connect recovered ECIS parameters to broader biological interpretation and drug-timing analysis

## Workflow Position

- Environment setup ✅
- Data loading ✅
- Frequency filtering ✅
- Baseline normalization ✅
- Pilot plotting ✅
- Initial analysis notes ✅
- Replicate summary statistics ✅
- Feature extraction ✅
- Metadata integration ✅
- Condition comparison at 500 Hz ✅
- Multifrequency comparison ✅
- Physics-based ECIS simulation ✅
- Inverse fitting attempted ✅
- Reliable parameter recovery ⏳
- Biological interpretation ⏳
- Reporting and presentation ⏳

## Summary

The pilot ECIS workflow is now functioning through the **early physics-based ECIS stage**. The project has progressed from preprocessing and multifrequency comparison into simulation and inverse fitting of interpretable ECIS parameters.

A full physics-based forward-model / inverse-fit workflow has now been tested, but the current inverse-fitting setup does not yet recover **Rb**, **alpha**, and **Cm** reliably. The next step is to debug the fitting process using simpler, lower-noise tests before moving on to broader physics-based interpretation.
