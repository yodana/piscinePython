def NULL_not_found(object: any) -> int:
    dict_null = {"Nothing : " : None, "Chesse : " : float, "Zero : " : int, "Empty : " : str, "Fake : " : bool}
    for key in dict_null:
        print(dict_null[key])
        if dict_null[key] == type(object) or object == None:
            if ((type(object) != str) or (type(object) == str and object == "")):
                print(key + str(object) + " " + str(type(object)))
            else:
                print("Type not found")
            return 42
    print("Type not found")
    return 42

Nothing = None
Garlic = float("NaN")
Zero = 0
Empty = ""
Fake = False
NULL_not_found(Nothing)
NULL_not_found(Garlic)
NULL_not_found(Zero)
NULL_not_found(Empty)
NULL_not_found(Fake)
print(NULL_not_found("Brian"))