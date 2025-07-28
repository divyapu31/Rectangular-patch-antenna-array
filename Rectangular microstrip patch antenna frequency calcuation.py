import numpy as np
# Constants
c = 3e8  # Speed of light (m/s)

# Substrate and dielectric
er = 2.2
h = 0.8e-3  # Substrate thickness (m)

# Original design frequency (before slots)
fr_initial = 6.9e9  # Hz

# Step 1: Calculate patch width (W)
W = c / (2 * fr_initial) * np.sqrt(2 / (er + 1))

# Step 2: Calculate effective dielectric constant (εeff)
eps_eff = (er + 1)/2 + (er - 1)/2 * (1/np.sqrt(1 + 12 * h / W))

# Step 3: Calculate effective length (Leff) and ΔL
lambda_0 = c / fr_initial
delta_L = 0.412 * h * ((eps_eff + 0.3) * ((W/h) + 0.264)) / ((eps_eff - 0.258) * ((W/h) + 0.8))
Leff = c / (2 * fr_initial * np.sqrt(eps_eff))

# Actual patch length before slots
L_actual = Leff - 2 * delta_L

# Step 4: Calculate guided wavelength λg
lambda_g = c / (fr_initial * np.sqrt(eps_eff))

# Step 5: Define slot parameters
slot_length = 4e-3            # 4 mm typical 
slot_width = 0.5e-3            # 0.5 mm typical

# Approximate extension in length due to slots (empirical)
# Slots increase current path → increases effective length → lowers frequency
delta_L_slot_effect = 0.1*lambda_g  # ~2% λg increase in effective length (tunable)

# New effective length
Leff_new = Leff + delta_L_slot_effect

# New resonant frequency after slotting
fr_new = c / (2 * Leff_new * np.sqrt(eps_eff))

# Convert to mm
W_mm = W * 1e3
L_mm = L_actual * 1e3
slot_len_mm = slot_length * 1e3
Leff_new_mm = Leff_new * 1e3

# Output
print("=== Patch Antenna With Slots ===")
print(f"Original Frequency        : {fr_initial/1e9:.2f} GHz")
print(f"Original Patch Length (L) : {L_mm:.2f} mm")
print(f"Patch Width (W)           : {W_mm:.2f} mm")
print(f"Effective εr (εeff)       : {eps_eff:.4f}")
print(f"Slot Length (0.1 λg)      : {slot_len_mm:.2f} mm")
print(f"Estimated Length Increase : {delta_L_slot_effect*1e3:.2f} mm")
print(f"New Effective Length      : {Leff_new_mm:.2f} mm")
print(f"Shifted Frequency         : {fr_new/1e9:.2f} GHz")