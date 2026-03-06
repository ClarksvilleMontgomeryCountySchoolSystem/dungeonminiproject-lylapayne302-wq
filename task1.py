Good = r"""
..
\\ //.'' -..-.
\ \ / /.'     ' -.-'   '.
~__\(    ) / __
~            '.    ..~
(. \!! /.). - '' -.'..~~~~
\ | (--) - -- | / '-..-'
BP
'-..-~'
^ ^ ^ '' ^ ^ ^
"""
Bad = r"""

                          .
                          /  , /
                        ,/' /`'
                       /(/`'   _
                      f'/)  ,-'
                     /    ,' itz
                    f,/  /
                    /"  7
                   / ,f /
              )   / / |J
                 7,( ;|j
      ,       (. "`/ ('
          `    )`-'/ l `
    (  (    ) '   ' (_,'  )
 (     ,)  7`  /  /,  (, (
  ,  ) (,- `-'  /  (,   -') (
 (_ ( `-_(,_,'_(_(__ )_, _`-_, _
"""
torch_lit = True
if torch_lit:
    outcome = "Flicker: Come on let's geto ut of here."
    print(Good)
else:
    outcome = "Doom: What should we do?"
    print(Bad)

print(outcome)
