'''
5. Hide the social security number
Write a function in Python that accepts a social. It should return a string where all the characters are hidden with an asterisk except the last four. 
For example, if the function gets sent "123-45-6789", then it should return "XXX-XX-6789".
Acceptance Criteria:
a) only accept valid social security format: ie 123-45-6789 not 123-45-456897 or 123546789
    - function should ERROR and not return
b) return should be string to be used in futher computation -> str('XXX-XX-6789')
'''

def social_encryption(social):
    encrypted_social = 'ERROR'
    # social.find(char='-', 2)
        # Search for -
    if '-' in social: 

        # split on -
        split_social = social.split(sep='-')

        # If social-split is 3 items
        if len(split_social) == 3:
            first = split_social[0]
            second = split_social[1]
            third = split_social[2]
            # if socials are isdigit():
            if first.isdigit() and second.isdigit() and third.isdigit():
                if len(split_social[0]) == 3 and len(split_social[1]) == 2 and len(split_social[2]) == 4:
                                    # print the fucker                                     
                    encrypted_social = 'XXX-XX-'  + split_social[-1]
    # social = parameter
    return str(encrypted_social)


# social = social_encryption('123-45-6789')
# print(social)
# # XXX-XX-6789

# social5 = social_encryption('ABC-15-JDK1')
# print(social5)
# # XXX-XX-JDK1
# # Test Cases:

# social2 = social_encryption('123456789')
# print(social2)
# # XX-XX-6789
# social3 = social_encryption('123-45-678910')
# print(social3)
# # XXX-XX-8910
# social4 = social_encryption('987-65-4321')
# print(social4)
# # XXX-XX-4321

# social6 = social_encryption('987-65-4321-120')
# print(social6)
# # XXX-XX-4321

enter_my_social = input('Enter your social yo:')
my_social = social_encryption(enter_my_social)
print(my_social)