import json
import os
from pdata import *

# table = [
#         "Name", 
#         "Symbol",
#         "Atomic Number",
#         "Atomic Weight (u.m)",
#         "Density (g/cm³)",
#         "Melting Point (K)",
#         "Boiling Point (K)",
#         "Atomic Radius (pm)",
#         "Covalent Radius (pm)",
#         "Ionic Radius (pm)",
#         "Atomic Volume (cm³/mol)",
#         "Specific Heat (@20°C J/(K*mol))",
#         "Fusion Heat (kJ/mol)",
#         "Evaporation Heat (kJ/mol)",
#         "Thermal Conductivity (@25°C W/(m*K))",
#         "Debye temperature (K)",
#         "Pauling Negativity Number",
#         "First Ionizing Energy (kJ/mol)",
#         "Oxidation states",
#         "Electronic Configuration",
#         "Lattice structure",
#         "Lattice constant (Å)",
#         "Lattice c/a ratio",
#         "Appearance",
#         "Discovery date",
#         "Discovered by",
#         "Named after"]

# property_lst =[["Hydrogen",
#          "H",
#          "1",
#          "1.00794",
#          "0.0708 (@ -253°C)",
#          "14.01",
#         "20.28",
#          "53-79",
#          "32",
#          "54 (-1e)",
#          "14.1",
#          "0.904 (H-H)",
#          "0.117 (H-H)",
#          "0.1815",
#          "110.00",
#          "2.20",
#          "1311.3",
#          "1, 0, -1",
#          "1s¹",
#          "HEX",
#          "3.750",
#          "1.731",
#          "Colorless, odorless, tasteless gas",
#          "1766 (England)",
#          "Henry Cavendish",
#          "Greek: hydro (water) and genes (generate)",
#          "n/a"
# ],[ "Helium",
#     "He",
#     "2",
#     "4.002602",
#     "0.147 (@ -270°C)",
#     "0.95",
#     "4.216",
#     "28-31",
#     "28-140",
#     "93",
#     "31.8",
#     "n/a",
#     "5.188",
#     "n/a",
#     "4.5",
#     "2361.3",
#     "0",
#     "1s²",
#     "HEX",
#     "3.570",
#     "1.633",
#     "Inert, color",
#     "n/a",
#     "n/a",
#     "n/a",
#     "n/a"]]

# First find the proper list

element = "H"
element_print = element+" Property"

red_color = '\033[31m'
reset_color = '\033[0m'

def print_left_right_aligned(left_value, right_value, colored=False):
    left_width = 40  # Adjust as needed
    right_width = 40
    if colored == True:
        print(f'{red_color}{left_value:<{left_width}}{right_value:>{right_width}}{reset_color}')
    else:
                print(f'{left_value:<{left_width}}{right_value:>{right_width}}')


print("\n")
print(f"!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! {red_color}{element_print}{reset_color} !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

# print("!"*80)
for item in property_lst:
    if element in item:
        for i, j in zip(table, item):
            if "Pauling Negativity Number" in i:
                print_left_right_aligned(i, j, colored=True)
            elif "Atomic Weight (u.m)" in i:
                print_left_right_aligned(i, j, colored=True)
            else:
                print_left_right_aligned(i, j, colored=False)

print("/"*80)


