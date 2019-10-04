import re
regex = '\S+@\S+.\S+'

def check(email):
    # pass the regualar expression
    # and the string in search() method
    if (re.search(regex, email)):
        print("Valid Email")

    else:
        print("Invalid Email")

    # Driver Code


if __name__ == '__main__':
    # Enter the email
    email = "ankitrai326@gmail.com"

    # calling run function
    check(email)

    email = "my.ownsite@ourearth.org"
    check(email)

    email = "ankitrai326@.com"
    check(email)