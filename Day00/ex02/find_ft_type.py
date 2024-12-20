def all_thing_is_obj(object: any) -> int:
    dict_obj = {"is in the kitchen : " : str, "List : " : list, "Tuple : " : tuple, "Dict : " : dict, "Set : " : set}
    for key in dict_obj:
        if dict_obj[key] == type(object):
            if type(object) == str:
                print(object + " " + key + str(type(object)))
            else:
                print(key + str(type(object)))   
            return 42
    print("Type not found") 
    return 42