function f = voltage_percentage_vs_phases(x, a)
%% V_r/V_c = R/\sqrt(R^2 + (\omega*L - 1/\omega*C)^2)

derivitor = 1 + (a(1).*x - (a(2).*x)^-1)^2
f= a(3)/sqrt(derivitor)


