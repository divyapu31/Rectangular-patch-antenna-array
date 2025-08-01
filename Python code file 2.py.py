import math
# Constants
c = 3e8  # Speed of light in m/s
# Design Parameters (updated)
f = 5.8e9  # Design frequency in Hz
er = 2.2  # Dielectric constant
h = 0.8e-3  # Substrate height in meters
z0 = 50  # System impedance in ohms

# Calculate guided wavelength (approximate with effective dielectric constant)
def calc_wavelength(frequency, er_eff):
    return c / (frequency * math.sqrt(er_eff))

# Microstrip line width calculator using Wheeler’s approximation
def calc_microstrip_width(Z0, er, h):
    A = Z0 / 60 * math.sqrt((er + 1) / 2) + (er - 1) / (er + 1) * (0.23 + 0.11 / er)
    if Z0 <= 60:
        W_h = 8 * math.exp(A) / (math.exp(2 * A) - 2)
    else:
        B = 377 * math.pi / (2 * Z0 * math.sqrt(er))
        W_h = (2 / math.pi) * (B - 1 - math.log(2 * B - 1) + 
              ((er - 1) / (2 * er)) * (math.log(B - 1) + 0.39 - 0.61 / er))
    return W_h * h

# Quarter-wave transformer impedance (for 1:2 split)
Z_transformer = math.sqrt(z0 * z0 * 2)  # ~70.7 Ω

# Approximate effective dielectric constant (for microstrip)
er_eff = (er + 1) / 2  # simple estimate

# Quarter-wave length
lambda_g = calc_wavelength(f, er_eff)
quarter_wave_length = lambda_g / 4

# Microstrip widths
w_50 = calc_microstrip_width(50, er, h)
w_70 = calc_microstrip_width(70.7, er, h)

# Output results
print("=== 1:4 Wilkinson Divider Corporate Feed ===")
print(f"Operating Frequency: {f/1e9:.2f} GHz")
print(f"Dielectric Constant: {er}")
print(f"Substrate Height: {h*1e3:.2f} mm")
print(f"Effective Wavelength (approx): {lambda_g*1e3:.2f} mm")
print(f"Quarter-Wave Length: {quarter_wave_length*1e3:.2f} mm")

print("\n--- Microstrip Line Widths ---")
print(f"50 Ω Line Width: {w_50*1e3:.2f} mm")
print(f"70.7 Ω Line Width: {w_70*1e3:.2f} mm")

print("\n--- Resistor Values for Isolation ---")
print(f"Each Wilkinson branch uses: {2*z0} Ω resistor (between output arms)")