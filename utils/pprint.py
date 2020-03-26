VERBOSITY = 0


def pprint(verbosity, *args):
    if verbosity <= VERBOSITY:
        for arg in args:
            print(arg, end=" ")
        print()
