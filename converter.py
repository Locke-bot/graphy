# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 13:38:53 2021

@author: Unrated
"""
import re, sys
from fractions import Fraction

a  =  \
'''
Fraction(191751, 6400), Fraction(8972816703296703, 10000000000000)], [Fraction(188853, 6400), Fraction(2224787064364207, 2500000000000)], [Fraction(1449, 50), Fraction(1765095962323391, 2000000000000)], [Fraction(91287, 3200), Fraction(218795284144427, 250000000000)], [Fraction(179193, 6400), Fraction(2169535729984301, 2500000000000)], [Fraction(27546093749999997, 1000000000000000), Fraction(8604474474097331, 10000000000000)], [Fraction(173397, 6400), Fraction(533175376766091, 625000000000)], [Fraction(170499, 6400), Fraction(4228568791208791, 5000000000000)], [Fraction(167601, 6400), Fraction(2095867284144427, 2500000000000)], [Fraction(164703, 6400), Fraction(4154900345368917, 5000000000000)], [Fraction(25282031250000003, 1000000000000000), Fraction(4118066122448979, 5000000000000)], [Fraction(158907, 6400), Fraction(1632492759811617, 2000000000000)], [Fraction(156009, 6400), Fraction(808879535321821, 1000000000000)], [Fraction(11961796875000001, 500000000000000), Fraction(1603025381475667, 2000000000000)], [Fraction(11735390624999999, 500000000000000), Fraction(3970729230769231, 5000000000000)], [Fraction(29463, 1280), Fraction(7867790015698587, 10000000000000)], [Fraction(1449, 64), Fraction(974265196232339, 1250000000000)], [Fraction(71001, 3200), Fraction(7720453124018837, 10000000000000)], [Fraction(10905234375000001, 500000000000000), Fraction(7646784678178963, 10000000000000)], [Fraction(10678828124999999, 500000000000000), Fraction(7573116232339089, 10000000000000)], [Fraction(67137, 3200), Fraction(3749723893249607, 5000000000000)], [Fraction(8211, 400), Fraction(7425779340659341, 10000000000000)], [Fraction(10075078125000001, 500000000000000), Fraction(3676055447409733, 5000000000000)], [Fraction(63273, 3200), Fraction(7278442448979591, 10000000000000)], [Fraction(483, 25), Fraction(3602387001569859, 5000000000000)], [Fraction(121233, 6400), Fraction(7131105557299843, 10000000000000)], [Fraction(59409, 3200), Fraction(55136227433281, 78125000000)], [Fraction(116403, 6400), Fraction(3491884332810047, 5000000000000)], [Fraction(28497, 1600), Fraction(6910100219780219, 10000000000000)], [Fraction(111573, 6400), Fraction(1367286354788069, 2000000000000)], [Fraction(54579, 3200), Fraction(676276332810047, 1000000000000)], [Fraction(106743, 6400), Fraction(1672273720565149, 2500000000000)], [Fraction(13041, 800), Fraction(3307713218210361, 5000000000000)], [Fraction(101913, 6400), Fraction(6541757990580847, 10000000000000)], [Fraction(49749, 3200), Fraction(6453355855572999, 10000000000000)], [Fraction(15169218749999999, 1000000000000000), Fraction(1594921852433281, 2500000000000)], [Fraction(14791875000000001, 1000000000000000), Fraction(251651410989011, 400000000000)], [Fraction(92253, 6400), Fraction(31088084144427, 50000000000)], [Fraction(44919, 3200), Fraction(122584293877551, 200000000000)], [Fraction(87423, 6400), Fraction(1513886562009419, 2500000000000)], [Fraction(13282499999999999, 1000000000000000), Fraction(2983572056514913, 5000000000000)], [Fraction(12905156250000001, 1000000000000000), Fraction(2939370989010989, 5000000000000)], [Fraction(40089, 3200), Fraction(361896240188383, 625000000000)], [Fraction(77763, 6400), Fraction(5701937708006279, 10000000000000)], [Fraction(18837, 1600), Fraction(5613535572998429, 10000000000000)], [Fraction(11395781249999999, 1000000000000000), Fraction(5525133437990581, 10000000000000)], [Fraction(11018437500000001, 1000000000000000), Fraction(5436731302982731, 10000000000000)], [Fraction(68103, 6400), Fraction(1333398869701727, 2500000000000)], [Fraction(8211, 800), Fraction(2622596671899529, 5000000000000)], [Fraction(63273, 6400), Fraction(5142057519623233, 10000000000000)], [Fraction(30429, 3200), Fraction(5038921695447409, 10000000000000)], [Fraction(9131718750000001, 1000000000000000), Fraction(987157174254317, 2000000000000)], [Fraction(14007, 1600), Fraction(4832650047095761, 10000000000000)], [Fraction(53613, 6400), Fraction(4729514222919937, 10000000000000)], [Fraction(7999687499999999, 1000000000000000), Fraction(4626378398744113, 10000000000000)], [Fraction(48783, 6400), Fraction(2254254442700157, 5000000000000)], [Fraction(1449, 200), Fraction(878127874411303, 2000000000000)], [Fraction(13735312500000001, 2000000000000000), Fraction(10681924646781789, 25000000000000)], [Fraction(20769, 3200), Fraction(4154900345368917, 10000000000000)], [Fraction(6112968749999999, 1000000000000000), Fraction(4037030832025117, 10000000000000)], [Fraction(9177, 1600), Fraction(30503340855573, 78125000000)], [Fraction(34293, 6400), Fraction(37718244270015697, 100000000000000)], [Fraction(9961875000000001, 2000000000000000), Fraction(9098053061224489, 25000000000000)], [Fraction(29463, 6400), Fraction(3491884332810047, 10000000000000)], [Fraction(4226249999999999, 1000000000000000), Fraction(1672273720565149, 5000000000000)], [Fraction(19244531249999999, 5000000000000000), Fraction(1591238430141287, 5000000000000)], [Fraction(11109, 3200), Fraction(6040812558869701, 20000000000000)], [Fraction(19803, 6400), Fraction(14291678492935637, 50000000000000)], [Fraction(4347, 1600), Fraction(1333398869701727, 5000000000000)], [Fraction(14973, 6400), Fraction(123762989010989, 500000000000)], [Fraction(6279, 3200), Fraction(2254254442700157, 10000000000000)], [Fraction(15848437499999999, 10000000000000000), Fraction(10092577080062793, 50000000000000)], [Fraction(483, 400), Fraction(1753309010989011, 10000000000000)], [Fraction(8301562499999999, 10000000000000000), Fraction(14291678492935637, 100000000000000)], [Fraction(1449, 3200), Fraction(10166245525902669, 100000000000000)]]
'''
# print(len(eval(a)))
py_c_frac_regex = re.compile(r'(-?\d+/\d+)')
# print(py_c_frac_regex.findall(a))
# print(py_c_frac_regex.findall(a))
def c_frac_py_frac(c_fraction): # c++ fraction to python fraction
    py_fraction = c_fraction.replace('{', '[').replace('}', ']').replace('"', '')
    return py_fraction

# def py_frac_c_frac(py_fraction): # python fraction to c++ fraction
    # c_fraction = py_fraction.replace('[', '{').replace(']', '}')
#     return py_c_frac_regex.sub(r'"\g<1>"', c_fraction)

def py_frac_c_frac(py_fraction): # python fraction to python fraction
    l = len(eval(py_fraction))
    print(type(py_fraction))
    c_fraction = []
    fractions = py_c_frac_regex.findall(py_fraction)
    print(fractions)
    for enum, fraction in enumerate(fractions):
        numerator, denominator = fraction.split('/')
        if enum % (l+1) == 0:
            c_fraction.append([])
        c_fraction[-1].append(f'Fraction("{numerator}", "{denominator}")')
    return str(c_fraction).replace("'", '').replace('[', '{').replace(']', '}')
    # return c_fraction

def c_frac_py(c_fraction): # c++ fraction to python list
    py_frac = eval(c_frac_py_frac(c_fraction)) # first convert to python fraction
    py_frac = [[float(i) for i in j] for j in py_frac]
    return py_frac

def py_c(py_list):
    if type(py_list) is str:
        return py_list.replace('[', '{').replace(']', '}')
    else:
        return str(py_list).replace('[', '{').replace(']', '}')

def py_py_frac(py_list): # python list to python fraction
    py_frac = [[Fraction(i) for i in j] for j in eval(py_list)]
    return py_frac

def py_c_frac(py_list): # python list to python fraction
    py_frac = py_py_frac(py_list) # convert list to fraction
    return py_frac_c_frac(str(py_frac))

def c_py(c): # c array to py list
    c = c.replace('{', '[').replace('}', ']')
    return eval(c)

def c_c_frac(c): # c array to c fraction
    py_list = c_py(c)
    py_frac = [[Fraction(i) for i in j] for j in py_list]
    # print(py_frac)
    c_frac = [[f'Fraction("{i.numerator}", "{i.denominator}")' for i in j] for j in py_frac]
    return str(c_frac).replace("'", '').replace('[', '{').replace(']', '}')
    
# print(py_c(c_frac_py(py_frac_c_frac(a))))
print(py_frac_c_frac(a).replace('},', '},\n'))
# print(py_c(c_frac_py(py_frac_c_frac(a))).replace('},', '},\n'))
# print(py_c(c_frac_py(py_frac_c_frac(a))))