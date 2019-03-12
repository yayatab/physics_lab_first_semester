function f = rc_circuit (x,a)
f = a(1) + a(2).*exp(-x./a(3));
