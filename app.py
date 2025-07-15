import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from spdc_simulation import sellmeier_ppktp  # ye function tumhare existing file me hona chahiye

st.title("SPDC PPKTP GUI Simulator")

st.markdown("This simulator shows refractive index vs wavelength using PPKTP Sellmeier equation.")

temperature = st.slider("Select Temperature (°C)", 20.0, 100.0, 25.0)
wavelengths = np.linspace(0.6, 1.0, 300)

n_vals = [sellmeier_ppktp(lam, temperature) for lam in wavelengths]

fig, ax = plt.subplots()
ax.plot(wavelengths, n_vals, label=f"T = {temperature}°C")
ax.set_xlabel("Wavelength (µm)")
ax.set_ylabel("Refractive Index")
ax.set_title("Refractive Index vs Wavelength (PPKTP)")
ax.grid(True)
ax.legend()

st.pyplot(fig)

