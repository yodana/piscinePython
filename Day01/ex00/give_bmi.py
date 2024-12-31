"""functions for calculating bmi and test the limit"""


def give_bmi(
    height: list[int | float],
    weight: list[int | float]
) -> list[int | float]:
    """ give_bmi(height: list[int | float], weight: list[int | float])
        -> list[int | float]
        calcul the bmi (Body Mass Index)
    """
    try:
        msg_error = "AssertationError: "
        assert isinstance(height, list) and isinstance(weight, list), \
            msg_error + "height or weight are not list types"
        assert all(isinstance(val, (int, float)) for val in height), \
            msg_error + "all height values are not int or float types"
        assert all(isinstance(val, (int, float)) for val in weight), \
            msg_error + "all weight values are not int or float types"
        assert all(val > 0 for val in height), \
            msg_error + "height values can't be negative"
        assert all(val > 0 for val in weight), \
            msg_error + "weight values can't be negative"
        assert len(height) == len(weight), \
            msg_error + "the lists are not equals"
    except AssertionError as msg:
        print(msg)
        return []
    new_list = [wei/(hei * hei) for hei, wei in zip(height, weight)]
    return new_list


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """ apply_limit(bmi: list[int | float], limit: int) -> list[bool]
        see if the limit is respected
    """
    try:
        msg_error = "AssertationError: "
        assert all(isinstance(val, (int, float)) for val in bmi), \
            msg_error + "all height values are not int or float types"
        assert isinstance(limit, int), \
            msg_error + "limit value is not int type"
    except AssertionError as msg:
        print(msg)
        return []
    new_list = [solo_bmi > limit for solo_bmi in bmi]
    return new_list
