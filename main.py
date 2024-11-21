"""c'est une fnction palindrome  """
def ispalindrome(p):
    """ fonction qui verif si c'est un palindrome"""
    accent     = "éèêëàâäîïôöùûüç-.:?!,';_"
    sansaccent = "eeeeaaaiioouuuc         "
    p = p.lower()
    p = p.translate(str.maketrans(accent , sansaccent)).replace(" ","")
    return p == p[::-1]


#### Fonction principale


def main():
    """ fonction main"""
# vos appels à la fonction secondaire ici

    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))


if __name__ == "__main__":
    main()
