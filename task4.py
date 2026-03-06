good = r"""
  ,d                                                              
  88                                                              
MM88MMM ,adPPYba,  88       88  ,adPPYba, ,adPPYYba, 8b,dPPYba,   
  88   a8"     "8a 88       88 a8"     "" ""     `Y8 88P'   `"8a  
  88   8b       d8 88       88 8b         ,adPPPPP88 88       88  
  88,  "8a,   ,a8" "8a,   ,a88 "8a,   ,aa 88,    ,88 88       88  
  "Y888 `"YbbdP"'   `"YbbdP'Y8  `"Ybbd8"' `"8bbdP"Y8 88       88  
"""
bad = r"""
     ^^      .-=-=-=-.  ^^
 ^^        (`-=-=-=-=-`)         ^^
         (`-=-=-=-=-=-=-`)  ^^         ^^
   ^^   (`-=-=-=-=-=-=-=-`)   ^^                            ^^
       ( `-=-=-=-(@)-=-=-` )      ^^
       (`-=-=-=-=-=-=-=-=-`)  ^^
       (`-=-=-=-=-=-=-=-=-`)              ^^
       (`-=-=-=-=-=-=-=-=-`)                      ^^
       (`-=-=-=-=-=-=-=-=-`)  ^^
        (`-=-=-=-=-=-=-=-`)          ^^
         (`-=-=-=-=-=-=-`)  ^^                 ^^
     jgs   (`-=-=-=-=-`)
            `-=-=-=-=-`
"""
drawbridge_raised = False
if not drawbridge_raised:
    outcome = "Thunder: We need to cross now!!"
    print(good)
else:
    outcome = "Doom: We've been caught, RUNNNNN!!!"
    print(bad)

print(outcome)

