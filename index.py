with open('data.txt') as data :
    for index in data :
        cont = data.readline(2)
        if cont == 'BB' :
            print("bomba")
        elif cont == 'CC' :
            print("classic")
        elif cont == 'TT' :
            print("tutut")
        else :
            print("empty space")
