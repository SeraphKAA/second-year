# import ppm
 #---------------------------------------------------------------------------
def LZSS(string, encLength, bufferSize, dictSize, dictFill):
  dictionaryAndString = [ dictFill ] * dictSize + list(string)
  compressedString = [ [], [], [] ]
 
  i = 0
  while i < len(string):
    buffer = string[i:bufferSize+i]
    d = ''.join(str(dictionaryAndString[i:dictSize+i]))
    dictionary = ''
    for j in d:
      dictionary += str(j)

    found = False
    for j in range(len(buffer), 0, -1):
      searched = buffer[:j]
      size = len(searched)
      if (size < encLength): break
      offset = dictionary.find(searched)
      if offset > -1:
        found = True
        compressedString[0].append('t')
        compressedString[1].append(offset)
        compressedString[2].append(size)
        break

    if not found:
      compressedString[0].append('f')
      compressedString[1].append(searched)
      compressedString[2].append(size)
    
    i = i + size
   
  return compressedString


# def LZSS(string, encLength, bufferSize, dictSize, dictFill):
#   dictionaryAndString = [ dictFill ] * dictSize + list(string)
#   compressedString = [ [], [], [] ]
 
#   i = 0
#   while i < len(string):
#     buffer = string[i:bufferSize+i]
#     dictionary = ''.join(dictionaryAndString[i:dictSize+i])
#     print(dictionary)
#     found = False
#     for j in range(len(buffer), 0, -1):
#       searched = buffer[:j]
#       size = len(searched)
#       if (size < encLength): break
#       offset = dictionary.find(searched)
#       if offset > -1:
#         found = True
#         compressedString[0].append(found)
#         compressedString[1].append(offset)
#         compressedString[2].append(size)
#         break
#     if not found:
#       compressedString[0].append(found)
#       compressedString[1].append(searched)
#       compressedString[2].append(size)
    
#     i = i + size
   
#   return compressedString

 #---------------------------------------------------------------------------


 
 #---------------------------------------------------------------------------
def decompressLZSS(compressedStr, dictFill, dictSize):
  dictionaryAndString = [ dictFill ] * dictSize; decompressedString = []
 
  for i in range(len(compressedStr[0])):
    if compressedStr[0][i] == "t":
      offset = compressedStr[1][i]
      size = compressedStr[2][i]
      found = dictionaryAndString[offset:size + offset]
      decompressedString = decompressedString + found
      dictionaryAndString = dictionaryAndString + found
      
    else:
      dictionaryAndString = dictionaryAndString + list(compressedStr[1][i])
      decompressedString = decompressedString + list(compressedStr[1][i])
      
    dictionaryAndString = dictionaryAndString[len(dictionaryAndString) - dictSize :]
 
  return ''.join(decompressedString)
 #---------------------------------------------------------------------------
 
def decomress_size(dict2):
  i = 0
  result = ''
  temp = ''
  while i < len(dict2):
    if dict2[i] == '|':
      index = len(temp) - 1
      symbol = temp[index]
      result += int(temp[:-1]) * symbol
      temp = ''
      i += 1
      
    else:
      temp += dict2[i]
      i += 1

  return result 
 
 #---------------------------------------------------------------------------
