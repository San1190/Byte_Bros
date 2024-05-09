try:
    n = 10

    print(n + "hello")
    print(n / 2)

except ZeroDivisionError:
    print("Divided by zero")

except (ValueError, TypeError):
    print("Erro occurred")