socks = [1,2,2,1,1,3,5,1,4,4]
print(socks)

sock_drawer = dict()

for s in socks:
    if s in sock_drawer:
        sock_drawer[s] += 1
    else:
        sock_drawer[s] = 1

for key, value in sock_drawer.items():
    # if value % 2 == 1:
    #     print(key, value)
    if value > 1:
        # result = value / 2
        print(f"{key} has {(value / 2):.0f} pair(s)")