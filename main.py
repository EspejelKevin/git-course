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

print("another print from test-task2")
print("nooooooooooow with pull")
print("noooooow from task-test2")
print("whaaaaat")

main()
test()
task()
