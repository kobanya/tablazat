def tabla(t):
    with open( t, 'r', encoding='utf-8') as f:
    # Az összes adatsor feldolgozása
        sorok = f.readlines()

    # Táblázat fejléce
        fejlec = sorok[0].strip().split(",")

    # Táblázat tartalma
        tartalom = []
        for sor in sorok[1:]:
            sor = sor.strip().split(",")
            tartalom.append(sor)

    # Táblázat kiírása
        oszlop_szelesseg = [max(len(str(oszlop)), len(max([str(sor[i]) for sor in tartalom], key=len))) for i, oszlop in
        enumerate(fejlec)]
        szelesseg = sum(oszlop_szelesseg) + 3 * (len(oszlop_szelesseg) )
        print("\u250C" + "\u2500" * (szelesseg - 1) + "\u2510")
        print("\u2502", end=" ")

        for i, oszlop in enumerate(fejlec):
            if i == 0:
                print("\033[91m{:^{width}}\033[0m".format(oszlop, width=oszlop_szelesseg[i]), end="  ")
            else:
                print("\u2502\033[91m{:^{width}}\033[0m".format(oszlop, width=oszlop_szelesseg[i]), end="  ")
        print("\u2502")
        print("\u251C" + "\u253C".join(["\u2500" * (width + 2) for width in oszlop_szelesseg]) + "\u2524")
        for sor in tartalom:
            for i, oszlop in enumerate(sor):
                print("\u2502" + "{:^{width}}".format(oszlop,
                width=oszlop_szelesseg[i] + 2),
                end="")
            print("\u2502")
            if sor == tartalom[-1]:
                print("\u2514" + "\u2534".join(["\u2500" * (width + 2) for width in oszlop_szelesseg]) + "\u2518")
            else:
                print("\u251C" + "\u253C".join(["\u2500" * (width + 2) for width in oszlop_szelesseg]) + "\u2524")

tabla('superbowl.csv')