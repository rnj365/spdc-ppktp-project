def sellmeier_ppktp(lambda_um, T):
    # Sellmeier constants for PPKTP (Z-axis)
    A = 4.59423
    B = 0.06206
    C = 0.04763
    D = 110.80672
    E = 86.12171

    lam2 = lambda_um ** 2
    n2 = A + B / (lam2 - C) + D / (lam2 - E)
    n = n2 ** 0.5

    # Optional: temperature correction
    dn_dT = 1e-5
    n_corrected = n + dn_dT * (T - 25)
    return n_corrected
