
import numpy as np
import pandas as pd

def simulate_viability_physics(df,time_hr=72,w_Rb=0.5,w_alpha=0.3,w_Cm=0.2):
    late=df[df.time_min>=time_hr*60]
    agg=late.groupby(["run_id","well_id"]).agg(
        Rb=("Rb","mean"),alpha=("alpha","mean"),Cm=("Cm","mean")
    ).reset_index()
    stress=(w_Rb*(agg.Rb.max()-agg.Rb)
           +w_alpha*(agg.alpha-agg.alpha.min())
           +w_Cm*(agg.Cm.max()-agg.Cm))
    agg["viability"]=np.clip(np.exp(-stress)+np.random.normal(0,0.05,len(stress)),0,1)
    return agg[["run_id","well_id","viability"]]
