import numpy as np

from scipy.optimize import fsolve

# Known resistances (ohms)
R3 = 330.0
R4 = 165.0

# Measured voltages (VOLTS)
# =========================
V_unload = 10  # voltage across R3 alone
V_24 = 12  # voltage with R2 || R4
V_load = 30  # voltage with R2 || R3 || R4

# Voltage ratios
A = V_24 / V_unload
B = V_load / V_unload


# Define equations
def equations(vars):
    R2, R1 = vars

    # Parallel resistances
    R24 = (R2 * R4) / (R2 + R4)
    Req = 1 / (1 / R2 + 1 / R3 + 1 / R4)

    eq1 = A - (R24 * (R3 + R1)) / (R3 * (R24 + R1))
    eq2 = B - (Req * (R3 + R1)) / (R3 * (Req + R1))

    return [eq1, eq2]


# Initial guess
initial_guess = [500, 10]

# Solve
R2_sol, R1_sol = fsolve(equations, initial_guess)

# Battery EMF
E_sol = V_unload * (1 + R1_sol / R3)


# Results
print(f"R2 = {R2_sol:.3f} ohms")
print(f"R1  = {R1_sol:.3f} ohms")
print(f"E  = {E_sol:.3f} V")
