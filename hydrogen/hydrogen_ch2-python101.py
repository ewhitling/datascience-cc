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
my_number = 5.0
my_string = "octopus"
my_boolean = False

# %% codecell
# data structures
# list
my_list = ["octopus", "squid", "cuttlefish"]
my_list[0]
my_list

# tuple

# set


# dictionary
my_dict = dict()
my_dict[''] = 1
my_dict[''] = 2

# dataframes

# %% codecell
# conditionals to control a logical flow of work
if my_boolean:
	print("It was true!")
else:
	print("False!")

if my_boolean == True:
	print("This is the same as just using 'if my_boolean:'")

print("Does the string equal the boolean? %s" % (my_string == my_boolean))

# %% codecell
# loops

# %% codecell
# asserts
assert  my_boolean==False, "Asserts check assumptions."

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
is_it_an_octopus(4, "cat")
is_it_an_octopus(9, "Gorgon!")

# %% codecell
# recursive functions
def walk_directory(path):
	contents = os.listdir(path)

	for item in contents:
		new_path = os.path.join(path, item)

		if os.path.isdir(new_path):
			walk_directory(new_path)
		elif os.path.isfile(new_path):
			print("We found a file: %s" % new_path)
		else:
			print("What the heck is this! %s " % new_path)

walk_directory("./")




# %% codecell
# list comprehensions and generators
