import NowLang

def getBinary(token: str)->str:
    match(token):
        case ">": return "000"
        case "<": return "001"
        case "+": return "010"
        case "-": return "011"
        case ".": return "100"
        case ",": return "101"
        case "[": return "110"
        case "]": return "111"

# ++++++++++[>+++++++>++++++++++>+++>+<<<<-]>++.>+.+++++++..+++.>++++++++++++++.------------.<<+++++++++++++++.>.+++.------.--------.>+.>.

bfCode = input("BrainFuck Code : ").replace(" ", "").replace("\n", "")
bfPointer = 0

nowLangCode = ""

while bfPointer < len(bfCode):
    bfToken = bfCode[bfPointer]
    bfBinary = getBinary(bfToken)
    print(f"\n[ {bfToken} ({bfBinary}) ]")
    for i in range(3):
        # print("IN")
        target = int(bfBinary[i])
        command = ""
        while True:
            command = input(f"{target} : ")
            # print(command)
            if (len(command) + target) % 2 == 0: break
            print("re:", end="")
        nowLangCode += f"{command} 이제 "
    
    bfPointer += 1

print(nowLangCode[:-4])