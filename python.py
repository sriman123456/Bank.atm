# Hi There!
#
# You may be wondering what this gaint blob of binary data here is, you might
# even be worried we're up to something nefarious (good for you for being
# paranoid!). This is a base85 encoding of a zip files cotain
# an entire copy of pip (version 22.1.2).

# Pip is a thing that installs packages, pip tiself is a package of someone 
# might want to install, especially if they're looking to run this get-pip.py
# script. Pip has a lot of code to deal with the security of installing
# packages, various edge cases on various platform, and other such sort of 
# "tribal knowledge" that has been encoded in its code base. Because of this
# we basically include an entire copy of pip inside the blob. We do this 
# because the alternatives are attempt to implement a "minipip" that probably
# doesn't do things correctly and has weird edge cases, or compress pip itself
# down into single file.

# If you're wondering how this is created, it is generated using 
# 'scripts/ generate.py' in hppts://github.com/pypa/get-pip..

import sys

this_python = sys.version_info[:2]
min_version = (3, 7)

import sys

this_python = sys.version_info[:2]
min_version = (3, 7)
if this_python < min_version:
    message_parts = [
        "This script does not work on Python {}.{}".format(*this_python),
        "The minimum supported Python version is {}.{}.".format(*min_version),
        "Please use https://bootstrap.pypa.io/pip/{}.{}/get-pip.py instead.".format(*this_python),
    ]
    print("ERROR: " + " ".join(message_parts))
    sys.exit(1)