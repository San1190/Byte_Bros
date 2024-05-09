def txt():
    print("Hello world!")

txt = decor(txt)


@decor
def txt():
    print("Hello Wolrd!")