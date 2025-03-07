class calculator:

    def __init__(self, vector):
        self.vector = vector

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """ Dot product of 2 vectors """
        v_new = [v1 * v2 for v1, v2 in zip(V1, V2)]
        print("Dot product: " + str(sum(v_new)))

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """ Add 2 vectors """
        v_new = [float(v1 + v2) for v1, v2 in zip(V1, V2)]
        print("Add vector is : " + str(v_new))

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """ Sub 2 vectors """
        v_new = [float(v1 - v2) for v1, v2 in zip(V1, V2)]
        print("Sous vector is: " + str(v_new))
