function f = voltage_percentage_vs_phases(x, a)
%% V_r/V_c = R/\sqrt(R^2 + (\omega*L - 1/\omega*C)^2)
%% a1 = L/RT
%% a2 = R+tot
%% a3 = Rr*C
derivitor = 1 + (a(1).*x - 1./(a(2).*x)).^2;
f= a(3)./sqrt(derivitor);

