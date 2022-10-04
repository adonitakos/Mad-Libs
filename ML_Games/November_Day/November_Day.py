class November_Day:

  @staticmethod
  def game():
    adjective1 = input("Adjective: ")
    adjective2 = input("Adjective: ")
    type_of_bird = input("Type of Bird: ")
    house_room = input("Room in the house: ")
    pastVerb = input("Verb (past tense): ")
    verb1 = input("Verb: ")
    relative_name = input("Name of relative: ")
    noun1 = input("Noun: ")
    liquid = input("Type of liquid: ")
    ing_verb1 = input("Verb ending in ing: ")
    body_parts = input("Part of the body (plural): ")
    plural_noun = input("Plural noun: ")
    ing_verb2 = input("Verb ending in ing: ")
    noun2 = input("Noun: ")

    with open("/home/runner/Python-Test/ML_Games/November_Day/November_Day.txt", "r") as file:
      print(file.read().format(adjective1, adjective2, type_of_bird, house_room, pastVerb, verb1, relative_name, noun1, liquid,       ing_verb1, body_parts, plural_noun, ing_verb2, noun2))

  # <--- game() function ends here

# <--- November_Day class ends here