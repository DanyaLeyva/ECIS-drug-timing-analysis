
import numpy as np
from scipy.optimize import least_squares

def ecis_forward(omega,Rb,alpha,Cm,Rs=50.0):
    Y=(1/Rb)+(np.sqrt(1j*omega)/alpha)+(1j*omega*Cm)
    return 1/Y+Rs

def fit_theta_single_time(freqs,Zobs):
    def res(x):
        Rb,alpha,Cm=x
        Z=np.array([ecis_forward(2*np.pi*f,Rb,alpha,Cm) for f in freqs])
        return np.concatenate([(Z.real-Zobs.real),(Z.imag-Zobs.imag)])
    out=least_squares(res,x0=[2,8,2e-6],
                      bounds=([0.05,0.05,1e-9],[50,50,1e-3]))
    return {"Rb":out.x[0],"alpha":out.x[1],"Cm":out.x[2]}
