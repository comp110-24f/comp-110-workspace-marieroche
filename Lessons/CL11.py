def chars(msg: str) -> str:
    copy: str = msg  # set up empty string to copy values over
    index: int = 0
    while index <= len(msg):
        print(msg[index])
        index += 1
    return copy


a: str = "hey"
b: str = "hi"
chars(msg=a)
