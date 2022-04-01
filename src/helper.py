from copy import deepcopy
import random

def readFile(file):
    lines = []
    with open(file) as f:
        lines = f.readlines()
    count = 0
    puzzle = [[0 for i in range(4)] for j in range(4)]
    for line in lines:
        line = line.strip()
        count_temp = 0
        word = line.split(' ')
        for w in word:
            puzzle[count][count_temp] = int(w)
            count_temp += 1
        count += 1
    return puzzle

def countDifferent(puzzle, puzzle_solution):
    count = 0
    for i in range(4):
        for j in range(4):
            if (puzzle[i][j] != puzzle_solution[i][j]):
                count += 1
    return count

def valueX(puzzle):
    puzzle_16 = readFile('src/valueX.txt')
    for i in range(4):
        for j in range(4):
            if puzzle[i][j] == 16:
                return int(puzzle_16[i][j]), i, j

def countIBelowJ(puzzle, tampilkan):
    count = 0
    for i in range(4):
        for j in range(4):
            counter_tampilkan = 0
            for k in range(4):
                for l in range(4):
                    if (int(puzzle[i][j]) > int(puzzle[k][l])) and ((j + 4 * i) < (k * 4 + l)):
                        count += 1
                        counter_tampilkan += 1
            if(tampilkan):
                print(4*i + j, ", kurang(", 4*i + j,") bernilai ", counter_tampilkan)
    return count

def copyPuzzle(puzzle, puzzle_temp):
    for i in range(4):
        for j in range(4):
            puzzle_temp[i][j] = puzzle[i][j]
    return puzzle_temp

def generatePuzzle():
    puzzle = [[0 for i in range(4)] for i in range(4)]
    pembangkit_acak = random.sample(range(1, 17), 16)
    for i in range(4):
        for j in range(4):
            puzzle[i][j] = pembangkit_acak[4*i + j]
    return puzzle

def functionMove(temp, tujuan, puzzle_saver, puzzle_solution, rute, puzzle_count_node):
    temp.historyRute = deepcopy(rute)
    temp.setDepth(1)
    temp.addRute(tujuan)
    cost = temp.countCost(puzzle_solution)
    puzzle_saver.put((cost,temp))
    puzzle_count_node.append(temp)