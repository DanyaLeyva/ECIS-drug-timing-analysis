
import numpy as np
import pandas as pd

def ecis_forward_impedance(omega, Rb, alpha, Cm, Rs=0.0):
    Y = (1.0 / Rb) + (np.sqrt(1j * omega) / alpha) + (1j * omega * Cm)
    return 1.0 / Y + Rs

def _step_exp_rise(t, t0, tau):
    x = np.maximum(0.0, t - t0)
    return 1.0 - np.exp(-x / tau)

def simulate_latent_theta(time_hr, dose_A=0, dose_B=0, lag_hr=0, order="A_then_B",
                           Rb0=2.0, alpha0=8.0, Cm0=2e-6,
                           k_Rb_A=0.20, k_Rb_B=0.15,
                           k_alpha_A=0.20, k_alpha_B=0.10,
                           k_Cm_A=0.10, k_Cm_B=0.20,
                           tau_Rb=6.0, tau_alpha=4.0, tau_Cm=10.0,
                           seq_coupling=0.15, random_state=None):
    rng = np.random.default_rng(random_state)
    tA = 0.0
    tB = lag_hr if order == "A_then_B" else 0.0
    if order == "B_then_A":
        tA = lag_hr

    A_Rb = _step_exp_rise(time_hr, tA, tau_Rb)
    B_Rb = _step_exp_rise(time_hr, tB, tau_Rb)
    A_alpha = _step_exp_rise(time_hr, tA, tau_alpha)
    B_alpha = _step_exp_rise(time_hr, tB, tau_alpha)
    A_Cm = _step_exp_rise(time_hr, tA, tau_Cm)
    B_Cm = _step_exp_rise(time_hr, tB, tau_Cm)

    both = A_Rb * B_Rb
    seqA = 1.0 + seq_coupling * both if order == "B_then_A" else 1.0
    seqB = 1.0 + seq_coupling * both if order == "A_then_B" else 1.0

    Rb = Rb0 * (1 - k_Rb_A*dose_A*A_Rb*seqA - k_Rb_B*dose_B*B_Rb*seqB)
    alpha = alpha0 * (1 + k_alpha_A*dose_A*A_alpha*seqA + k_alpha_B*dose_B*B_alpha*seqB)
    Cm = Cm0 * (1 - k_Cm_A*dose_A*A_Cm*seqA - k_Cm_B*dose_B*B_Cm*seqB)

    Rb = np.clip(Rb + rng.normal(0,0.02,len(Rb)),0.05,None)
    alpha = np.clip(alpha + rng.normal(0,0.02,len(alpha)),0.05,None)
    Cm = np.clip(Cm + rng.normal(0,5e-8,len(Cm)),1e-9,None)

    return pd.DataFrame({"time_hr":time_hr,"Rb":Rb,"alpha":alpha,"Cm":Cm})

def simulate_ecis_physics_run(run_id, well_id, frequencies=(500,4000,16000),
                              duration_hr=72, dt_min=5,
                              dose_A=0, dose_B=0, lag_hr=0, order="A_then_B",
                              Rs=50.0, noise_sd=2.0, random_state=None):
    rng = np.random.default_rng(random_state)
    time_min = np.arange(0,duration_hr*60+dt_min,dt_min)
    time_hr = time_min/60
    theta = simulate_latent_theta(time_hr,dose_A,dose_B,lag_hr,order,random_state=random_state)

    rows=[]
    for f in frequencies:
        omega = 2*np.pi*f
        Z = ecis_forward_impedance(omega,theta.Rb.values,theta.alpha.values,theta.Cm.values,Rs)
        Z += rng.normal(0,noise_sd,len(Z)) + 1j*rng.normal(0,noise_sd,len(Z))
        for t,z,rb,a,cm in zip(time_min,Z,theta.Rb,theta.alpha,theta.Cm):
            rows.append({
                "run_id":run_id,"well_id":well_id,"time_min":float(t),
                "frequency_hz":float(f),"Zreal":float(np.real(z)),
                "Zimag":float(np.imag(z)),"Zmag":float(np.abs(z)),
                "Zphase":float(np.angle(z)),"Rb":float(rb),
                "alpha":float(a),"Cm":float(cm)
            })
    return pd.DataFrame(rows)
