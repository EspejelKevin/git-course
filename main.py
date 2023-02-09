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


print("task test 1 ...")
print("task test 1 new print...")
print("nooooooooooow with pull")
print("whaaaaat")

main()
test()
task()
