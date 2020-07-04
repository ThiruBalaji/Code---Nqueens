class totalQueens:
    def __init__(self, size):
        """initial"""
        self.size = size
        self.solutions = 0
        self.score_pop()
    def score_pop(self):
        """No of Queens position found"""
        positions = [-1] * self.size
        self.initial_pop(positions, 0)
        print("Found", self.solutions, "solutions.")
 
    def initial_pop(self, positions, target_row):
        """Adding Full board in with Queens Position"""
        if target_row == self.size:
            self.show_full_board(positions)
            self.solutions += 1
        else:
            for column in range(self.size):
                if self.cross_over(positions, target_row, column):
                    positions[target_row] = column
                    self.initial_pop(positions, target_row + 1)
                    
    def cross_over(self, positions, ocuppied_rows, column):
        """position and occupied space"""
        for i in range(ocuppied_rows):
            if positions[i] == column or positions[i] - i == column - ocuppied_rows or positions[i] + i == column + ocuppied_rows:
                return False
        return True
 
    def show_full_board(self, positions):
        """Adding Full board in with Queens Position"""
        for row in range(self.size):
            line = ""
            for column in range(self.size):
                if positions[row] == column:
                    line += "Q "
                else:
                    line += ". "
            print(line)
        print("\n")
def main():
    """to identify the right sequence"""
    totalQueens(8)
    
if __name__ == "__main__":
    # execute only if run as a script
    main()