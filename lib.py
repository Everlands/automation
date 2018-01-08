##########################################################################
# Everlands Library of Useful Functions
# Started November 2017
#
# Python 3.5
##########################################################################



##########################################################################
# Check out a string and return True if that string contains just a number
##########################################################################


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
 
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
 
    return False    



