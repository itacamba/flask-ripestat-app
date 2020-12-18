import re



def validate(obj):
    inetnum_pattern = "^([01]?\d\d?|2[0-4]\d|25[0-5])(?:\.[01]?\d\d?|\.2[0-4]\d|\.25[0-5]){3}(?:\/[0-2]\d|\/3[0-2]|\/[8-9])?$"
    organisation_pattern = "ORG-([a-zA-Z]+){2,4}\d+-RIPE"

    if re.search(inetnum_pattern, obj):
        return "inetnum"
    elif re.search(organisation_pattern, obj): 
        return "organisation"