def saveToFile(saveFile, compressedStr):
  # compressedStr[0] = ['f', 'f', 't', 't', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f']
  if saveFile.closed:
    print("File closed")
  else:

    # count = 1
    # result = ''
    # for i in range(1, len(string)):
    #     if string[i] == string[i-1]:
    #         count += 1
    #     else:
    #         result += str(count) + string[i-1]
    #         count = 1
    # result += str(count) + string[-1]
    # return result

    for tab in compressedStr:

      if compressedStr.index(tab) == 0:
        saveFile0 = open("compressed0.txt", 'w+')
        count = 1
        result = ''
        for i in range (len(tab)):
          if tab[i] == tab[i-1]:         
            count += 1

          else:
            result += str(count) + tab[i-1]
            count = 1

        result += str(count) + tab[-1]
        saveFile0.write(result)
        saveFile0.close()

      elif compressedStr.index(tab) == 1:
        for value in tab:
          saveFile.write(str(value))

      elif compressedStr.index(tab) == 2:
        saveFile2 = open("compressed2.txt", "w+")
        count = 1
        result = ''

        for i in range (len(tab)):
          if tab[i] == tab[i-1]:         
            count += 1

          else:
            result += str(count) + str(tab[i-1]) + '|'
            count = 1

        result += str(count) + str(tab[-1]) + '|'
        saveFile2.write(result)
        saveFile2.close()

    saveFile.close()

        # if 0 == compressedStr.index(tab):
        #   countf = 0
        #   countt = 0

        #   for j in range(len(tab)):
        #     if tab[j] == 'f':
        #       countf += 1
            
        #     elif tab[j] == 't':
        #       countt += 1
            
        #     if j != len(tab) - 1 and tab[j + 1] != 'f':
        #       saveFile.write(str(countf) + 'f')
        #       countf = 0
            
        #     elif j != len(tab) - 1 and tab[j + 1] != 't':
        #       saveFile.write(str(countt) + 't')
        #       countt = 0


        # elif 2 == compressedStr.index(tab):
        #   pass
        # else:


 #---------------------------------------------------------------------------
 

 
 









    # w_uncompr = open("C:\\Users\\79045\\Desktop\\бессонные ночи\\сделанное дз\\2 курс 4 сем\\лабы у ляхи\\laba 1\\ppm_uncompressed.txt", 'w', encoding = "utf-8")
    # temp1 = ''
    # temp2 = ''
    # global temp3
    
    # temp3 = list()
    
    # for i in uncompressed_data:
    #   for j in i:
    #      if type(j) == int:
    #         temp1 += str(j) + '\t'
    #      elif type(j) == str:
    #         temp2 += '"'+ str(j) + '"' + '\t'
    #         try:
    #            temp3.append(int(j))
    #         except:
    #            temp3.append(j)

    
    # w_uncompr.write(temp1 + '\n')
    # w_uncompr.write(temp2)
    # # print('after decompression:\n' + 'decompressed:', temp2 + '\n' + '              ', temp1)
    # print('after decompression:\n' + temp2 + '\n' + temp1)
    # w_uncompr.close()

    # return uncompressed_data

# dictFill = "a"
# encLength = 3
# dictSize = 16
# bufferSize = 8
 
# compressFile = open("C:\\Users\\79045\\Desktop\\бессонные ночи\\сделанное дз\\2 курс 4 сем\\лабы у ляхи\\laba 1\\ppm_compressed.txt", "r", encoding = "utf-8")
compressedFile = open("C:\\Users\\79045\\Desktop\\бессонные ночи\\сделанное дз\\2 курс 4 сем\\лабы у ляхи\\laba 1\\compressed.txt", "w", encoding = "utf-8")
# sampleString = compressFile.read(); sampleString = sampleString[:-1]
# compressFile.close()

# row_text_txt = open("C:\\Users\\79045\\Desktop\\бессонные ночи\\сделанное дз\\2 курс 4 сем\\лабы у ляхи\\laba 1\\compressMuMu.txt", 'r', encoding = "utf-8")
# tempus = row_text_txt.read()
# row_text_txt.close()

# sampleString = ppm.encode_ppm(tempus)

# def main():
#   # print("before compression lzss:\n{}\n".format(sampleString))
#   global tlz0, tlz2
#   compStr = LZSS(sampleString, encLength, bufferSize, dictSize, dictFill)
#   global ac, result; ac = ''; result = list(); temp_count = 0

#   tlz0 = compStr[0]; tlz2 = compStr[2]

 
# #   print("compression:")
# #   print('found:', end='\t')
# #   for i in range(len(compStr[0])):
# #     print(repr(str(compStr[0][i])), end='\t')
  

