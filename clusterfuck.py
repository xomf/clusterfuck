import sys
def generateCProgram(filename, hex_data):
    program = open("template.c","r").read() % (hex_data)
    return program

def generateHexData(file_path):
    with open(file_path, "rb") as file:
        data = file.read()
        hex_data = ",".join(["0x{:02x}".format(b) for b in data])
        return hex_data

if __name__ == "__main__":

    if len(sys.argv) == 1:
        print(f"usage: python3 {sys.argv[0]} ./input_binary output.c")
        exit()
        
    file_path = sys.argv[1]
    hex_data = generateHexData(file_path)
    program = generateCProgram(file_path, hex_data)

    with open(sys.argv[2], "w") as file:
        file.write(program)
