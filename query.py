"""Skills 5: SQLAlchemy & AJAX

This file is used in Part 2 and 3 of Skills 5: SQLAlchemy & AJAX. You need to
complete Part 1 first, otherwise this part of the assessment won't work.

Be sure to read the instructions before you get started.
"""

from model import db, Human, Animal


##############################################################################
# PART 2: QUERIES


def q1():
    """Return the human with the id 2."""
    human = Human.query.filter_by(human_id = 2).first()

    return human


def q2():
    """Return the FIRST animal with the species 'fish'."""

    animal_fish = Animal.query.filter_by(animal_species = 'fish').first()

    return animal_fish 


def q3():
    """Return all animals that were born after 2015.

    Do NOT include animals without birth years.
    """
    animal_2015 = Animal.query.filter(Animal.birth_year > 2015).all()

    return animal_2015


def q4():
    """Return the humans with first names that start with 'J'."""

    fname_j = Human.query.filter(Human.fname.like('%J%')).all()

    return fname_j


def q5():
    """Return all animals whose birth years are NULL in the database."""

    animal_null = Animal.query.filter(Animal.birth_year == None).all()

    return animal_null


def q4():
    """Return all animals whose species is 'fish' OR 'rabbit'."""

    fish_rabbit = Animal.query.filter( (Animal.animal_species == 'rabbit') | (Animal.animal_species == 'fish')).all()

    return fish_rabbit


def q5():
    """Return all humans whose email addresses do NOT contain 'gmail'."""

    not_gmail = Human.query.filter_by(email != contains("gmail")).all()

    return not_gmail


##############################################################################
# PART 3: NAVIGATING RELATIONSHIPS

# **Use SQLAlchemy relationships for each function**

# 1. Write a function, print_directory, which does not take any arguments
#    and prints out each human (once) with a list of their animals.
#
#    The output should look like this (with tabs to indent each animal name under
#    a human's name)
#
#       Human_first_name Human_last_name
#           Animal name (animal species)
#           Animal name (animal species)
#
#       Human_first_name Human_last_name
#           Animal name (animal species)

def print_directory():
    """Print all Humans and their corresponding animal 
        and also the animal specie"""

    humans = Human.query.all()

    for human in humans: 
        for animal in human.animals:
            print(human.fname, human.lname)
            print(animal.name, "(",animal.animal_species,")")



# 2. Write a function, find_humans_by_animal_species, which takes in an animal
#    species and *returns a list* of all of Human objects who have animals of
#    that species.

def find_humans_by_animal_species(species):
    """Replace this with a good docstring."""

    animals = Animal.query.filter_by(animal_species=species).all()

    human_list = []
    for animal in animals: 
        human = animal.human.fname
        human_list.append(human)

    print(human_list)


if __name__ == "__main__":
    from server import app
    from model import connect_to_db

    connect_to_db(app)
    # print_directory()
    # find_humans_by_animal_species(species)

