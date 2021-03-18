def sockMerchant(n,ar):

    sock_accounting = dict()
    for sock in ar:
        sock_accounting[sock] = sock_accounting.get(sock, 0) + 1

    for sock,count in sock_accounting.items():
        sock_accounting[sock] = count // 2


    return sum(sock_accounting.values())


n = input()
colors_of_socks = [int(x) for x in input().split()]
print(sockMerchant(n,colors_of_socks))