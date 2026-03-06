good = r"""
     _               _               
    | |             | |              
 ___| |__   __ _  __| | _____      __
/ __| '_ \ / _` |/ _` |/ _ \ \ /\ / /
\__ \ | | | (_| | (_| | (_) \ V  V / 
|___/_| |_|\__,_|\__,_|\___/ \_/\_/ 
"""
bad = r"""
                                                           
88                              88                         
88                              88                         
88                              88                         
88,dPPYba,  ,adPPYYba,  ,adPPYb,88  ,adPPYb,d8  ,adPPYba,  
88P'    "8a ""     `Y8 a8"    `Y88 a8"    `Y88 a8P_____88  
88       d8 ,adPPPPP88 8b       88 8b       88 8PP"""""""  
88b,   ,a8" 88,    ,88 "8a,   ,d88 "8a,   ,d88 "8b,   ,aa  
8Y"Ybbd8"'  `"8bbdP"Y8  `"8bbdP"Y8  `"YbbdP"Y8  `"Ybbd8"'  
                                    aa,    ,88             
                                     "Y8bbdP"   
"""
guard_awake = True
if guard_awake:
    outcome = "Doom: OH NO RUN!"
else:
    outcome = "Shadow: Be quiet, we woke up the guard."

print(outcome)
