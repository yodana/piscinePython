def NULL_not_found(object: any) -> int:
    dict_null = {"Nothing : " : None, "Chesse : " : float, "Zero : " : int, "Empty : " : str, "Fake : " : bool}
    if bool(object) == False or (type(object) == float and object != object):
        for key in dict_null:
            if dict_null[key] == type(object) or object == None:
                print(key + str(object) + " " + str(type(object)))
                return 42
    print("Type not found")
    return 42