# #   print('\noffset:', end='\t')
#   for i in range(len(compStr[1])):
#     # print(repr(str(compStr[1][i])), end='\t')
#     temp_count += 1
#     temp = ({temp_count: str(compStr[1][i])})
#     result.append(str(compStr[1][i]))
#     ac += str(compStr[1][i])
  
# #   print('\nlength:', end='\t')
# #   for i in range(len(compStr[2])):
#     # print(repr(str(compStr[2][i])), end='\t')
 
#   saveToFile(compressedFile, compStr)

#   return compStr
import random
def save():
  result = ""
  temp = 0 
  # пока сумма чисел не превышает 12319
  while temp < 12319:
    # генерируем случайное число от 1 до 32
    r = random.randint(1, 32)
    temp += r
    # добавляем число в строку
    result += str(r) + str(random.randint(1, 8)) + '|'
  
  a = open("compressed2.txt", 'w')
  a.write(result)
  a.close()
  
  result = ""
  temp = 0 
  # пока сумма чисел не превышает 12319
  while temp < 12319:
    # генерируем случайное число от 1 до 32
    r = random.randint(1, 32)
    temp += r
    # добавляем число в строку
    result += str(r) + random.choice(["t", "f"]) + '|'
  
  a = open("compressed0.txt", 'w')
  a.write(result)
  a.close()


import os

def delete (): 
  if os.path.isfile('compressed0.txt'): 
    os.remove('compressed0.txt')

  if os.path.isfile('compressed2.txt'): 
    os.remove('compressed2.txt')

def save2():
  with open("photo\\gta sa.bmp", "rb") as s, open("after all.bmp", "wb") as f:
    asd = s.read()
    f.write(asd)


# def lzss_encode(text, window_size, lookahead_size, threshold):
#     # инициализация словаря и выходной строки
#     dictionary = ''
#     encoded_text = ''
#     current_position = 0

#     while current_position < len(text):
#         search_position = max(0, current_position - window_size)
#         window = text[search_position:current_position]
#         best_match = ''
#         best_match_length = 0
#         best_match_position = 0

#         # поиск самого длинного совпадения среди запаса идущих текстовых символов
#         for i in range(lookahead_size):
#             if current_position + i >= len(text):
#                 break
#             current_string = text[current_position:current_position + i + 1]
#             match_length = 0
#             match_position = 0
#             if current_string in dictionary:
#                 match_position = search_position + dictionary.index(current_string)
#                 while current_position + match_length < len(text) and text[match_position + match_length] == text[current_position + match_length] and match_length < lookahead_size:
#                     match_length += 1
#             if match_length > best_match_length:
#                 best_match_length = match_length
#                 best_match = current_string
#                 best_match_position = match_position

#         # добавление результатов поиска в выходную строку
#         if best_match_length >= threshold:
#             distance = current_position - best_match_position
#             encoded_text += f'({distance}, {best_match_length})'
#             current_position += best_match_length
#         else:
#             encoded_text += text[current_position]
#             dictionary += text[current_position]
#             current_position += 1

#         # обновление словаря
#         if len(dictionary) > window_size:
#             dictionary = dictionary[-window_size:]

#     return encoded_text



# def lzss_decode(encoded_text):
#     decoded_text = ''
#     i = 0
#     while i < len(encoded_text):
#         if encoded_text[i] == '(':
#             j = i + 1
#             while encoded_text[j] != ',':
#                 j += 1
#             distance = int(encoded_text[i + 1:j])

#             k = j + 2
#             while encoded_text[k] != ')':
#                 k += 1
#             length = int(encoded_text[j + 2:k])

#             start = len(decoded_text) - distance
#             for l in range(length):
#                 decoded_text += decoded_text[start + l]
#             i = k + 1
#         else:
#             decoded_text += encoded_text[i]
#             i += 1
#     return decoded_text


