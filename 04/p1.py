with open("input.txt") as file:
    order = file.readline().strip().split(",")
    print(order)
    boards = []
    while file.readline():
        boards.append([line for line in [file.readline().strip().split() for i in range(5)]])

def checkWinningBoard(track, hor, ver):
    for i in range(hor):
        if sum(track[i]) == hor:
            return True
    for i in range(ver):
        if sum([track[j][i] for j in range(ver)]) == ver:
            return True
    return False

def mapBoard(board, track, hor, ver, num):
    for i in range(hor):
        for j in range(ver):
            if num == board[i][j]:
                track[i][j] = True
    return track

def mapNot(board, track):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if track[i][j]:
                board[i][j] = 0
    return board

def mult(board, num):
    ctr = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            ctr += int(num)*int(board[i][j])
    return ctr

tracker = [[[False for i in range(5)] for j in range(5)] for board in boards]

m = lambda board, tracker, num: [True if board[t] == num else tracker[t] for t in range(len(tracker))]

winnerBoard = []
winTrack = []
winNum = 0

won = False
for num in order:
    if won:
        break
    for b in range(len(boards)):
        if won:
            break
        tracker[b] = mapBoard(boards[b], tracker[b], 5, 5, num)
        if checkWinningBoard(tracker[b], 5, 5):
            won = True
            winnerBoard = boards[b]
            winTrack = tracker[b]
            winNum = num

for line in winnerBoard:
    print(line)
print(winNum)
winnerBoard = mapNot(winnerBoard, winTrack)
out = mult(winnerBoard, winNum)
print(out)

    
                
