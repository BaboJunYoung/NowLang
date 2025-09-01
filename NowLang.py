import BrainFuck

SEPARATION_TOKEN = "이제"

# [ Public Functions ]
def run(code: str) -> None:
    code = code.split(SEPARATION_TOKEN)
    binaryCode = __getBinaryCode(code)

    __runBinaryCode(binaryCode)

def compile(code: str, fileName: str = "a") -> bool:
    binaryCode = __getBinaryCode(code)
    bfCode = __getBfCode(binaryCode)
    
    try:
        with open(f"./{fileName}.bf", "w", encoding="UTF8") as f:
            f.write(bfCode)
            
    except Exception as e:
        print(f"파일 처리 중 오류 발생: {e}")
        return False
    
    return True

"""
[bf 명령어의 종류]
0. 포인터 증가 >
1. 포인터 감소 <
2. 포인터 값 1 증가 +
3. 포인터 값 1 감소 -
4. 포인터 값 출력 .
5. 포인터에 입력 ,
6. 포인터 값이 0이면 짝( ] )으로 이동 [
7. 포인터 값이 0이 아니면 짝( [ )으로 이동 ]

[bf 대응관계]
000 <-> >
001 <-> <
010 <-> +
011 <-> -
100 <-> .
101 <-> ,
110 <-> [
111 <-> ]
"""

# [ Private Functions ]

# now Lang -> binary code
def __getBinaryCode(code: str) -> str:
    code = code.split(SEPARATION_TOKEN)
    binaryCode = ""

    for token in code:
        if len(token) % 2 == 0: binaryCode += "0"
        else: binaryCode += "1"
    
    return binaryCode

# binary code -> bf code
def __getBfCode(binaryCode: str) -> str:
    if len(binaryCode) % 3 != 0:
        print("토큰이 부족합니다.")
        return

    bfCode = ""
    numberCounter = 0

    for _ in range(len(binaryCode) // 3):
        match(binaryCode[:3]):
            # >
            case "000":
                if numberCounter != None: bfCode += " "
                numberCounter = None
                bfCode += ">"
            # <
            case "001": 
                if numberCounter != None: bfCode += " "
                numberCounter = None
                bfCode += "<"
            # +
            case "010":
                if numberCounter == None: 
                    numberCounter = 0
                    bfCode += " "

                bfCode += "+"
                numberCounter += 1

                if numberCounter % 5 == 0: bfCode += " "
            # -
            case "011":
                if numberCounter == None:
                    numberCounter = 0
                    bfCode += " "     
                bfCode += "-"
                numberCounter -= 1

                if numberCounter % 5 == 0: bfCode += " "
            # .
            case "100": 
                if numberCounter != None: bfCode += " "
                numberCounter = None
                bfCode += "."
            # ,
            case "101": 
                if numberCounter != None: bfCode += " "
                numberCounter = None
                bfCode += ","
            # [
            case "110": 
                if numberCounter != None: bfCode += " "
                numberCounter = None
                bfCode += "["
            # ]
            case "111": 
                if numberCounter != None: bfCode += " "
                numberCounter = None
                bfCode += "]"

            # exception
            case "_": raise Exception(f".now -> .bf 변환 도중 알 수 없는 토큰. \"{binaryCode[:3]}\"")
        binaryCode = binaryCode[3:]

    return bfCode

def __runBfCode(bfCode: str) -> None:
    BrainFuck.run(bfCode)        

def __runBinaryCode(binaryCode: str) -> None:
    bfCode = __getBfCode(binaryCode)
    __runBfCode(bfCode)