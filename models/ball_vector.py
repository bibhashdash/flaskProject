class BallVector:

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __sub__(self, other):
        vector_difference = BallVector(self.x - other.x, self.y - other.y)
        return vector_difference

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y