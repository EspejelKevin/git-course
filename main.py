def decorator(main):
    def wrapper():
        print("Hello world")
        main()
    return wrapper


@decorator
def main():
    print("I am learning Git")


@decorator
def task():
    print("Creating a new message")



def test():
    print("Learning branching")


@decorator
def test2():
    print("Learning branching 2")


main()
test()
test2()
task()