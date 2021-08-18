from fractions import Fraction
from sympy import *
x = [[Fraction(0, 1), Fraction(0, 1), Fraction(0, 1), Fraction(0, 1), Fraction(0, 1), Fraction(0, 1), Fraction(0, 1), Fraction(0, 1), Fraction(0, 1), Fraction(0, 1), Fraction(1, 1), Fraction(5, 1)],
 [Fraction(1, 1), Fraction(1, 1), Fraction(1, 1), Fraction(1, 1), Fraction(1, 1), Fraction(1, 1), Fraction(1, 1), Fraction(1, 1), Fraction(1, 1), Fraction(1, 1), Fraction(1, 1), Fraction(33, 1)],
 [Fraction(1024, 1), Fraction(512, 1), Fraction(256, 1), Fraction(128, 1), Fraction(64, 1), Fraction(32, 1), Fraction(16, 1), Fraction(8, 1), Fraction(4, 1), Fraction(2, 1), Fraction(1, 1), Fraction(397, 1)],
 [Fraction(59049, 1), Fraction(19683, 1), Fraction(6561, 1), Fraction(2187, 1), Fraction(729, 1), Fraction(243, 1), Fraction(81, 1), Fraction(27, 1), Fraction(9, 1), Fraction(3, 1), Fraction(1, 1), Fraction(1961, 1)],
 [Fraction(1048576, 1), Fraction(262144, 1), Fraction(65536, 1), Fraction(16384, 1), Fraction(4096, 1), Fraction(1024, 1), Fraction(256, 1), Fraction(64, 1), Fraction(16, 1), Fraction(4, 1), Fraction(1, 1), Fraction(6165, 1)],
 [Fraction(9765625, 1), Fraction(1953125, 1), Fraction(390625, 1), Fraction(78125, 1), Fraction(15625, 1), Fraction(3125, 1), Fraction(625, 1), Fraction(125, 1), Fraction(25, 1), Fraction(5, 1), Fraction(1, 1), Fraction(15025, 1)],
 [Fraction(60466176, 1), Fraction(10077696, 1), Fraction(1679616, 1), Fraction(279936, 1), Fraction(46656, 1), Fraction(7776, 1), Fraction(1296, 1), Fraction(216, 1), Fraction(36, 1), Fraction(6, 1), Fraction(1, 1), Fraction(31133, 1)],
 [Fraction(282475249, 1), Fraction(40353607, 1), Fraction(5764801, 1), Fraction(823543, 1), Fraction(117649, 1), Fraction(16807, 1), Fraction(2401, 1), Fraction(343, 1), Fraction(49, 1), Fraction(7, 1), Fraction(1, 1), Fraction(57657, 1)],
 [Fraction(1073741824, 1), Fraction(134217728, 1), Fraction(16777216, 1), Fraction(2097152, 1), Fraction(262144, 1), Fraction(32768, 1), Fraction(4096, 1), Fraction(512, 1), Fraction(64, 1), Fraction(8, 1), Fraction(1, 1), Fraction(98341, 1)],
 [Fraction(3486784401, 1), Fraction(387420489, 1), Fraction(43046721, 1), Fraction(4782969, 1), Fraction(531441, 1), Fraction(59049, 1), Fraction(6561, 1), Fraction(729, 1), Fraction(81, 1), Fraction(9, 1), Fraction(1, 1), Fraction(157505, 1)],
 [Fraction(10000000000, 1), Fraction(1000000000, 1), Fraction(100000000, 1), Fraction(10000000, 1), Fraction(1000000, 1), Fraction(100000, 1), Fraction(10000, 1), Fraction(1000, 1), Fraction(100, 1), Fraction(10, 1), Fraction(1, 1), Fraction(240045, 1)]]


# y = [[Fraction(76000)], [Fraction(45)], [Fraction(56)], [Fraction(-9)], [Fraction(4)]]
y = [[Fraction(5)], [Fraction(33)], [Fraction(397)], [Fraction(1961)], [Fraction(6165)], [Fraction(15025)], [Fraction(31133)],  [Fraction(57657)], [Fraction(98341)], [Fraction(157505)], [Fraction(240045)]]

xx = Matrix(x)
yy = Matrix(y)

print(linsolve((xx, yy)))