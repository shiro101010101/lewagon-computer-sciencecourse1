"""
pylint: disable=missing-docstringq
"""

import sys

def full_name(first_name, last_name):
    """returns the full name"""

    if first_name=="" or last_name=="":
        name = f"{first_name.capitalize().strip()}{last_name.capitalize().strip()}"
    else:
        name = f"{first_name.capitalize().strip()} {last_name.capitalize().strip()}"
    return name

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("You must provide a first name and a last name as arguments!")
    else:
        print(f"Hello {full_name(sys.argv[1], sys.argv[2])}")

full_name("george", "harrison")
