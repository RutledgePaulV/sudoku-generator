class Cell:

    # defining the cell, each cell keeps track of its own value and location
    def __init__(self, row, col, box):
        self.row = row
        self.col = col
        self.box = box

        self.value = 0

    # returns a string representation of cell (for debugging)
    def __str__(self):
        temp = (self.value, self.row, self.col, self.box)
        return "Value: %d, Row: %d, Col: %d, Box: %d" % temp
