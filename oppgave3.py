# Egner seg for: 1. og 2. klasse

# Med kode, print ut følgende tallmønster i konsollen ved å bruke løkker. Se bort fra fnuttene over og under tallene.
# Se følgende ressurs for å lære mer om løkker i Python (https://www.dataquest.io/blog/python-for-loop-tutorial/)

"""
 1 2 3 4 5 6 7 8 9 
  2 3 4 5 6 7 8 9 
   3 4 5 6 7 8 9 
    4 5 6 7 8 9 
     5 6 7 8 9 
      6 7 8 9 
     5 6 7 8 9 
    4 5 6 7 8 9 
   3 4 5 6 7 8 9 
  2 3 4 5 6 7 8 9 
 1 2 3 4 5 6 7 8 9 
"""

# Du kan bruke følgende kode som start-punkt eller begynne fra scratch:
for i in range(11):
    for j in range(10):
            # Forklaring: end=" " sier at det skal legges til et mellomrom på slutten av det som printes ut
            # Hvis man ikke definerer end-verdien så vil det som standard legges til en ny linje i terminalen etter teksten.
            print(f"{j}", end=" ")
    print() # brukes for å starte på en ny linje