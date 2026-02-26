
from pathlib import Path
import pandas as pd
from ecis_physics_sim import simulate_ecis_physics_run

def simulate_and_export(outdir="ecis_physics_csv"):
    out = Path(outdir)
    out.mkdir(exist_ok=True)

    conditions=[
        {"dose_A":0,"dose_B":0,"lag_hr":0,"order":"A_then_B"},
        {"dose_A":10,"dose_B":0,"lag_hr":0,"order":"A_then_B"},
        {"dose_A":0,"dose_B":10,"lag_hr":0,"order":"A_then_B"},
        {"dose_A":10,"dose_B":10,"lag_hr":0,"order":"A_then_B"},
        {"dose_A":10,"dose_B":10,"lag_hr":6,"order":"A_then_B"},
        {"dose_A":10,"dose_B":10,"lag_hr":6,"order":"B_then_A"},
    ]

    meta=[]
    for i,c in enumerate(conditions,1):
        for r in range(1,4):
            well=f"C{i}_R{r}"
            df=simulate_ecis_physics_run(
                "pilot_phys_001",well,
                dose_A=c["dose_A"],dose_B=c["dose_B"],
                lag_hr=c["lag_hr"],order=c["order"],
                random_state=1000+i*10+r
            )
            fname=f"{well}.csv"
            df.to_csv(out/fname,index=False)
            meta.append({**c,"run_id":"pilot_phys_001","well_id":well,"file_path":fname})

    pd.DataFrame(meta).to_csv(out/"ecis_metadata.csv",index=False)

if __name__=="__main__":
    simulate_and_export()
