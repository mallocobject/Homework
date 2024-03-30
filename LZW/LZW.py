import sys
# import os

HEX = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']

def main():
    def myEncode(filename_in, filename_out):
        ump = {}
        for c in range(256):
            ump[chr(c)] = c
        
        with open(filename_in, 'r', encoding='UTF-8') as inputFile, open(filename_out, 'w', encoding='UTF-8') as outputFile:
            # Initialize variables
            key = ''
            value = 0xFF

            # Read the first character from the input file
            current_char = inputFile.read(1)
            key += current_char

            # Continue reading characters from the input file until the end of the file is reached
            while current_char:
                current_char = inputFile.read(1)
                temp = key
                key += current_char

                # If the current string of characters is not in the dictionary, add it
                if key not in ump:
                    temp_value = ump[temp]
                    ump[key] = value + 1
                    value += 1

                    # Write the encoded value to the output file
                    outputFile.write(HEX[(temp_value >> 8) & 0xF] + HEX[(temp_value >> 4) & 0xF] + HEX[temp_value & 0xF])

                    # Reset the key to the current character
                    key = current_char

    if len(sys.argv) == 1:
        filename_in = input("Enter the name of the input file (absolute path): ")
        filename_out = input("Enter the name of the output file (absolute path): ")
        myEncode(filename_in, filename_out)
    elif len(sys.argv) == 3:
        print(f"Reading from {sys.argv[1]}")
        print(f"Writing to {sys.argv[2]}")
        myEncode(sys.argv[1], sys.argv[2])
    else:
        print("Usage: python LZW.py <input file> <output file> (absolute paths)")
        return
    
    print("Encoding complete")
    
if __name__ == "__main__":
    main()