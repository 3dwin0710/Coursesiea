def syracuse(n, count):
    if n > 1:
        print("Etape: {}".format(count))
        print("=> {}".format(n))
        if(n%2==0):
            print("Paire => {}/2".format(n))
        else:
            print("Impaire => 3*{}+1".format(n))
        print ("--------------------------------------------")
        return syracuse(3 * n + 1 if n % 2 == 1 else int(n / 2), count + 1)
    print("Resultat is :")
    return n





n = int(input())
m = int(input())

print(syracuse(n, m))
