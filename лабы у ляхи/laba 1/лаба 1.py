# дан тест.
# закодировать с помощью алгоритма PPM затем LZSS сохранить закодированный тест в файл открыть файл с закодированным тестом, и декодировать с помощью алгоритма PPM затем LZ78.
# сохранить результат в новый файл.
# реализовать на python


import ppm, LZSS
# compressFile = open("C:\\Users\\79045\\Desktop\\бессонные ночи\\сделанное дз\\2 курс 4 сем\\лабы у ляхи\\laba 1\\ppm_compressed.txt", "r", encoding = "utf-8")

# sampleString = compressFile.read(); sampleString = sampleString[:-1]
# compressFile.close()





# row_text_txt = open("C:\\Users\\79045\\Desktop\\бессонные ночи\\сделанное дз\\2 курс 4 сем\\лабы у ляхи\\laba 1\\compr.txt", 'r', encoding = "utf-8")
row_text_txt = open("C:\\Users\\79045\\Desktop\\бессонные ночи\\сделанное дз\\2 курс 4 сем\\лабы у ляхи\\laba 1\\compressMuMu.txt", 'r', encoding = "utf-8")
tempus = row_text_txt.read()
row_text_txt.close()
 #---------------------------------------------------------------------------

# print(tempus)
print(1)
compr_text_ppm = ppm.encode_ppm(tempus)
text = ''
for i in compr_text_ppm:
    text += str(i)

# print(text, '\n', compr_text_ppm)

 #---------------------------------------------------------------------------
# compr_text_ppm_txt = open("C:\\Users\\79045\\Desktop\\бессонные ночи\\сделанное дз\\2 курс 4 сем\\лабы у ляхи\\laba 1\\ppm_compressed.txt", 'w', encoding = "utf-8")
# for i in range(len(compr_text_ppm)):
#   compr_text_ppm_txt.write(str(compr_text_ppm[i]))
print(2)

dictFill = "a"
encLength = 64
dictSize = 32
bufferSize = 32

compStr = LZSS.LZSS(text, encLength, bufferSize, dictSize, dictFill)




# print("compression:")
# print('found:', end='\t')
# for i in range(len(compStr[0])):
#   print(repr(str(compStr[0][i])), end='\t')
  

# print('\noffset:', end='\t')
# for i in range(len(compStr[1])):
#   print(repr(str(compStr[1][i])), end='\t')
#   temp_count += 1
#   temp = ({temp_count: str(compStr[1][i])})
#   result.append(str(compStr[1][i]))
#   ac += str(compStr[1][i])
  
# print('\nlength:', end='\t')
# for i in range(len(compStr[2])):
#   print(repr(str(compStr[2][i])), end='\t')
# print('\n')


compressedFile = open("C:\\Users\\79045\\Desktop\\бессонные ночи\\сделанное дз\\2 курс 4 сем\\лабы у ляхи\\laba 1\\compressed.txt", "w", encoding = "utf-8")
LZSS.saveToFile(compressedFile, compStr)
compressedFile.close()

#  #---------------------------------------------------------------------------
print(3)
decompr_text_lzss = LZSS.decompressLZSS(compStr, dictFill, dictSize)
# print(decompr_text_lzss)
temp1 = decompr_text_lzss.split("|")
temp1.pop()
# print(f"{temp1}")
txt = list(map(int, temp1))


# print(txt)


# de_lzss = open("C:\\Users\\79045\\Desktop\\бессонные ночи\\сделанное дз\\2 курс 4 сем\\лабы у ляхи\\laba 1\\decompressedLZSS.txt", 'w', encoding = "utf-8")
# de_lzss.write(decompr_text_lzss)
# de_lzss.close()


 #---------------------------------------------------------------------------
# decompr_text_lzss_txt = open("C:\\Users\\79045\\Desktop\\бессонные ночи\\сделанное дз\\2 курс 4 сем\\лабы у ляхи\\laba 1\\decompressedLZSS.txt", 'r', encoding = "utf-8")
# dec_lzss_list = list(map(int, decompr_text_lzss_txt.read().split(' ')))


# decompr_text_lzss_txt.close()

 #---------------------------------------------------------------------------
print(4)
final_text = ppm.decode_ppm(txt)

final = open("C:\\Users\\79045\\Desktop\\бессонные ночи\\сделанное дз\\2 курс 4 сем\\лабы у ляхи\\laba 1\\after all.txt", 'w', encoding = "utf-8")
final.write(final_text)
final.close()


# ass = "121|24|56|"
# print(LZSS.decomress_size(ass))























LZSS.save()