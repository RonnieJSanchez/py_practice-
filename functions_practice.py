def hello():
    print("Hello Stranger!")


def pack(x, y, z):
    return [x, y, z]


def eat_lunch(i_eat):
    if len(i_eat) == 0:
        print("My lunchbox is empty!")
    else:
        for i in range(len(i_eat)):
            if i == 0:
                print(f"First I eat {i_eat[0]}")
            else:
                print(f"Next I eat {i_eat[i]}")


hello()
print(pack("x", "y", "z"))
print(pack(1, 2, 3))
eat_lunch([])
eat_lunch(["a sandwhich"])
eat_lunch(["a snickers", "some jerky", "fruit snacks", "pretzles"])
