def decorator(main):
    def wrapper():
        print("Hello world")
        main()
    return wrapper


@decorator
def main():
    print("I am learning Git")


main()
