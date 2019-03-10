
function f = first_messure (x,a)
% a(1) = v_0, a(2) = \emoga, a(3) = \phi, a(4)= error in messurment
b = sin(a(2).*x + a(3));
f = a(1).*b +a(4);
% i'ts ok that it won't fit.there is toooooooo many errors.