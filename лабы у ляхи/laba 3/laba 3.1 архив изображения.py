import ppm, LZSS


row_text_txt = open("C:\\Users\\79045\\Desktop\\бессонные ночи\\сделанное дз\\2 курс 4 сем\\лабы у ляхи\\laba 3\\photo\\gta sa.bmp", 'rb')
header = row_text_txt.read(54)

tempus = row_text_txt.read()
row_text_txt.close()
 #---------------------------------------------------------------------------


print(1)
tempuss = str(tempus)
compr_text_ppm = ppm.encode_ppm(tempuss)
text = ''
for i in compr_text_ppm:
    text += str(i)

 #---------------------------------------------------------------------------
print(2)

dictFill = "a"
encLength = 64
dictSize = 32
bufferSize = 32

compStr = LZSS.LZSS(text, encLength, bufferSize, dictSize, dictFill)



compressedFile = open("C:\\Users\\79045\\Desktop\\бессонные ночи\\сделанное дз\\2 курс 4 сем\\лабы у ляхи\\laba 3\\compressed.bmp", "w")
LZSS.saveToFile(compressedFile, compStr)
compressedFile.close()

#---------------------------------------------------------------------------
print(3)
decompr_text_lzss = LZSS.decompressLZSS(compStr, dictFill, dictSize)
# print(decompr_text_lzss)
temp1 = decompr_text_lzss.split("|")
temp1.pop()
# print(f"{temp1}")
txt = list(map(int, temp1))


#---------------------------------------------------------------------------
print(4)
final_text = ppm.decode_ppm(txt)
final = open("C:\\Users\\79045\\Desktop\\бессонные ночи\\сделанное дз\\2 курс 4 сем\\лабы у ляхи\\laba 3\\after all.bmp", 'wb')
final.write(header)
final.write(final_text.encode('utf-8'))
final.close()
































LZSS.save2(); LZSS.delete()
# LZSS.save()