def NULL_not_found(object: any) -> int:
    #print("type:" + str(type(object)) + str(bool(object)))
    dict_null = {"Nothing : " : None, "Chesse : " : float, "Zero : " : int, "Empty : " : str, "Fake : " : bool}
    if bool(object) == False:
        for key in dict_null:
            if dict_null[key] == type(object) or object == None:
                print(key + str(object) + " " + str(type(object)))
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