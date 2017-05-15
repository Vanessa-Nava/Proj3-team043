import struct

# open file we want to read in
file = open("iCry (1).wav","rb")  
ChunkID=file.read(4) # First four bytes are ChunkID which must be "RIFF" in ASCII
print("ChunkID=",ChunkID)

ChunkSizeString=file.read(4) # Total Size of File in Bytes - 8 Bytes
ChunkSize=struct.unpack('I',ChunkSizeString) # 'I' Format is to to treat the 4 bytes 
TotalSize=ChunkSize[0]+8 # The subscript is used because struct unpack returns everything as tuple
print("TotalSize=",TotalSize)


DataSize=TotalSize-44 # This is the number of bytes of data
print("DataSize=",DataSize)

Format=file.read(4) # "WAVE" in ASCII
print("Format=",Format)

SubChunk1ID=file.read(4) # "fmt " in ASCII
print("SubChunk1ID=",SubChunk1ID)

file.close()