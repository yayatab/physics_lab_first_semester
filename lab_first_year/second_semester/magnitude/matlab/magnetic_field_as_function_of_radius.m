function f = magnetic_field_as_function_of_radius(x, a)
%% y = a_1 \times 1/(x-a_2)^a_3 + a_4
% y = B/ mue_0
% x = r
% a_1 == m/ 2pi * cos(theta =0 )
% a_3 = 3
% a_2, a_4 free parameters
    derivitor = (x .- a(2))^a(3)
    f = a(1) .* 1./derivitor + a(4)


