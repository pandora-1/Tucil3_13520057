# Nama : Marcellus Michael Herman Kahari
# NIM : 13520057
# Kelas : K03

from helper import *
from puzzle import *
import time
from queue import PriorityQueue

print("""
  __ _____       _____               _      
 /_ | ____|     |  __ \             | |     
  | | |__ ______| |__) |   _ _______| | ___ 
  | |___ \______|  ___/ | | |_  /_  / |/ _ 
  | |___) |     | |   | |_| |/ / / /| |  __/
  |_|____/      |_|    \__,_/___/___|_|\___|
""")
print()
print("Selamat datang di permainan puzzle 15")
print("Kami tidak pernah meragukan pemain meski permintaannya aneh-aneh")
print("Kami akan membantu pemain untuk menyelesaikan puzzle ini")
print()
print("Anda ingin memasukkan puzzle anda sendiri dari file.txt atau ingin membuat puzzle dari pembangkit bilangan acak? (Masukkan nomornya saja)")
print("1. Masukkan puzzle dari file.txt")
print("2. Buat puzzle dari pembangkit bilangan acak")
tipe = int(input("Masukkan nomor: "))
if(tipe == 1):
    file = input("Masukkan nama file yang hendak diselesaikan yang terdapat pada folder test (tidak perlu memasukkan path test/): ")
    puzzle = Puzzle(readFile('test/' + file))
elif(tipe == 2):
    print()
    print("Puzzle yang akan diselesaikan adalah puzzle ini:")
    puzzle = Puzzle(generatePuzzle()) # Akan membangkitkan puzzle acak
    puzzle.printPuzzle()
    print()
else:
    print("Masukkan nomor yang valid")
    exit()

# Membaca file solusi
puzzle_solution = readFile('src\solution.txt')

# Menghitung nilai KURANG(i)
valueX_temp, i, j = valueX(puzzle.getPuzzle())
print("Posisi KURANG(i) untuk setiap i:")
total_I_below_J = countIBelowJ(puzzle.getPuzzle(), True)
print("Total KURANG(i) + X adalah ", total_I_below_J + valueX_temp)

# Mengecek apakah puzzle bisa diselesaikan atau tidak
if(total_I_below_J + valueX_temp % 2 == 1):
    print("Tidak bisa diselesaikan")
else:
    puzzle_saver = PriorityQueue() # Menyimpan puzzle yang sudah dikunjungi dan bertindak sebagai prioqueue
    puzzle_count_node = [] # Menyimpan jumlah node yang dibangkitkan untuk puzzle yang sudah dikunjungi

    puzzle_saver.put((0,puzzle)) # Inisialisasi pertama kali
    puzzle_count_node.append(puzzle) # Inisialisasi pertama kali

    startTime = time.time() # Waktu menghitung dimulai
    while(countDifferent(puzzle_saver.queue[0][1].getPuzzle(), puzzle_solution) != 0): # Jika masih terdapat perbedaan, lakukan while loop
        currentPuzzle = puzzle_saver.get()[1] # Menghapus elemen pertama dari priqueue

        # Membangkitkan anak dari parent dengan memindahkan kotak kosong ke atas
        if(currentPuzzle.getPosisiEmptyI() != 0 and currentPuzzle.getHistoryRute()[-1] != 'down'):
            up = deepcopy(currentPuzzle)
            up.moveUp()
            functionMove(up, 'up', puzzle_saver, puzzle_solution, currentPuzzle.historyRute, puzzle_count_node)

        # Membangkitkan anak dari parent dengan memindahkan kotak kosong ke bawah
        if(currentPuzzle.getPosisiEmptyI() != 3 and currentPuzzle.getHistoryRute()[-1] != 'up'):
            down = deepcopy(currentPuzzle)
            down.moveDown()
            functionMove(down, 'down', puzzle_saver, puzzle_solution, currentPuzzle.historyRute, puzzle_count_node)
        
        # Membangkitkan anak dari parent dengan memindahkan kotak kosong ke kiri
        if(currentPuzzle.getPosisiEmptyJ() != 0 and currentPuzzle.getHistoryRute()[-1] != 'right'):
            left = deepcopy(currentPuzzle)
            left.moveLeft()
            functionMove(left, 'left', puzzle_saver, puzzle_solution, currentPuzzle.historyRute, puzzle_count_node)
        
        # Membangkitkan anak dari parent dengan memindahkan kotak kosong ke kanan
        if(currentPuzzle.getPosisiEmptyJ() != 3 and currentPuzzle.getHistoryRute()[-1] != 'left'):
            right = deepcopy(currentPuzzle)
            right.moveRight()
            functionMove(right, 'right', puzzle_saver, puzzle_solution, currentPuzzle.historyRute, puzzle_count_node)

    # Waktu menghitung selesai
    endTime = time.time() 
    executionTime = (endTime-startTime)*1.00
    index = 1

    # Melakukan print hasil
    print()
    print("Posisi puzzle 15 awal:")
    puzzle.printPuzzle()
    # Digunakan history rute sebagai penyimpan command yang akan dilakukan oleh puzzle
    # Hasil dari historyRute pada indeks 0 akan dijamin jika dilakukan secara berurutan
    # akan menghasilkan puzzle tujuan
    for i in puzzle_saver.queue[0][1].historyRute:
        if(i == 'blank'):
            continue
        print("Langkah ke-", index, " adalah ")
        if(i == 'up'):
            puzzle.moveUp()
            puzzle.printPuzzle()
        elif(i == 'down'):
            puzzle.moveDown()
            puzzle.printPuzzle()
        elif(i == 'left'):
            puzzle.moveLeft()
            puzzle.printPuzzle()
        elif(i == 'right'):
            puzzle.moveRight()
            puzzle.printPuzzle()
        index += 1

    print("Banyak simpul yang dibuat adalah " + str(len(puzzle_count_node))) # Diambil dari panjang puzzle_count_node
    print("Waktu eksekusi program adalah " + str(round((executionTime),4)) + " sekon")