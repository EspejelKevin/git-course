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


@decorator
def test():
    print("Learning branching")


print("test2")
print("task test 1 ...")
print("task test 1 new print...")


main()
test()
task()
