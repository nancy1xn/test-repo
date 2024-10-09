from mymod import foo, convert_to_string


@convert_to_string
def bar():
    return 1


if __name__ == "__main__":
    foo()
    assert bar() == "1"
