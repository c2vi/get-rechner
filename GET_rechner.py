import pyautogui
import numpy as np
from math import * 

def round_complex(x):
    return complex(round(x.real,4),round(x.imag,4))


def convert(complex_):
   r = sqrt((complex_.imag)**2 + (complex_.real)**2)

   phi_rad = np.angle(complex_)
   phi = (phi_rad*180)/pi

   polar = [r,phi]
   return polar

def omega(f_loc):
   return (2*pi*f_loc)

while True:
   if pyautogui.locateOnScreen("C:\\Users\\holas\\OneDrive - HTL Anichstrasse (1)\\Privat\\Backup\\Python\\GET\\Beispiele\\beispiel_1.png",confidence = 0.9) != None:
  
      Ue = float(input("Ue="))
      r1 = float(input("R1="))
      c1 = float(input("C1="))
      r2 = float(input("R2="))
      f = float(input("f="))

      
      Xc = 1/(omega(f)*1j*c1)
      Zcr = 1/((1/Xc) + (1/r2))
      Z = Zcr + r1
      print("Z=",round_complex(Z))


   elif pyautogui.locateOnScreen("C:\\Users\\holas\\OneDrive - HTL Anichstrasse (1)\\Privat\\Backup\\Python\\GET\\Beispiele\\beispiel_2.png",confidence = 0.9) != None:
      Ue = float(input("Ue="))
      r1 = float(input("R1="))
      c1 = float(input("C1="))     
      f = float(input("f="))

      Xc = 1/(omega(f)*1j*c1)
      Z = 1/((1/Xc) + (1/r1))
      print("Z=",round_complex(Z))


   elif pyautogui.locateOnScreen("C:\\Users\\holas\\OneDrive - HTL Anichstrasse (1)\\Privat\\Backup\\Python\\GET\\Beispiele\\beispiel_3.png",confidence = 0.9) != None:
      Ue = float(input("Ue="))
      r1 = float(input("R1="))
      l1 = float(input("L1="))
      c1 = float(input("C1="))     
      f = float(input("f="))

      Xc = 1/(omega(f)*1j*c1)
      Xl = omega(f)*1j*l1
      Rzr = Xl+r1
      Z = 1/((1/Xc) + (1/Rzr))
      Z_polar = convert(Z)
      print("Z= " + str(Z_polar[0]) + " Ohm   " + str(Z_polar[1]) + "°")

      Ic1 = (Z/Xc) * (Ue/Z)
      Ic1_polar = convert(Ic1)
      print("Ic1= " + str(Ic1_polar[0]) + " A   " + str(Ic1_polar[1]) + "°")

      Ur1 = (r1/Rzr)*Ue
      Ur1_polar = convert(Ur1)
      print("Ur1= " + str(Ur1_polar[0]) + " V   " + str(Ur1_polar[1]) + "°")

      Ul1 = (Xl/Rzr)*Ue
      Ul1_polar = convert(Ul1)
      print("Ul1= " + str(Ul1_polar[0]) + " V   " + str(Ul1_polar[1]) + "°")	

      Uc1 = Ue
      Uc1_polar = convert(Uc1)
      print("Uc1= " + str(Uc1_polar[0]) + " V   " + str(Uc1_polar[1]) + "°")     


   elif pyautogui.locateOnScreen("C:\\Users\\holas\\OneDrive - HTL Anichstrasse (1)\\Privat\\Backup\\Python\\GET\\Beispiele\\beispiel_4.png",confidence = 0.9) != None:
      Ue = float(input("Ue="))
      r1 = float(input("R1="))
      c1 = float(input("C1="))
      l1 = float(input("L1=")) 
      r2 = float(input("R2="))   
      f = float(input("f="))

      Xc = 1/(omega(f)*1j*c1)
      Xl = omega(f)*1j*l1
      Xrc = 1/((1/Xc) + (1/r1))
      Xrl = 1/((1/Xl) + (1/r2))
      Z = Xrc + Xrl
      print("Z=" , round_complex(Z))


   elif pyautogui.locateOnScreen("C:\\Users\\holas\\OneDrive - HTL Anichstrasse (1)\\Privat\\Backup\\Python\\GET\\Beispiele\\beispiel_5.png",confidence = 0.9) != None:
      Ue = float(input("Ue="))
      r1 = float(input("R1="))
      l1 = float(input("L1="))
      c1 = float(input("C1="))
      r2 = float(input("R2="))   
      f = float(input("f="))     

      Xc = 1/(omega(f)*1j*c1)
      Xl = omega(f)*1j*l1
      Xrc = 1/((1/Xc) + (1/r2))
      Xrl = 1/((1/Xl) + (1/r1))
      Z = Xrc + Xrl
      print("Z=" , round_complex(Z))


   elif pyautogui.locateOnScreen("C:\\Users\\holas\\OneDrive - HTL Anichstrasse (1)\\Privat\\Backup\\Python\\GET\\Beispiele\\beispiel_6.png",confidence = 0.9) != None:
      UWq1 = float(input("Ue="))
      r1 = float(input("R1="))
      l1 = float(input("L1="))
      c1 = float(input("C1="))  
      f = float(input("f=")) 

      Xc = 1/(omega(f)*1j*c1)  
      Xl = omega(f)*1j*l1
      Xcl = 1/((1/Xc) + (1/Xl))
      Z = Xcl + r1
      Z_polar = convert(Z)
      print("Z= " + str(Z_polar[0]) + " Ohm   " + str(Z_polar[1]) + "°")
      
      Ic1 = (Xcl/Xc) * (UWq1/Z)
      Ic1_polar = convert(Ic1)
      print("Ic1= " + str(Ic1_polar[0]) + " A   " + str(Ic1_polar[1]) + "°")

      Ur1 = (UWq1/Z) * r1
      Ur1_polar = convert(Ur1)
      print("Ur1= " + str(Ur1_polar[0]) + " V   " + str(Ur1_polar[1]) + "°")     

      Ucl1 = (UWq1/Z) * Xcl
      Ucl1_polar = convert(Ucl1)
      print("Ul1= " + str(Ucl1_polar[0]) + " V   " + str(Ucl1_polar[1]) + "°")
      print("Uc1= " + str(Ucl1_polar[0]) + " V   " + str(Ucl1_polar[1]) + "°")


   elif pyautogui.locateOnScreen("C:\\Users\\holas\\OneDrive - HTL Anichstrasse (1)\\Privat\\Backup\\Python\\GET\\Beispiele\\beispiel_7.png",confidence = 0.9) != None:
      Uq1 = float(input("Ue="))
      r1 = float(input("R1="))
      l1 = float(input("L1="))
      c1 = float(input("C1="))  
      f = float(input("f="))

      Xc = 1/(omega(f)*1j*c1)  
      Xl = omega(f)*1j*l1
      Xrl = 1/((1/Xl) + (1/r1))
      Z = Xrl + Xc
      Z_polar = convert(Z)
      print("Z= " + str(Z_polar[0]) + " Ohm   " + str(Z_polar[1]) + "°")      

      Ic1 = Uq1/Z
      Ic1_polar = convert(Ic1)
      print("Ic1= " + str(Ic1_polar[0]) + " A   " + str(Ic1_polar[1]) + "°")   

      Ur1 = (Xrl/Z) * Uq1
      Ur1_polar = convert(Ur1)
      print("Ur1= " + str(Ur1_polar[0]) + " V   " + str(Ur1_polar[1]) + "°")    
      print("Ul1= " + str(Ur1_polar[0]) + " V   " + str(Ur1_polar[1]) + "°") 

      Uc1 = (Xc/Z) * Uq1
      Uc1_polar = convert(Uc1)
      print("Uc1= " + str(Uc1_polar[0]) + " V   " + str(Uc1_polar[1]) + "°")


   else:
      print("not found")



      ["Ue = 12.3V", "R1 = 1.8kOhm" ]