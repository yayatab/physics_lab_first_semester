function f = electro_magnetic_force(x, a)
%% y = a_1 \cdot sin(a_2 * x -a_e) + a_4
% y = volt
% x = time
% a_1 == A,plitude
% a_2 = omega
% a_3, a_4 free parameters
    f = a(1) .* sin(a(2) .* x - a(3))+ a(4)


