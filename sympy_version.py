# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 20:45:03 2021

@author: Unrated
"""
import graphene, time
from benchmark import prepare_lists
from bs4 import BeautifulSoup as soup
import matplotlib.pyplot as plt
from decimal import Decimal
import random, itertools
from fractions import Fraction
from scipy import linalg
import numpy as np
from sympy import *
import mpmath
import string, sys

# sys.exit()
# 1.1*x**0.9 - 31.000000001*x**4+4*x+5 shitfaced.png
def preemptZero(x):
    if x == 0 and end < 0: # can't raise zero to negative power
        x = 1e-15
    return x

# def calc(x):
#     try:
#         return graphene.Fraction('0.8')*graphene.Fraction(str(Decimal(x**-0.1))) - graphene.Fraction('31.000000001')*graphene.Fraction(str(x**4)) + graphene.Fraction('4')*graphene.Fraction(str(x.numerator), str(x.denominator)) + graphene.Fraction('5')
#     except TypeError:
#         return graphene.Fraction('0.8')*graphene.Fraction(str(x**-0.1)) - graphene.Fraction('31.000000001')*graphene.Fraction(str(x**4)) + graphene.Fraction('4')*graphene.Fraction(str(x.numerator), str(x.denominator)) + graphene.Fraction('5')
    # return graphene.Fraction('1.00000000000000001')*graphene.Fraction(str(Decimal(x**2.5)))
    
start = Fraction(5)
end = Fraction(0, 1)
step = Fraction(1, 1) # don't give it input as a float, ever.

startloop = Fraction(76, 1)
endloop = Fraction(0, 1)
steploop = Fraction(1, 1)
# step = Fraction(10, 10)
# step = 0.4
# print(start, end, step)
# sys.exit()

# all_array = [i for i in zip(input_x[::int(200/s)], out_y[::int(200/s)])]
# all_array = [[i, i] for i in range(10, 110, 10)] + [
# all_array = [[Fraction(i), Fraction(calc(i))] for i in np.arange(end, start+step, step, dtype="object")]
# all_array = [[Fraction(187, 1), Fraction(249, 1)], [Fraction(179, 1), Fraction(249, 1)], [Fraction(181, 1), Fraction(248, 1)], [Fraction(203, 1), Fraction(245, 1)], [Fraction(205, 1), Fraction(244, 1)], [Fraction(217, 1), Fraction(242, 1)], [Fraction(219, 1), Fraction(241, 1)], [Fraction(220, 1), Fraction(240, 1)], [Fraction(229, 1), Fraction(238, 1)], [Fraction(229, 1), Fraction(237, 1)], [Fraction(236, 1), Fraction(235, 1)], [Fraction(242, 1), Fraction(233, 1)], [Fraction(247, 1), Fraction(231, 1)], [Fraction(251, 1), Fraction(229, 1)], [Fraction(254, 1), Fraction(227, 1)], [Fraction(257, 1), Fraction(225, 1)], [Fraction(259, 1), Fraction(223, 1)], [Fraction(266, 1), Fraction(220, 1)], [Fraction(267, 1), Fraction(218, 1)], [Fraction(273, 1), Fraction(215, 1)], [Fraction(273, 1), Fraction(213, 1)], [Fraction(278, 1), Fraction(210, 1)], [Fraction(282, 1), Fraction(207, 1)], [Fraction(286, 1), Fraction(204, 1)], [Fraction(286, 1), Fraction(202, 1)], [Fraction(290, 1), Fraction(199, 1)], [Fraction(292, 1), Fraction(196, 1)], [Fraction(296, 1), Fraction(193, 1)], [Fraction(300, 1), Fraction(190, 1)], [Fraction(300, 1), Fraction(188, 1)], [Fraction(304, 1), Fraction(184, 1)], [Fraction(306, 1), Fraction(181, 1)], [Fraction(310, 1), Fraction(177, 1)], [Fraction(314, 1), Fraction(173, 1)], [Fraction(316, 1), Fraction(170, 1)], [Fraction(319, 1), Fraction(166, 1)], [Fraction(320, 1), Fraction(163, 1)], [Fraction(323, 1), Fraction(159, 1)], [Fraction(325, 1), Fraction(155, 1)], [Fraction(328, 1), Fraction(151, 1)], [Fraction(331, 1), Fraction(147, 1)], [Fraction(334, 1), Fraction(143, 1)], [Fraction(335, 1), Fraction(140, 1)], [Fraction(337, 1), Fraction(136, 1)], [Fraction(340, 1), Fraction(132, 1)], [Fraction(342, 1), Fraction(128, 1)], [Fraction(343, 1), Fraction(125, 1)], [Fraction(345, 1), Fraction(121, 1)], [Fraction(347, 1), Fraction(117, 1)], [Fraction(349, 1), Fraction(113, 1)], [Fraction(351, 1), Fraction(109, 1)], [Fraction(353, 1), Fraction(105, 1)], [Fraction(355, 1), Fraction(101, 1)], [Fraction(358, 1), Fraction(97, 1)], [Fraction(360, 1), Fraction(93, 1)], [Fraction(362, 1), Fraction(89, 1)], [Fraction(363, 1), Fraction(85, 1)], [Fraction(365, 1), Fraction(81, 1)], [Fraction(367, 1), Fraction(77, 1)], [Fraction(368, 1), Fraction(73, 1)], [Fraction(370, 1), Fraction(69, 1)], [Fraction(372, 1), Fraction(65, 1)], [Fraction(373, 1), Fraction(61, 1)], [Fraction(375, 1), Fraction(57, 1)]]
# all_array = all_array[:30]
# remove = True
# all_array = []
# all_array = [[Fraction(8972816703296703, 10000000000000), Fraction(191751, 6400)], [Fraction(2224787064364207, 2500000000000), Fraction(188853, 6400)], [Fraction(1765095962323391, 2000000000000), Fraction(1449, 50)], [Fraction(218795284144427, 250000000000), Fraction(91287, 3200)], [Fraction(2169535729984301, 2500000000000), Fraction(179193, 6400)], [Fraction(8604474474097331, 10000000000000), Fraction(27546093749999997, 1000000000000000)], [Fraction(533175376766091, 625000000000), Fraction(173397, 6400)], [Fraction(4228568791208791, 5000000000000), Fraction(170499, 6400)], [Fraction(2095867284144427, 2500000000000), Fraction(167601, 6400)], [Fraction(4154900345368917, 5000000000000), Fraction(164703, 6400)], [Fraction(4118066122448979, 5000000000000), Fraction(25282031250000003, 1000000000000000)], [Fraction(1632492759811617, 2000000000000), Fraction(158907, 6400)], [Fraction(808879535321821, 1000000000000), Fraction(156009, 6400)], [Fraction(1603025381475667, 2000000000000), Fraction(11961796875000001, 500000000000000)], [Fraction(3970729230769231, 5000000000000), Fraction(11735390624999999, 500000000000000)], [Fraction(7867790015698587, 10000000000000), Fraction(29463, 1280)], [Fraction(974265196232339, 1250000000000), Fraction(1449, 64)], [Fraction(7720453124018837, 10000000000000), Fraction(71001, 3200)], [Fraction(7646784678178963, 10000000000000), Fraction(10905234375000001, 500000000000000)], [Fraction(7573116232339089, 10000000000000), Fraction(10678828124999999, 500000000000000)], [Fraction(3749723893249607, 5000000000000), Fraction(67137, 3200)], [Fraction(7425779340659341, 10000000000000), Fraction(8211, 400)], [Fraction(3676055447409733, 5000000000000), Fraction(10075078125000001, 500000000000000)], [Fraction(7278442448979591, 10000000000000), Fraction(63273, 3200)], [Fraction(3602387001569859, 5000000000000), Fraction(483, 25)], [Fraction(7131105557299843, 10000000000000), Fraction(121233, 6400)], [Fraction(55136227433281, 78125000000), Fraction(59409, 3200)], [Fraction(3491884332810047, 5000000000000), Fraction(116403, 6400)], [Fraction(6910100219780219, 10000000000000), Fraction(28497, 1600)], [Fraction(1367286354788069, 2000000000000), Fraction(111573, 6400)], [Fraction(676276332810047, 1000000000000), Fraction(54579, 3200)], [Fraction(1672273720565149, 2500000000000), Fraction(106743, 6400)], [Fraction(3307713218210361, 5000000000000), Fraction(13041, 800)], [Fraction(6541757990580847, 10000000000000), Fraction(101913, 6400)], [Fraction(6453355855572999, 10000000000000), Fraction(49749, 3200)], [Fraction(1594921852433281, 2500000000000), Fraction(15169218749999999, 1000000000000000)], [Fraction(251651410989011, 400000000000), Fraction(14791875000000001, 1000000000000000)], [Fraction(31088084144427, 50000000000), Fraction(92253, 6400)], [Fraction(122584293877551, 200000000000), Fraction(44919, 3200)], [Fraction(1513886562009419, 2500000000000), Fraction(87423, 6400)], [Fraction(2983572056514913, 5000000000000), Fraction(13282499999999999, 1000000000000000)], [Fraction(2939370989010989, 5000000000000), Fraction(12905156250000001, 1000000000000000)], [Fraction(361896240188383, 625000000000), Fraction(40089, 3200)], [Fraction(5701937708006279, 10000000000000), Fraction(77763, 6400)], [Fraction(5613535572998429, 10000000000000), Fraction(18837, 1600)], [Fraction(5525133437990581, 10000000000000), Fraction(11395781249999999, 1000000000000000)], [Fraction(5436731302982731, 10000000000000), Fraction(11018437500000001, 1000000000000000)], [Fraction(1333398869701727, 2500000000000), Fraction(68103, 6400)], [Fraction(2622596671899529, 5000000000000), Fraction(8211, 800)], [Fraction(5142057519623233, 10000000000000), Fraction(63273, 6400)], [Fraction(5038921695447409, 10000000000000), Fraction(30429, 3200)], [Fraction(987157174254317, 2000000000000), Fraction(9131718750000001, 1000000000000000)], [Fraction(4832650047095761, 10000000000000), Fraction(14007, 1600)], [Fraction(4729514222919937, 10000000000000), Fraction(53613, 6400)], [Fraction(4626378398744113, 10000000000000), Fraction(7999687499999999, 1000000000000000)], [Fraction(2254254442700157, 5000000000000), Fraction(48783, 6400)], [Fraction(878127874411303, 2000000000000), Fraction(1449, 200)], [Fraction(10681924646781789, 25000000000000), Fraction(13735312500000001, 2000000000000000)], [Fraction(4154900345368917, 10000000000000), Fraction(20769, 3200)], [Fraction(4037030832025117, 10000000000000), Fraction(6112968749999999, 1000000000000000)], [Fraction(30503340855573, 78125000000), Fraction(9177, 1600)], [Fraction(37718244270015697, 100000000000000), Fraction(34293, 6400)], [Fraction(9098053061224489, 25000000000000), Fraction(9961875000000001, 2000000000000000)], [Fraction(3491884332810047, 10000000000000), Fraction(29463, 6400)], [Fraction(1672273720565149, 5000000000000), Fraction(4226249999999999, 1000000000000000)], [Fraction(1591238430141287, 5000000000000), Fraction(19244531249999999, 5000000000000000)], [Fraction(6040812558869701, 20000000000000), Fraction(11109, 3200)], [Fraction(14291678492935637, 50000000000000), Fraction(19803, 6400)], [Fraction(1333398869701727, 5000000000000), Fraction(4347, 1600)], [Fraction(123762989010989, 500000000000), Fraction(14973, 6400)], [Fraction(2254254442700157, 10000000000000), Fraction(6279, 3200)], [Fraction(10092577080062793, 50000000000000), Fraction(15848437499999999, 10000000000000000)], [Fraction(1753309010989011, 10000000000000), Fraction(483, 400)], [Fraction(14291678492935637, 100000000000000), Fraction(8301562499999999, 10000000000000000)], [Fraction(10166245525902669, 100000000000000), Fraction(1449, 3200)]]
all_array = [[Fraction(6003, 200), Fraction(895670173076923, 1000000000000)], [Fraction(29768571428571427, 1000000000000000), Fraction(4410667980769231, 5000000000000)], [Fraction(29522142857142857, 1000000000000000), Fraction(866340923076923, 1000000000000)], [Fraction(29275714285714287, 1000000000000000), Fraction(4264021730769231, 5000000000000)], [Fraction(29029285714285713, 1000000000000000), Fraction(837011673076923, 1000000000000)], [Fraction(28782857142857143, 1000000000000000), Fraction(411737548076923, 500000000000)], [Fraction(2853642857142857, 100000000000000), Fraction(2024846298076923, 2500000000000)], [Fraction(2829, 100), Fraction(7964019423076923, 10000000000000)], [Fraction(2804357142857143, 100000000000000), Fraction(7828653653846153, 10000000000000)], [Fraction(5559428571428571, 200000000000000), Fraction(961660985576923, 1250000000000)], [Fraction(5510142857142857, 200000000000000), Fraction(1511584423076923, 2000000000000)], [Fraction(2730428571428571, 100000000000000), Fraction(3711278173076923, 5000000000000)], [Fraction(1352892857142857, 50000000000000), Fraction(1821797644230769, 2500000000000)], [Fraction(2681142857142857, 100000000000000), Fraction(1787956201923077, 2500000000000)], [Fraction(13282499999999999, 500000000000000), Fraction(3508229519230769, 5000000000000)], [Fraction(6579642857142857, 250000000000000), Fraction(6881093269230769, 10000000000000)], [Fraction(13036071428571427, 500000000000000), Fraction(6768288461538461, 10000000000000)], [Fraction(6456428571428571, 250000000000000), Fraction(1658230673076923, 2500000000000)], [Fraction(12789642857142857, 500000000000000), Fraction(1304023576923077, 2000000000000)], [Fraction(3166607142857143, 125000000000000), Fraction(1276950423076923, 2000000000000)], [Fraction(12543214285714287, 500000000000000), Fraction(6271947307692307, 10000000000000)], [Fraction(621, 25), Fraction(3068290769230769, 5000000000000)], [Fraction(12296785714285713, 500000000000000), Fraction(6023776730769231, 10000000000000)], [Fraction(3043392857142857, 125000000000000), Fraction(2955485961538461, 5000000000000)], [Fraction(12050357142857143, 500000000000000), Fraction(2887803076923077, 5000000000000)], [Fraction(5963571428571429, 250000000000000), Fraction(2831400673076923, 5000000000000)], [Fraction(11803928571428571, 500000000000000), Fraction(2774998269230769, 5000000000000)], [Fraction(5840357142857143, 250000000000000), Fraction(543719173076923, 1000000000000)], [Fraction(4623, 200), Fraction(2662193461538461, 5000000000000)], [Fraction(2286857142857143, 100000000000000), Fraction(1042316423076923, 2000000000000)], [Fraction(11311071428571429, 500000000000000), Fraction(50987773076923077, 100000000000000)], [Fraction(4475142857142857, 200000000000000), Fraction(4985972499999999, 10000000000000)], [Fraction(11064642857142857, 500000000000000), Fraction(1218291923076923, 2500000000000)], [Fraction(1094142857142857, 50000000000000), Fraction(9520725769230769, 20000000000000)], [Fraction(10793571428571429, 500000000000000), Fraction(4647558076923077, 10000000000000)], [Fraction(5335178571428571, 250000000000000), Fraction(22673766346153843, 50000000000000)], [Fraction(10522499999999999, 500000000000000), Fraction(44219484615384613, 100000000000000)], [Fraction(5199642857142857, 250000000000000), Fraction(21545718269230767, 50000000000000)], [Fraction(10251428571428571, 500000000000000), Fraction(2098169423076923, 5000000000000)], [Fraction(2025642857142857, 100000000000000), Fraction(40835340384615387, 100000000000000)], [Fraction(3992142857142857, 200000000000000), Fraction(397072923076923, 1000000000000)], [Fraction(3933, 200), Fraction(3857924423076923, 10000000000000)], [Fraction(4842321428571429, 250000000000000), Fraction(7490239230769231, 20000000000000)], [Fraction(19073571428571427, 1000000000000000), Fraction(9080787019230769, 25000000000000)], [Fraction(938892857142857, 50000000000000), Fraction(8798774999999999, 25000000000000)], [Fraction(9241071428571429, 500000000000000), Fraction(851676298076923, 2500000000000)], [Fraction(1818642857142857, 100000000000000), Fraction(8234750961538461, 25000000000000)], [Fraction(17841428571428573, 1000000000000000), Fraction(3181095576923077, 10000000000000)], [Fraction(17545714285714283, 1000000000000000), Fraction(3068290769230769, 10000000000000)], [Fraction(4300178571428571, 250000000000000), Fraction(2955485961538461, 10000000000000)], [Fraction(3371142857142857, 200000000000000), Fraction(1421340576923077, 5000000000000)], [Fraction(8255357142857143, 500000000000000), Fraction(1364938173076923, 5000000000000)], [Fraction(4041428571428571, 250000000000000), Fraction(1308535769230769, 5000000000000)], [Fraction(15820714285714287, 1000000000000000), Fraction(25042667307692307, 100000000000000)], [Fraction(7737857142857143, 500000000000000), Fraction(23914619230769227, 100000000000000)], [Fraction(1508142857142857, 100000000000000), Fraction(11393285576923077, 50000000000000)], [Fraction(1835892857142857, 125000000000000), Fraction(866340923076923, 4000000000000)], [Fraction(14292857142857141, 1000000000000000), Fraction(10265237499999999, 50000000000000)], [Fraction(3474642857142857, 250000000000000), Fraction(9701213461538461, 50000000000000)], [Fraction(6752142857142857, 500000000000000), Fraction(9137189423076923, 50000000000000)], [Fraction(2612142857142857, 200000000000000), Fraction(17146330769230767, 100000000000000)], [Fraction(12617142857142857, 1000000000000000), Fraction(1601828269230769, 10000000000000)], [Fraction(3043392857142857, 250000000000000), Fraction(7445117307692307, 50000000000000)], [Fraction(5840357142857143, 500000000000000), Fraction(6881093269230769, 50000000000000)], [Fraction(5593928571428571, 500000000000000), Fraction(12634138461538461, 100000000000000)], [Fraction(5322857142857143, 500000000000000), Fraction(11506090384615383, 100000000000000)], [Fraction(1010357142857143, 100000000000000), Fraction(10378042307692307, 100000000000000)], [Fraction(9561428571428571, 1000000000000000), Fraction(924999423076923, 10000000000000)], [Fraction(4460357142857143, 500000000000000), Fraction(8121946153846153, 100000000000000)], [Fraction(207, 25), Fraction(6993898076923077, 100000000000000)], [Fraction(1508142857142857, 200000000000000), Fraction(117317, 2000)], [Fraction(6752142857142857, 1000000000000000), Fraction(23689009615384613, 500000000000000)], [Fraction(1173, 200), Fraction(1804876923076923, 50000000000000)], [Fraction(2390357142857143, 500000000000000), Fraction(2481705769230769, 100000000000000)], [Fraction(1700357142857143, 500000000000000), Fraction(6768288461538461, 500000000000000)]]
# all_array.reverse()
# all_array = [[2, 4], [5, 25], [10, 100]]
n = 0
# n = len(all_array)-10
power = 3.5
all_array =  all_array[n:n+5]
# try:
#     all_array =  [[Fraction(Decimal(j[0]**power)), Fraction(Decimal(j[1]**power))] for j in [i for i in all_array[:20]]]
# except TypeError:
#     all_array =  [[Fraction(j[0]**power), Fraction(j[1]**power)] for j in [i for i in all_array[:20]]]
# print([[float(i) for i in sublst] for sublst in all_array])
# all_array = [[i[0], i[0]**2] for i in all_array]
# print([[float(i) for i in sublst] for sublst in all_array])
# print(all_array)
# all_array = [[4.87012987012987, 27.17391304347826], [6.4935064935064934, 54.34782608695652], [8.116883116883116, 67.93478260869566], [9.74025974025974, 108.69565217391305], [11.363636363636363, 163.0434782608696], [12.987012987012987, 203.80434782608697], [14.61038961038961, 244.56521739130437], [16.233766233766232, 312.5], [17.857142857142858, 380.4347826086957], [19.48051948051948, 448.3695652173913], [22.727272727272727, 597.8260869565217], [24.35064935064935, 692.9347826086957], [25.974025974025974, 774.4565217391305], [27.597402597402596, 855.9782608695652], [29.22077922077922, 978.2608695652175], [30.844155844155843, 1086.9565217391305], [32.467532467532465, 1182.0652173913045], [34.09090909090909, 1277.1739130434783], [35.714285714285715, 1426.6304347826087], [37.33766233766234, 1562.5000000000002], [38.96103896103896, 1671.1956521739132], [40.58441558441558, 1793.4782608695652], [42.20779220779221, 1970.108695652174], [43.83116883116883, 2119.5652173913045]]
# print(all_array.__len__())
# sys.exit()
# for enum, frac in enumerate(np.arange(endloop, startloop, steploop, dtype="object")):
#     if frac == 0:
#         remove = False
#         continue
#     # print('end', frac)
#     calcd = calc(frac)
#     all_array.append([frac, Fraction(int(calcd.get_num()), int(calcd.get_den()))])
# if remove:
#     all_array.pop()
# initial_y = [[enum, i[1]] for enum, i in enumerate(all_array)]
# all_array.pop()
# print(all_array)
# sys.exit() 
#   sys.exit()
# init_y = [calc(i) for i in np.arange(0, start+1, 0.2)]
# plt.figure()
# plt.plot([i[0] for i in all_array], initial_y, label='mad')
# print(len(all_array), 'len')
# print(all_array)
# print(all_array.__len__())

def polywer(x): # start is the greater than end
    # print(x, type(x), [x**i for i in np.arange(start, end-step, -step, dtype="object")])
    # x = preemptZero(x)
    return [Fraction(x**i) for i in np.arange(end, start, step, dtype="object")][::-1]

arr_x = None
graph = None
def poly_all(arr):
    global arr_x, graph;
    arr_x = np.array([polywer(i[0]) for i in arr], dtype='float64')
    arr_y = np.array([[i[1]] for i in arr], dtype='float64')
    x = np.array([polywer(i[0]) for i in arr], dtype='object') + Fraction()
    # matrixx = Matrix(x)
    # print(matrixx.det())
    # print(len(arr_x), len(arr_x[0]))
    # print(np.linalg.solve(arr_x, arr_y))
    # print()
    # sys.exit()
    # print(arr_x)
    y = np.array([[i[1]] for i in arr])
    # print(y)
    fd = time.time()
    matrixy = Matrix(y)
    ds = time.time()
    f = graphene.Fraction
    x = np.ndarray.tolist(x)
    prepare_lists(x, y)
    # print('trust bust')
    grap = [[f(str(i.numerator), str(i.denominator)) for i in sub_lst] for sub_lst in x]
    print(grap[0], grap[1])
    # print(grap)
    # sys.exit()
    # grap = [[f'Fraction({i.numerator}, {i.denominator})' for i in sub_lst] for sub_lst in x]
    # print(grap)
    # print([[eval(str(i)) for i in sub_lst] for sub_lst in x])
    print(f'A {len(grap)} by {len(grap[0])} matrix')
    # sys.exit()
    ay = time.time()
    # print(grap)
    graph = graphene.GaussianElimination(grap)
    print(f'graphene took {time.time()-ay} sec')
    # print(graph)
    print([eval(str(i)) for i in graph])
    # print(f'custom shit took {time.time()-ds}')
    
    # print(matrixx)
    # print(matrixy)
    # print(mpmath.qr_solve(x, np.ndarray.tolist(arr_y)))
    # print(matrixx**-1 * arr_y)
    # arr_x = np.array([polywer(i[0]) for i in arr], dtype='object')
    print('Matrix')
    # print(x)
    # print(arr_x, 'arr', arr_x[6], arr[6][0]==6, polywer(arr[6][0]), polywer(6))
    # inv = np.linalg.inv(arr_x,)
    # x = np.ndarray.tolist(arr_x)
    # inv = getMatrixInverse(x)
    # inv = np.array(inv)
    # print('why')
    # print(inv)
    # x = np.dot(inv, arr_x)
    # print(np.ndarray.tolist(x))
    # print(inv)
    # return np.dot(inv, arr_y,)
    return np.linalg.solve(arr_x, arr_y)

def readable(arr):
    print('A')

def abacus(x):
    lst = [2.08068745e-02, -7.84285307e-02, -6.78604187e-02, 1.26770834e-01, -1.82963752e+03, 7.31722515e+04, -1.15173266e+06,  9.13788534e+06, -3.89440418e+07, 8.86267389e+07, -9.90133333e+07, 4.12731459e+07, 8.00000000e+00][::-1]
    return

pw = poly_all(all_array)
# print(pw)
sys.exit()
print('power')
# print(pw)
cv = 0
for enum, i in enumerate(arr_x):
    if enum == 6:
        # print(i, 'hi')
        for var, j in enumerate(i):
            val = j*pw[var][0]
            cv += val
        # print(cv, 'hans', enum)
        # print(np.dot(i, pw), 'hans', enum)
# print()
for enum, i in enumerate(arr_x):
        # print(np.dot(i, pw), 'hans', enum)
        pass

for enum, i in enumerate(all_array):
        pass
        # print('mf', i[0], get_function(pw, i[0]), 'model', initial_y[enum][::-1])
print('=====')
print()
# print()
# print(init_y, start, end)
# last_y = itertools.chain.from_iterable([np.ndarray.tolist(get_function(pw, i)) for i in np.arange(0, start+1, 0.2)])
# print(list(last_y))
# print('===last===')
print([[i, *np.ndarray.tolist(j)] for i, j in zip(list(np.arange(end,start+step, step, dtype="object"))[::-1], pw) if np.ndarray.tolist(j)[0] != 0])
# print('graph', graph)

print(list(np.arange(end, start, step)))
def get_function(arr, x):
    # x = preemptZero(x)
    power_list = list(np.arange(end, start, step))
    count = 0
    for i in arr:
        count +=  i*x**power_list.pop()
    # printa(len(power_list), 'na d thing')
    return count

# print(list(filter(lambda _: _[1] > 10e-5, [[i, *np.ndarray.tolist(j)] for i, j in zip(list(np.arange(end,start, step, dtype="object"))[::-1], pw) if np.ndarray.tolist(j)[0] != 0])))
xxx = [i[0] for i in all_array]
xxy = [i[1] for i in all_array]
# xxx.remove(0)
# print(graph)
# print(get_function([Fraction(int(i.get_num()), int(i.get_den())) for i in graph], 0))
coeff = [Fraction(int(i.get_num()), int(i.get_den())) for i in graph]
yyy = [get_function(coeff, i) for i in xxx]
print()
float_x = [float(i[1]) for i in all_array]
# print(float_x)
# print()
# print('yyy', yyy)
float_y = [float(i) for i in yyy]
# print('yyy')
print(xxy == yyy)
# plt.figure()
plt.grid
plt.plot(xxx,  yyy)
plt.show()