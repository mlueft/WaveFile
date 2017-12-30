from BinaryFile import BinaryFile

## A Class to write wave files.
#  
class WaveFile:

    ##
    #  @param   samplingRate    The sampling rate of the wave file.
    #  @param   resolution      Resolution in bits. Normally 8 or 16
    #  @param   channels        Number of channels.
    #                           1 - mono
    #                           2 - stereo
    #
    def __init__(self, samplingRate=22000, resolution= 8, channels = 1):
        self.__samplingRate = samplingRate
        self.__resolution   = resolution
        self.__channels     = channels

    ##
    #  @param   file            File handle.
    #  @param   size            Chunk size in bytes.
    #
    def __writeFileHeader(self, file, size):
        
        # ID
        file.writeChar("RIFF")

        # CHUNKSIZE
        file.writeInt32(size)

        file.writeChar("WAVE")

    ##
    #  @param   file            File handle.
    #
    def __writeChunk1(self, file):
        
        # ID
        file.writeChar("fmt ")

        # SubChunkSize
        file.writeInt32(16)

        # audio format
        file.writeInt16(1)

        # channels
        file.writeInt16(self.__channels )

        # sampling rate
        file.writeInt32( self.__samplingRate )

        # byte rate
        file.writeInt32( self.__resolution/8 * self.__channels * self.__samplingRate )

        # block align
        file.writeInt16( self.__resolution/8 * self.__samplingRate )

        # bits per sample
        file.writeInt16( self.__resolution )

    ##
    #  @param   file            File handle.
    #  @param   data            sound data to write.
    #
    def __writeData(self, file, data):
        
        file.writeChar("data")

        file.writeInt32(
            len(data)*self.__channels*self.__resolution/8
        )

        bps = self.__resolution/8

        for i in data:
            i = int(i)
            if bps == 1:
                file.writeInt8(i)
            elif bps == 2:
                file.writeInt16(i)
            elif bps == 3:
                file.writeInt24(i)
            elif bps == 4:
                file.writeInt32(i)
            elif bps == 8:
                file.writeInt64(i)

    ##
    #  @param   fileName    The file name.
    #  @param   data        Sound data.
    #
    def save(self, fileName, data):
        
        file = BinaryFile.BinaryFile( fileName, "wb+" )
        file.bigEndian = False

        size = 4
        size = size + 4+4+2+2+4+4+2+2
        size = size + 4+4+len(data)

        self.__writeFileHeader(file, size)
        self.__writeChunk1(file)
        self.__writeData(file, data)

        file.close()



