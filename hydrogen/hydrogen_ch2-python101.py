# %% codecell
# basic math
1+1
4*4


# %% codecell
# printing things
print("Hello, data!")

# %% codecell
# open some libraries
import os
os.listdir()

# %% codecell
# data types

# %% codecell
# conditionals

# %% codecell
# loops

# %% codecell
# asserts

# %% codecell
# create a function
def is_it_an_octopus(limbs, thing):

    assert type(limbs) == int, "Limbs must be an integer."
    assert type(thing) == str, "Your thing must be a string."

    if limbs == 8:
        print("This %s probably an octopus. Run away!" % thing)
    elif limbs >= 7 and limbs <= 9:
        print("This %s is a mutant octopus. Tread carefully..." % thing)
    else:
        print("This octopus is well disguised as a %s!" % thing)

is_it_an_octopus(8, "dog")
