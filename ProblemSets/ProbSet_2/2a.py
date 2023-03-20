import sympy as sp

th1, th2, th3 = sp.symbols("theta_1, theta_2, theta_3")
th1_d, th2_d, th3_d = sp.symbols("theta__'_1 theta__'_2 theta__'_3")
Omega = sp.symbols("Omega")
omega_1, omega_2, omega_3 = sp.symbols("omega_1 omega_2 omega_3")

#R_1
R_1 = sp.Matrix([[1, 0, 0], [0, sp.cos(th1), sp.sin(th1)], [0, -sp.sin(th1), sp.cos(th1)]])
# R_2
R_2 = sp.Matrix([[sp.cos(th2), 0, -sp.sin(th2)], [0, 1, 0], [sp.sin(th2), 0, sp.cos(th2)]])
# R_3
R_3 = sp.Matrix([[sp.cos(th3), sp.sin(th3), 0], [-sp.sin(th3), sp.cos(th3), 0], [0, 0, 1]])
#sp.pprint([R_1, R_2, R_3])

P = ((R_1.T @ R_2.T @ R_3.T)[2, :]).T
X_1 = (R_2.T @ R_3.T)[0, :]
X_2 = (R_3.T)[1, :]
X_3 = sp.Matrix([0, 0, 1]).T
Tr = sp.Matrix([X_1, X_2, X_3])
omega = sp.Matrix([[omega_1], [omega_2], [omega_3]])
invTr_T = sp.simplify(Tr.inv()).T
dots = sp.simplify( invTr_T @ (omega - Omega * P) )
sp.print_latex(dots)
