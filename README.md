# 📐 SPDC in PPKTP

Simulation of SPDC in PPKTP crystal with temperature-dependent phase matching.

---

## 📐 Equations Used

### **Equation 1 – Refractive index squared (Y-axis)**

\[
n_y^2 = A_y + B_y \cdot \frac{\lambda^2}{\lambda^2 - C_y} - D_y \cdot \lambda^2
\]

**Y-axis Coefficients:**

| Coefficient | Value   |
|-------------|---------|
| \(A_y\)     | 2.19229 |
| \(B_y\)     | 0.83547 |
| \(C_y\)     | 0.04970 |
| \(D_y\)     | 0.01621 |

---

### **Equation 2 – Refractive index squared (Z-axis)**

\[
n_z^2 = A_z + B_z \cdot \frac{\lambda^2}{\lambda^2 - C_z} - D_z \cdot \lambda^2
\]

**Z-axis Coefficients:**

| Coefficient | Value   |
|-------------|---------|
| \(A_z\)     | 2.25411 |
| \(B_z\)     | 1.06543 |
| \(C_z\)     | 0.05486 |
| \(D_z\)     | 0.02140 |

---

### **Equation 3 – Temperature derivative of \(n_y\)**

\[
\frac{dn_y}{dT} = \left( \frac{1.997}{\lambda^3} - \frac{4.067}{\lambda^2} + \frac{5.154}{\lambda} - 5.425 \right) \times 10^{-6}
\]

---

### **Equation 4 – Temperature derivative of \(n_z\)**

\[
\frac{dn_z}{dT} = \left( \frac{9.221}{\lambda^3} - \frac{29.220}{\lambda^2} + \frac{36.667}{\lambda} - 1.897 \right) \times 10^{-6}
\]

---

### **Equation 5 – Temperature-adjusted refractive index (Y-axis)**

\[
n_{new,y} = n_y + \left( \frac{dn_y}{dT} \right) \cdot (T - 25.0)
\]

---

### **Equation 6 – Temperature-adjusted refractive index (Z-axis)**

\[
n_{new,z} = n_z + \left( \frac{dn_z}{dT} \right) \cdot (T - 25.0)
\]

---

### **Equation 7 – Temperature-dependent grating period**

\[
\Lambda(T) = \Lambda_0 \cdot \left[ 1 + A(T - 25^\circ C) + B(T - 25^\circ C)^2 \right]
\]

**Constants:**

- \(A = 6.7 \times 10^{-6}\)
- \(B = 11 \times 10^{-9}\)

---

### **Equation 8 – Phase mismatch \(\Delta k\)**

\[
\Delta k = \frac{2\pi n_y(\lambda_p)}{\lambda_p} - \frac{2\pi n_z(\lambda_s)}{\lambda_s} - \frac{2\pi n_y(\lambda_i)}{\lambda_i} - \frac{2\pi}{\Lambda(T)}
\]

**Clarifications:**
- \(n_y(\lambda_p)\): from Equation 1 evaluated at \(\lambda_p\)  
- \(n_z(\lambda_s)\): from Equation 2 evaluated at \(\lambda_s\)  
- \(n_y(\lambda_i)\): from Equation 1 evaluated at \(\lambda_i\)  
- Refractive indices adjusted using Equations 5 and 6  
- \(\Lambda(T)\) from Equation 7

---

### **Equation 9 – Wavelength relation (energy conservation)**

\[
\frac{1}{\lambda_p} = \frac{1}{\lambda_s} + \frac{1}{\lambda_i}
\]

---

## 📊 Output

This simulator generates:

- Signal wavelength vs. temperature  
- Idler wavelength vs. temperature  
- Combined tuning curves (\(\Delta k = 0\) phase-matching)

---

## 🗂️ Files

| File | Description |
|------|-------------|
| `phase_match.py` | Computes \(\Delta k\) using Equations 1–9 |
| `tuning_curves.py` | Plots phase-matched signal/idler wavelengths |
| `sellmeier.py` | Defines refractive index and temperature dependence (not shown) |

---

## ⚙️ Dependencies

- Python 3.7+
- NumPy
- SciPy
- Matplotlib
