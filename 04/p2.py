with open("input.txt") as file:
    order = [int(i) for i in file.readline().strip().split(",")]
    print(order)
    boards = []
    while file.readline():
        boards.append([line for line in [[int(j) for j in file.readline().strip().split()] for i in range(5)]])

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

def getNotWon(boards, winTracker):
    out = []
    for i in range(len(boards)):
        if not i in winTracker:
            out.append(boards[i])
    return out

tracker = [[[False for i in range(5)] for j in range(5)] for board in boards]

winnerBoard = []
winTrack = []
winNum = 0
contNum = 0

won = False
for num in order:
    if won:
        break
    contNum += 1
    for b in range(len(boards)):
        if b in winTrack:
            continue
        if winNum+1 == len(boards):
            won = True
            break
        tracker[b] = mapBoard(boards[b], tracker[b], 5, 5, num)
        if checkWinningBoard(tracker[b], 5, 5):
            print(b)
            winNum += 1
            winTrack.append(b)

last = getNotWon(boards, winTrack)[0]
lastTrack = getNotWon(tracker, winTrack)[0]
[print(line) for line in last]
print()
for num in order[contNum:]:
    lastTrack = mapBoard(last, lastTrack, 5, 5, num)
    if checkWinningBoard(lastTrack, 5, 5):
        winNum = num
        break
    
last = mapNot(last, lastTrack)
out = mult(last, winNum)
print(out)

    
                

