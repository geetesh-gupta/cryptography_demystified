VERBOSITY = 0


def pprint(verbosity, *args):
    if verbosity <= VERBOSITY:
        for arg in args:
            print(arg, end=" ")
        print()


def hexprint(arg):
    if isinstance(arg, list):
        lis = []
        for i in arg:
            lis.append(hexprint(i))
        return lis
    else:
        return hex(arg)
