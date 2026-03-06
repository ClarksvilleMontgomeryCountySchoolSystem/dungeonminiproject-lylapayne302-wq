bad = r"""
                        888                      
                        888                      
                        888                      
 8888b. 88888b. 888  888888  888 .d88b. 888  888 
    "88b888 "88b888  888888 .88Pd8P  Y8b888  888 
.d888888888  888888  888888888K 88888888888  888 
888  888888  888Y88b 888888 "88bY8b.    Y88b 888 
"Y888888888  888 "Y88888888  888 "Y8888  "Y88888 
                     888                     888 
                Y8b d88P                Y8b d88P 
                 "Y88P"                  "Y88P" 
"""
good = r"""

                                   88                               
                                   88                               
                                   88                               
,adPPYYba, 8b,dPPYba,  8b       d8 88   ,d8  ,adPPYba, 8b       d8  
""     `Y8 88P'   `"8a `8b     d8' 88 ,a8"  a8P_____88 `8b     d8'  
,adPPPPP88 88       88  `8b   d8'  8888[    8PP"""""""  `8b   d8'   
88,    ,88 88       88   `8b,d8'   88`"Yba, "8b,   ,aa   `8b,d8'    
`"8bbdP"Y8 88       88     Y88'    88   `Y8a `"Ybbd8"'     Y88'     
                           d8'                             d8'      
                          d8'                             d8'    
"""
has_key = False
if not has_key:
    outcome = "Doom: We have failed our mission."
else:
    outcome = "Click: Come on we have to keep looking."

print(outcome)
