### Matteo Bianchini ###
### WAV Decoder ###

import sys


def header_decoder(wav_content):
    print("Decode Header")
    #Raise exception if Header doesn't correspond to what expect
    if (wav_content[0] != 0x52 or wav_content[1] != 0x49 or wav_content[2] != 0x46 or wav_content[3] != 0x46):
        raise TypeError("File corrupted")
    #Read file dim (add 8 bytes at the end that miss in the header of the file)
    file_dim = (wav_content[7] << 24) + (wav_content[6] << 16) + (wav_content[5] << 8) + wav_content[4]
    print("File size =", file_dim +8)
    if (wav_content[8:16] != b'WAVEfmt '):
        raise TypeError("File corrupted")


if __name__ == "__main__":
    print("---------------------------------------------")
    print("@@@@        Welcome to WAV Decoder       @@@@")
    print("---------------------------------------------")
    #file is passed as argument
    file_name= sys.argv[1]
    #read file content as binary
    with open(sys.argv[1], 'rb') as file:
        content = file.read()
    #decoder func
    print(type(content))
    header_decoder(content[0:16])