ERROR_POINTER_OUT_FROM_MEMORY = "Pointer is homeless"


memory = [0 for _ in range(32768)]
pointer = 0

def run(bfCode: str) -> None:
    readingIndex = 0
    inputQueue = []


    while readingIndex < len(bfCode):
        token = bfCode[readingIndex]
        
        # print(pointer)

        match(token):
            case ">":
                __movePointerRight()
            case "<":
                __movePointerLeft()
            case "+":
                memory[pointer] += 1
            case "-":
                memory[pointer] -= 1
            case ".":
                print(chr(memory[pointer]), end="")
            case ",":
                if len(inputQueue) == 0: 
                    datas = input()
                    for data in datas: inputQueue.append(data)
                memory[pointer] = ord(inputQueue.pop())
            case "[":
                if memory[pointer] != 0: 
                    readingIndex += 1
                    continue
                # 짝으로 이동
                bracket = 1
                while bracket != 0:
                    readingIndex += 1
                    match(bfCode[readingIndex]):
                        case "[": bracket += 1
                        case "]": bracket -= 1
                # readingIndex += 1
            case "]":
                if memory[pointer] == 0: 
                    readingIndex += 1
                    continue
                # 짝으로 이동
                bracket = 1
                while bracket != 0:
                    readingIndex -= 1
                    match(bfCode[readingIndex]):
                        case "[": bracket -= 1
                        case "]": bracket += 1
                # readingIndex += 1

        readingIndex += 1
    


def __movePointerRight():
    global pointer
    pointer += 1

    if pointer == len(memory):
        # print(ERROR_POINTER_OUT_FROM_MEMORY)
        raise Exception(ERROR_POINTER_OUT_FROM_MEMORY)

def __movePointerLeft():
    global pointer
    pointer -= 1

    if pointer < 0:
        # print(ERROR_POINTER_OUT_FROM_MEMORY)
        raise Exception(ERROR_POINTER_OUT_FROM_MEMORY)
