_**Repository information**_:

This repository contains  the steps to develop a rectangular microstrip patch antenna array conatining 4 rectangular slots for miniaturization and the 4 antenna elements are fed with 4 equal way power wilkinson power divider. Firstly the dimensions of the patch and power divider are calculated with help of python code, later the antenna is designed and optimized using CST microwave studio simulation solver. The original CST files of the proposed antenna as single element and overall array antenna is defined here.

**_Manuscript Information_** :

**Title of the manuscript**:Design of Rectangular Slotted-Patch Antenna Array-Sensor for Breast-Tumor Detection

**Paper id:** 9775

**Authors and their affiliations:** 
1. D. Chaturvedi, Dept. of Electronics and Communication Engineering, Indian Institute of Information Technology, Pune, India
2. MVL Bhavani( corresponding author) Dept. of Electronics and Communication Engineering, SRM University-AP, India 
3. Arvind Kumar, Dept. of Electronics and Communication Engineering, Visvesvaraya National Institute of Technology, Nagpur, India.
   
**Journal:** Latin America Transactions


_**** Steps to design the proposed Antenna Array** **_
Python code file 1 (  determine the dimensions of slotted RMPA)
Python code file 2 (determine the dimesnions of 4 way power divider)_


****Design work flow****

  o	Dielectric constant (εr) = 2.2
  
  o	Substrate height (h) = 0.8 mm

 This is based on standard design equations for a rectangular microstrip patch antenna operating in the TM₁₀ mode as shown below
 1. Width (W) of the patch
W = c / (2 * f_r) * sqrt(2 / (ε_r + 1))
2. The Effective Dielectric Constant (ε_eff) is 
eps_eff = (ε_r + 1)/2 + (ε_r - 1)/2 * [1 + 12 * (h / W)]^(-0.5)
3. The Extension in Length (ΔL) due to fringing fields is:
ΔL = 0.412 * h * ((eps_eff + 0.3) * (W/h + 0.264)) / ((eps_eff - 0.258) * (W/h + 0.8))
4. Effective Length (L_eff)  is:
L_eff = c / (2 * f_r * sqrt(ε_eff))
5. The actual Length (L) of the patch is:
L = L_eff - 2 * ΔL
6. The resonant frequency of the patch antenna in TM_10 mode is:
f_r = c / (2 * L * sqrt(ε_eff))

After calculating the dimensions of the patch the next step is to etch 4 rectangular slots in the non-radiating edge of the patch
The extension in the length of the rectangular patch is:
Leff_new = Leff + delta_L_slot_effect
The frequency will shift downward due to extension in patch length
fr_new = c / (2 * Leff_new * np.sqrt(eps_eff))
The new operating frequency will be 5.8 GHz

The next step is to design a **1:4 wilkinson power divider** which distribute power equally to 4 antenna-elements
The wilkinson power divider will be based on the quarter wave transformer impedance calculation
 Zt = sqrt(Zi*ZL) , where Zi is the input impedance and ZL is the load impedance, and Zt is the characteristic impedance of a quarter-wave transformer 
 
**_Antenna optimization/ Analysis/ Results Visulization_**
1. Single patch with slots.cst
2. Proposed Array antenna.cst


_**Results **_

List of Figures.docx
