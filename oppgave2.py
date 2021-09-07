#
#   Sjekk om personen kan ta lappen!
#
#   I denne oppgaven skal du sjekke om en person
#   er gammel nok til å ta sertifikatet for bil i landet sitt.
#
#   Funksjonen under skal ta inn to parametre: alder og land.
#
#   Om personen er fra Norge, må hen være 18 år eller eldre for å ta lappen.
#   Om personen er fra USA, mer aldersgrensen 16 år.
#
#   Dette betyr at
#
#       check_legal_driving_age(17, "Norway")
#
#   skal returnere noe sånt som
#
#       "The person is not old enough to drive ⛔",
#
#   og at

#       check_legal_driving_age(17, "USA")
#
#   skal returnere noe sånt som
#
#       "The person is old enough to drive 🚗"
#
#
#   Bruk kodeskjelettet under til å fullføre funksjonen!
#

def check_legal_driving_age(age: int, country: str):

    print("")
    # LF:
    # can_drive = False

    # if country == "Norway":
    #     can_drive = (age >= 18)
    # elif country == "USA":
    #     can_drive = (age >= 16)

    # if can_drive:
    #     print("The person is old enough to drive 🚗")
    # else:
    #     print("The person is not old enough to drive ⛔")


check_legal_driving_age(17, "Norway")
check_legal_driving_age(17, "USA")
