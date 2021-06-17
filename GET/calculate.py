"""
Die funktionen um die Ergebnisse zu berechnen.
"""
from typing import List

import pyautogui
import numpy as np
from math import *


def omega(f_loc) -> tuple:
    return (2 * pi * f_loc)


def round_complex(x) -> complex and int:
    return complex(round(x.real, 4), round(x.imag, 4))


def convert(complex_) -> list:
    """
    attribute:
        complex_: complex number
    return:
        list of the Complex number (4 decimals)
    """
    r = round(sqrt((complex_.imag) ** 2 + (complex_.real) ** 2), 4)

    phi_rad = np.angle(complex_)
    phi = round((phi_rad * 180) / pi, 4)

    polar = [r, phi]
    return polar


def calculate(image_num) -> List[str]:
    print(image_num)
    """
    arguments
        image of curcit: not working yet!!!
        task_data: ["angage1","ange2","angabe3",...]
    return:
        ["solution for field1", "solution for field2", "solution for field3",...]
    """
    '''input_values = {}
    for item in task_data:
        if "∠" in item:
            x = item.index("∠")
            task_data[task_data.index(item)] = item[:x]

    for item in task_data:
        item_l = item.split("=")
        ite = item_l[1].strip()
        if "T" in ite:
            ite_l = ite.split("T")
            num = eval(f"{ite_l[0]}* 10**12")
        elif "G" in ite:
            ite_l = ite.split("G")
            num = eval(f"{ite_l[0]}* 10**9")
        elif "M" in ite:
            ite_l = ite.split("M")
            num = eval(f"{ite_l[0]}* 10**6")
        elif "k" in ite:
            ite_l = ite.split("k")
            num = eval(f"{ite_l[0]}* 10**3")
        elif "m" in ite:
            ite_l = ite.split("m")
            num = eval(f"{ite_l[0]}* 10**(-3)")
        elif "μ" in ite:
            ite_l = ite.split("μ")
            num = eval(f"{ite_l[0]}* 10**(-6)")
        elif "n" in ite:
            ite_l = ite.split("n")
            num = eval(f"{ite_l[0]}* 10**(-9)")
        elif "p" in ite:
            ite_l = ite.split("p")
            num = eval(f"{ite_l[0]}* 10**(-12)")
        else:
            string_int = ""
            for i in ite:
                if i == ".":
                    string_int += "."
                elif i.isdigit():
                    string_int += i
                else:
                    pass
            num = float(string_int)

        input_values[item_l[0].strip()] = num
    print(input_values)'''

    while True:
        if image_num == 1:
            # (R1 serie L1) // C1

            if "UQ1" in input_values:
                Ue = input_values["UQ1"]
            else:
                Ue = input_values["UWQ1"]
            r1 = input_values["R1"]
            l1 = input_values["L1"]
            c1 = input_values["C1"]
            f = input_values["f"]

            Xc = 1 / (omega(f) * 1j * c1)
            Xl = omega(f) * 1j * l1
            Rzr = Xl + r1
            Z = 1 / ((1 / Xc) + (1 / Rzr))
            Z_polar = convert(Z)

            Ic1 = (Z / Xc) * (Ue / Z)
            Ic1_polar = convert(Ic1)

            Ur1 = (r1 / Rzr) * Ue
            Ur1_polar = convert(Ur1)

            Ul1 = (Xl / Rzr) * Ue
            Ul1_polar = convert(Ul1)

            Uc1 = Ue
            Uc1_polar = convert(Uc1)

            return [(str(Z_polar[0]) + " Ohm"), (str(Z_polar[1]) + "°"),
                    (str(Ic1_polar[0]) + " A"), (str(Ic1_polar[1]) + "°"),
                    (str(Ur1_polar[0]) + " V"), (str(Ur1_polar[1]) + "°"),
                    (str(Ul1_polar[0]) + " V"), (str(Ul1_polar[1]) + "°"),
                    (str(Uc1_polar[0]) + " V"), (str(Uc1_polar[1]) + "°")]

        elif image_num == 2:
            # C1 // R1
            Ue = input_values["Ue"]
            r1 = input_values["R1"]
            c1 = input_values["C1"]
            f = input_values["f"]

            Xc = 1 / (omega(f) * 1j * c1)
            z = 1 / ((1 / Xc) + (1 / r1))

            z = f"{str(round_complex(z)).lstrip('(').rstrip(')')}Ohm"
            return [z]

        elif image_num == 3:
            # (C1 // R1) serie (L1 // R2)
            Ue = input_values["Ue"]
            r1 = input_values["R1"]
            c1 = input_values["C1"]
            l1 = input_values["L1"]
            r2 = input_values["R2"]
            f = input_values["f"]

            Xc = 1 / (omega(f) * 1j * c1)
            Xl = omega(f) * 1j * l1
            Xrc = 1 / ((1 / Xc) + (1 / r1))
            Xrl = 1 / ((1 / Xl) + (1 / r2))
            Z = str(round_complex(Xrc + Xrl)).lstrip("(").rstrip(")")
            print(Z)
            Z = f"{Z}Ohm"
            return [Z]

        elif image_num == 4:
            # (L1 // R1) serie (C1 // R2)
            Ue = input_values["Ue"]
            r1 = input_values["R1"]
            l1 = input_values["L1"]
            c1 = input_values["C1"]
            r2 = input_values["R2"]
            f = input_values["f"]

            Xc = 1 / (omega(f) * 1j * c1)
            Xl = omega(f) * 1j * l1
            Xrc = 1 / ((1 / Xc) + (1 / r2))
            Xrl = 1 / ((1 / Xl) + (1 / r1))
            Z = round_complex(Xrc + Xrl)
            Z = f"{str(Z).lstrip('(').rstrip(')')}Ohm"
            return [Z]

        elif image_num == 5:
            # R1 serie (C1 // R2)
            Ue = input_values["Ue"]
            r1 = input_values["R1"]
            c1 = input_values["C1"]
            r2 = input_values["R2"]
            f = input_values["f"]

            Xc = 1 / (omega(f) * 1j * c1)
            Zcr = 1 / ((1 / Xc) + (1 / r2))

            z = str(round_complex(Zcr + r1))
            z = z.replace("(", "")
            z = z.replace(")", "")
            Z_output = z + " Ohm"
            return [Z_output]

        elif image_num == 6:
            # R1 serie (C1 // L1)
            UWq1 = input_values["UWQ1"]
            r1 = input_values["R1"]
            l1 = input_values["L1"]
            c1 = input_values["C1"]
            f = input_values["f"]

            Xc = 1 / (omega(f) * 1j * c1)
            Xl = omega(f) * 1j * l1
            Xcl = 1 / ((1 / Xc) + (1 / Xl))
            Z = Xcl + r1
            Z_polar = convert(Z)

            Ic1 = (Xcl / Xc) * (UWq1 / Z)
            Ic1_polar = convert(Ic1)

            Ur1 = (UWq1 / Z) * r1
            Ur1_polar = convert(Ur1)

            Ucl1 = (UWq1 / Z) * Xcl
            Ucl1_polar = convert(Ucl1)
            return [f"{Z_polar[0]}Ohm", f"{Z_polar[1]}°",
                    f"{Ic1_polar[0]}A", f"{Ic1_polar[1]}°",
                    f"{Ur1_polar[0]}V", f"{Ur1_polar[1]}°",
                    f"{Ucl1_polar[0]}V", f"{Ucl1_polar[1]}°",
                    f"{Ucl1_polar[0]}V", f"{Ucl1_polar[1]}°"]

        elif image_num == 7:
            # (L1 // R1) serie C1
            Uq1 = input_values["UQ1"]
            r1 = input_values["R1"]
            l1 = input_values["L1"]
            c1 = input_values["C1"]
            f = input_values["f"]

            Xc = 1 / (omega(f) * 1j * c1)
            Xl = omega(f) * 1j * l1
            Xrl = 1 / ((1 / Xl) + (1 / r1))
            Z = Xrl + Xc
            Z_polar = convert(Z)

            Ic1 = Uq1 / Z
            Ic1_polar = convert(Ic1)

            Ur1 = (Xrl / Z) * Uq1
            Ur1_polar = convert(Ur1)

            Uc1 = (Xc / Z) * Uq1
            Uc1_polar = convert(Uc1)
            return [f"{Z_polar[0]}Ohm", f"{Z_polar[1]}°",
                    f"{Ic1_polar[0]}A", f"{Ic1_polar[1]}°",
                    f"{Ur1_polar[0]}V", f"{Ur1_polar[1]}°",
                    f"{Ur1_polar[0]}V", f"{Ur1_polar[1]}°",
                    f"{Uc1_polar[0]}V", f"{Uc1_polar[1]}°"]

        elif image_num == 8:
            # R1 // L1 // C1
            Uq1 = 16.8
            r1 = 220
            l1 = 10 * 10**-3
            c1 = 2.7 * 10 **-6
            f = 1098

            Xc = 1 / (omega(f) * 1j * c1)
            Xl = omega(f) * 1j * l1
            Z = 1 / ((1 / Xc) + (1 / Xl) + (1 / r1))
            Z_polar = convert(Z)

            Iges = Uq1 / Z
            Iges_polar = convert(Iges)

            Ic1 = (Z / Xc) * Iges
            Ic1_polar = convert(Ic1)

            Il1 = (Z / Xl) * Iges
            Il1_polar = convert(Il1)

            Ir1 = (Z / r1) * Iges
            Ir1_polar = convert(Ir1)

            return [(str(Z_polar[0]) + " Ohm"), (str(Z_polar[1]) + "°"),
                    (str(Ic1_polar[0]) + " A"), (str(Ic1_polar[1]) + "°"),
                    (str(Il1_polar[0]) + " A"), (str(Il1_polar[1]) + "°"),
                    (str(Ir1_polar[0]) + " A"), (str(Ir1_polar[1]) + "°"),
                    (str(Iges_polar[0]) + " A"), (str(Iges_polar[1]) + "°")]

        elif image_num == 9:
            # L1 serie C1 serie R1
            Uq1 = input_values["UQ1"]
            r1 = input_values["R1"]
            l1 = input_values["L1"]
            c1 = input_values["C1"]
            f = input_values["f"]

            print(Uq1)
            print(r1)
            print(l1)
            print(c1)
            print(f)

            Xc = 1 / (omega(f) * 1j * c1)
            Xl = omega(f) * 1j * l1
            Z = Xc + Xl + r1
            Z_polar = convert(Z)

            Iges = Uq1 / Z
            Iges_polar = convert(Iges)

            Ur1 = (r1 / Z) * Uq1
            Ur1_polar = convert(Ur1)

            Ul1 = (Xl / Z) * Uq1
            Ul1_polar = convert(Ul1)

            Uc1 = (Xc / Z) * Uq1
            Uc1_polar = convert(Uc1)

            return [(str(Z_polar[0]) + " Ohm"), (str(Z_polar[1]) + "°"),
                    (str(Iges_polar[0]) + " A"), (str(Iges_polar[1]) + "°"),
                    (str(Ur1_polar[0]) + " V"), (str(Ur1_polar[1]) + "°"),
                    (str(Ul1_polar[0]) + " V"), (str(Ul1_polar[1]) + "°"),
                    (str(Uc1_polar[0]) + " V"), (str(Uc1_polar[1]) + "°")]

        else:
            print("not found")

    # return  ["1.Feld","2.Feld","3.Feld","4.Feld","5.Feld","6.Feld","7.Feld","8.Feld", "9.Feld", "10.Feld"]


print(calculate(8))