# mad lib

import random

def gather_madlibs():
    adjective1 = input('enter an adjective: ')
    adjective2 = input('enter an adjective: ')
    name = input('enter a name: ')
    noun1 = input('enter a noun: ')
    noun2 = input('enter a noun: ')
    verb1 = input('enter a verb: ')
    verb2 = input('enter a verb: ')
    madlibs = [adjective1, adjective2, name, noun1, noun2, verb1, verb2]
    return madlibs

def print_madlib(words):
    words_list = words
    adjective1 = words_list[0]
    adjective2 = words_list[1]
    name = words_list[2]
    noun1 = words_list[3]
    noun2 = words_list[4]
    verb1 = words_list[5]
    verb2 = words_list[6]
        
    madlib1 = f"Justin really made me do this {adjective1} thing multiple times so here it is. But he makes me laugh when we {verb1} together. Make sure you check on {name} because he might be sleeping off that smoothie!!!"
    madlib2 = f"Ayo {name}, this is starting to make sense. Python reall makes my head {verb1}! maybe after this we can {adjective2} go get some food? I havent eaten all day dawg lmao."
    madlib3 = f"I tried {adjective1} hard to make 5 of these for Justin, but I got {adjective2} hungry and forgot to come back and finish it LOL. My head is {verb2} trying to cram all of this in as fast as possible."
    madlib4 = f"What the fuck is up mother {verb1 if verb1 == 'fuck' else 'fuck'}er! It's your boy, {name}. I came here in my brand new {noun1} to {verb2} some {adjective1} {noun2}."
    madlib_list = [madlib1, madlib2, madlib3,madlib4]
    print(random.choice(madlib_list))
    # print(madlib4)
    return None

# words = gather_madlibs()
# print_madlib(words)

if __name__ == "__main__":
    words = gather_madlibs()
    print_madlib(words)