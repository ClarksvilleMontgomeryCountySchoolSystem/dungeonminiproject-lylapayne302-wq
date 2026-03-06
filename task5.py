good = r"""
              ________
             / ______ \
             || _  _ ||
             ||| || |||
             |||_||_|||
             || _  _o|| (o)
             ||| || |||
             |||_||_|||      ^~^  ,
             ||______||     ('Y') )
            /__________\    /   \/
    ________|__________|__ (\|||/) _________
   hjw     /____________\
   `97     |____________|
"""
bad = r"""
                       ______
                    .-"      "-.
                   /            \
       _          |              |          _
      ( \         |,  .-.  .-.  ,|         / )
       > "=._     | )(__/  \__)( |     _.=" <
      (_/"=._"=._ |/     /\     \| _.="_.="\_)
             "=._ (_     ^^     _)"_.="
                 "=\__|IIIIII|__/="
                _.="| \IIIIII/ |"=._
      _     _.="_.="\          /"=._"=._     _
     ( \_.="_.="     `--------`     "=._"=._/ )
      > _.="                            "=._ <
     (_/   jgs                              \_)
"""
escaped = True
if escaped:
    outcome = "Legend: You have escaped."
    print(good)
else:
    outcome = "Doom: You have not escaped, try again next time or will there be a next time?"
    print(bad)

print(outcome)
