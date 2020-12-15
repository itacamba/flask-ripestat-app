import re

inetnum_pattern = "^([01]?\d\d?|2[0-4]\d|25[0-5])(?:\.[01]?\d\d?|\.2[0-4]\d|\.25[0-5]){3}(?:\/[0-2]\d|\/3[0-2]|\/[8-9])?$"
organisation_pattern = "ORG-([a-zA-Z]+){2,4}\d+-RIPE"
user_input = input()
if re.search(inetnum_pattern, user_input):
    print("this is an Inetnum object")
elif re.search(organisation_pattern, user_input): 
    print("this is an organisation object")
# def find_object_type('185.83.159.255'):
#     if()