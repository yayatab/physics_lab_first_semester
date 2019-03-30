function f = phase_as_function_of_omega(x, a)
%% \phi = arctan( (\omega*L - 1/\omega*C)/R)

f= arctan(a(1).*x - 1/(a(2).*x))


