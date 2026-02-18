'''
FILE 3 INSTRUCTIONS:
- For this file, you'll be playing Tic Tac Toe against the computer
- Don't worry about changing any code in this file
- Just run, then try to beat the computer
- Once you win, you'll get a password for the free Monster
'''

b = ["_"] * 9
w = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
p = lambda: print(f"{b[0]}|{b[1]}|{b[2]}\n{b[3]}|{b[4]}|{b[5]}\n{b[6]}|{b[7]}|{b[8]}\n")

print("YOU: X | COMPUTER: O")
p()

while "_" in b:
    try:
        m = int(input("Your move (1-9): ")) - 1
        if not (0 <= m <= 8) or b[m] != "_": continue
        b[m] = "X"
    except: continue
    
    p()
    if any(all(b[i]=="X" for i in s) for s in w):
        print("--- You Win! The password for the Monster is HackAI2026 ---"); break
    
    e = [i for i, x in enumerate(b) if x == "_"]
    if not e: break
    
    print("Computer is moving...")
    b[e[hash(str(b)) % len(e)]] = "O"
    p()
    
    if any(all(b[i]=="O" for i in s) for s in w):
        print("--- Computer Wins! ---"); break