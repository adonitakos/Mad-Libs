class Day_At_Zoo():

  @staticmethod
  def game():
    adjective1 = input("Adjective: ")
    noun1 = input("Noun: ")
    pastVerb1 = input("Verb (past tense): ")
    adverb1 = input("Adverb: ")
    adjective2 = input("Adjective: ")
    noun2 = input("Noun: ")
    noun3 = input("Noun: ")
    adjective3 = input("Adjective: ")
    verb = input("Verb: ")
    adverb2 = input("Adverb: ")
    pastVerb2 = input("Verb (past tense): ")
    adjective4 = input("Adjective: ")

    Zoo_FILE = open("DayAtZoo.txt","r")
    zoo_day = Zoo_FILE.read()
    Zoo_FILE.close()

    output = zoo_day.format(adjective1, pastVerb1, pastVerb1, adverb1, adjective2, noun2, noun3, adjective3, verb, adverb2, pastVerb2, adjective4)

    print("\n" + output)

