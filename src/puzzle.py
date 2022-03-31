from helper import *

class Puzzle:
    # Daftar atribut
    depth = 0
    historyRute = []
    posisiEmptyI = 0
    posisiEmptyJ = 0

    # constructor
    def __init__(self, puzzle):
        self.puzzle = puzzle
        for i in range(4):
            for j in range(4):
                if(int(puzzle[i][j]) == 16):
                    self.setPosisiEmptyI(i)
                    self.setPosisiEmptyJ(j)
                    break
    
    # Getter
    def getPosisiEmptyI(self):
        return self.posisiEmptyI
    
    def getPosisiEmptyJ(self):
        return self.posisiEmptyJ
    
    def getPuzzle(self):
        return self.puzzle
    
    def getDepth(self):
        return self.depth
    
    def getHistoryRute(self):
        return self.historyRute
    
    # Setter
    def setDepth(self, depth):
        self.depth += depth
    
    def setPosisiEmptyI(self, posisiI):
        self.posisiEmptyI = posisiI
    
    def setPosisiEmptyJ(self, posisiJ):
        self.posisiEmptyJ = posisiJ
    
    # Method
    def moveUp(self):
        if(self.posisiEmptyI != 0):
            self.puzzle[self.posisiEmptyI][self.posisiEmptyJ], self.puzzle[self.posisiEmptyI-1][self.posisiEmptyJ] = self.puzzle[self.posisiEmptyI-1][self.posisiEmptyJ], self.puzzle[self.posisiEmptyI][self.posisiEmptyJ]
            self.posisiEmptyI -= 1
    
    def moveDown(self):
        if(self.posisiEmptyI != 3):
            self.puzzle[self.posisiEmptyI][self.posisiEmptyJ], self.puzzle[self.posisiEmptyI+1][self.posisiEmptyJ] = self.puzzle[self.posisiEmptyI+1][self.posisiEmptyJ], self.puzzle[self.posisiEmptyI][self.posisiEmptyJ]
            self.posisiEmptyI += 1
    
    def moveLeft(self):
        if(self.posisiEmptyJ != 0):
            self.puzzle[self.posisiEmptyI][self.posisiEmptyJ], self.puzzle[self.posisiEmptyI][self.posisiEmptyJ-1] = self.puzzle[self.posisiEmptyI][self.posisiEmptyJ-1], self.puzzle[self.posisiEmptyI][self.posisiEmptyJ]
            self.posisiEmptyJ -= 1
    
    def moveRight(self):
        if(self.posisiEmptyJ != 3):
            self.puzzle[self.posisiEmptyI][self.posisiEmptyJ], self.puzzle[self.posisiEmptyI][self.posisiEmptyJ+1] = self.puzzle[self.posisiEmptyI][self.posisiEmptyJ+1], self.puzzle[self.posisiEmptyI][self.posisiEmptyJ]
            self.posisiEmptyJ += 1
    
    def printPuzzle(self):
        for i in range(4):
            for j in range(4):
                if(self.puzzle[i][j] == 16):
                    print('  ', end='')
                else:
                    print(self.puzzle[i][j], end=' ')
            print()
    
    def addRute(self, rute):
        self.historyRute.append(rute)
    
    def countCost(self, puzzle_solution):
        return countDifferent(self.puzzle, puzzle_solution) + self.depth