
contents = []

with open("myfile.txt", "r") as f:
  for line in f:
    contents.append(line.strip())

#DAY 1
# digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

# calibrations = []

# totalCalibrations = 0
# currentCalibration = ''

# for i in contents:
#   for j in range(len(i)):#
#     if i[j] in digits:
#       calibrations.append(i[j])
#     try: 
#       if i[j] + i[j + 1] + i[j + 2] == "one":
#         calibrations.append('1')
#       if i[j] + i[j + 1] + i[j + 2] == "two":
#         calibrations.append('2')
#       if i[j] + i[j + 1] + i[j + 2] == "six":
#         calibrations.append('6')
#       if i[j] + i[j + 1] + i[j + 2] + i[j + 3] == "four":
#         calibrations.append('4')
#       if i[j] + i[j + 1] + i[j + 2] + i[j + 3]== "five":
#         calibrations.append('5')
#       if i[j] + i[j + 1] + i[j + 2] + i[j + 3] == "nine":
#         calibrations.append('9')
#       if i[j] + i[j + 1] + i[j + 2] + i[j + 3] == "zero":
#         calibrations.append('0')
#       if i[j] + i[j + 1] + i[j + 2] + i[j + 3] + i[j + 4] == "three":
#         calibrations.append('3')
#       if i[j] + i[j + 1] + i[j + 2] + i[j + 3] + i[j + 4] == "seven":
#         calibrations.append('7')
#       if i[j] + i[j + 1] + i[j + 2] + i[j + 3] + i[j + 4] == "eight":
#         calibrations.append('8')

#     except:
#       continue
#   currentCalibration = calibrations[0] + calibrations[-1]
#   totalCalibrations += int(currentCalibration)
#   calibrations.clear()
  
#   currentCalibration = ''

# print(totalCalibrations)




#DAY 2
# totalID = 0

# powerTotal = 0
# games = []
# for x in range(1, 101):
#   games.append(x)

# for i in contents:
#   minSet = []
#   maxGreen = 0
#   maxRed = 0
#   maxBlue = 0
#   power = 1
#   lenGameSubstring = i.find(':')
#   if lenGameSubstring == 6:
#     gameNumber = int(i[5])
#   elif lenGameSubstring == 7:
#     gameNumber = int(i[5] + i[6])
#   elif lenGameSubstring == 8:
#     gameNumber = int(i[5] + i[6] + i[7])
    
#   else:
#     continue
  
  
#   sets = i.split(';')
#   firstSet = sets[0].split(':')
#   del firstSet[0]
#   del sets[0]
#   sets.append(''.join(firstSet))
#   for j in sets:
#     contents = j.split(',')
#     for item in contents:
#       colourAndNum = item.split(' ')
#       numColours = int(colourAndNum[1])
#       colour = colourAndNum[2]
#       if colour == 'red':
#         if numColours >= maxRed:
#           maxRed = numColours
#         # if numColours > 12:
#         #   if gameNumber in games:
#         #     games.remove(gameNumber)
#         # else:
#         #   continue
        
#       elif colour == 'green':
#         if numColours >= maxGreen:
#           maxGreen = numColours
#         # if numColours > 13:
#         #   if gameNumber in games:
#         #     games.remove(gameNumber)
#       elif colour == 'blue':
#         if numColours >= maxBlue:
#           maxBlue = numColours
#         # if numColours > 14:
#         #   if gameNumber in games:
#         #     games.remove(gameNumber)
#       else:
#         continue
#   max = [maxBlue, maxGreen, maxRed]
#   minSet.extend(max)
#   for m in max:
#     power = power * m
#   powerTotal += power

# for y in games:
#   totalID += y

#DAY 3
#Part 1 - the file was modified so this program will not work on the original file
# sum = 0
# digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

# for i in range(len(contents)):
#   for j in range(len(contents[i])):
#     if contents[i][j] in digits and contents[i][j + 1] in digits and contents[i][j + 2] in digits:
#       if contents[i][j-1] != '.' or contents[i][j + 3] != '.' or contents[i + 1][j - 1] != '.' or contents[i + 1][j] != '.' or contents[i + 1][j + 1] != '.' or contents[i + 1][j + 2] != '.' or contents[i + 1][j + 3] != '.' or contents[i - 1][j - 1] != '.' or contents[i - 1][j] != '.' or contents[i - 1][j + 1] != '.' or contents[i - 1][j + 2] != '.' or contents[i - 1][j + 3] != '.':
#         sum += int(contents[i][j] + contents[i][j + 1] + contents[i][j + 2])
#     elif contents[i][j] in digits and contents[i][j + 1] in digits and contents[i][j + 2] not in digits and contents[i][j - 1] not in digits:
#       if contents[i][j-1] != '.' or contents[i][j + 2] != '.' or contents[i + 1][j - 1] != '.' or contents[i + 1][j] != '.' or contents[i + 1][j + 1] != '.' or contents[i + 1][j + 2] != '.' or contents[i - 1][j - 1] != '.' or contents[i - 1][j] != '.' or contents[i - 1][j + 1] != '.' or contents[i - 1][j + 2] != '.':
#         sum += int(contents[i][j] + contents[i][j + 1])
#     elif contents[i][j] in digits and contents[i][j-1] not in digits and contents[i][j+1] not in digits:
#       if contents[i][j-1] != '.' or contents[i][j+1] != '.' or contents[i-1][j-1] != '.' or contents[i-1][j] != '.' or contents[i-1][j+1] != '.' or contents[i+1][j-1] != '.' or contents[i+1][j] != '.' or contents[i+1][j+1] != '.':
#         sum += int(contents[i][j])
#     else:
#       continue
#   print(sum)

#Part 2
# sumGearRatios = 0

# def productList(ls):
#   product = 1
#   for item in ls:
#     product = product * item
#   return product
    
# for i in range(len(contents)):
#   for j in range(len(contents[i])):
#     if contents[i][j] == '*':
#       partNums = []
#       numNums = 0
#       above = ''
#       below = ''
#       for x in range(-3, 4):
#         above += contents[i - 1][j + x]
#         below += contents[i + 1][j + x]
#       left = contents[i][j - 3] + contents[i][j - 2] + contents[i][j - 1]
#       right = contents[i][j + 1] + contents[i][j + 2] + contents[i][j + 3]
#       if above[0].isdigit() and above[1].isdigit() and above[2].isdigit():
#         numNums += 1
#         partNums.append(int(above[0] + above[1] + above[2]))
#       if above[2].isdigit() and not above[1].isdigit() and not above[3].isdigit():
#         numNums += 1
#         partNums.append(int(above[2]))
#       if above[3].isdigit() and not above[2].isdigit() and not above[4].isdigit():
#         numNums += 1
#         partNums.append(int(above[3]))
#       if above[4].isdigit() and not above[3].isdigit() and not above[5].isdigit():
#         numNums += 1
#         partNums.append(int(above[4]))
#       if above[1].isdigit() and above[2].isdigit() and above[3].isdigit():
#         numNums += 1
#         partNums.append(int(above[1] + above[2] + above[3]))
#       if above[2].isdigit() and above[3].isdigit() and above[4].isdigit():
#         numNums += 1
#         partNums.append(int(above[2] + above[3] + above[4]))
#       if above[3].isdigit() and above[4].isdigit() and above[5].isdigit():
#         numNums += 1
#         partNums.append(int(above[3] + above[4] + above[5]))
#       if above[4].isdigit() and above[5].isdigit() and above[6].isdigit():
#         numNums += 1
#         partNums.append(int(above[4] + above[5] + above[6]))
#       if above[1].isdigit() and above[2].isdigit() and not above[0].isdigit() and not above[3].isdigit():
#         numNums += 1
#         partNums.append(int(above[1] + above[2]))
#       if above[2].isdigit() and above[3].isdigit() and not above[1].isdigit() and not above[4].isdigit():
#         numNums += 1
#         partNums.append(int(above[2] + above[3]))
#       if above[3].isdigit() and above[4].isdigit() and not above[2].isdigit() and not above[5].isdigit():
#         numNums += 1
#         partNums.append(int(above[3] + above[4]))
#       if above[4].isdigit() and above[5].isdigit() and not above[3].isdigit() and not above[6].isdigit():
#         numNums += 1
#         partNums.append(int(above[4] + above[5]))
#       if below[0].isdigit() and below[1].isdigit() and  below[2].isdigit():
#         numNums += 1
#         partNums.append(int(below[0] + below[1] + below[2]))
#       if below[1].isdigit() and below[2].isdigit() and below[3].isdigit():
#         numNums += 1
#         partNums.append(int(below[1] + below[2] + below[3]))
#       if below[2].isdigit() and below[3].isdigit() and below[4].isdigit():
#         numNums += 1
#         partNums.append(int(below[2] + below[3] + below[4]))
#       if below[3].isdigit() and below[4].isdigit() and below[5].isdigit():
#         numNums += 1
#         partNums.append(int(below[3] + below[4] + below[5]))
#       if below[4].isdigit() and below[5].isdigit() and below[6].isdigit():
#         numNums += 1
#         partNums.append(int(below[4] + below[5] + below[6]))
#       if below[1].isdigit() and below[2].isdigit() and not below[0].isdigit() and not below[3].isdigit():
#         numNums += 1
#         partNums.append(int(below[1] + below[2]))
#       if below[2].isdigit() and below[3].isdigit() and not below[1].isdigit() and not below[4].isdigit():
#         numNums += 1
#         partNums.append(int(below[2] + below[3]))
      
#       if below[3].isdigit() and below[4].isdigit() and not below[2].isdigit() and not below[5].isdigit():
#         numNums += 1
#         partNums.append(int(below[3] + below[4]))
#       if below[4].isdigit() and below[5].isdigit() and not below[3].isdigit() and not below[6].isdigit():
#         numNums += 1
#         partNums.append(int(below[4] + below[5]))
#       if below[2].isdigit() and not below[1].isdigit() and not below[3].isdigit():
#         numNums += 1
#         partNums.append(int(below[2]))
#       if below[3].isdigit() and not below[2].isdigit() and not below[4].isdigit():
#         numNums += 1
#         partNums.append(int(below[3]))
#       if below[4].isdigit() and not below[3].isdigit() and not below[5].isdigit():
#         numNums += 1
#         partNums.append(int(below[4]))
#       if left[0].isdigit() and left[1].isdigit() and left[2].isdigit():
#         numNums += 1
#         partNums.append(int(left[0] + left[1] + left[2]))
#       if right[0].isdigit() and right[1].isdigit() and right[2].isdigit():
#         numNums += 1
#         partNums.append(int(right[0] + right[1] + right[2]))
#       if left[1].isdigit() and left[2].isdigit() and not left[0].isdigit():
#         numNums += 1
#         partNums.append(int(left[1] + left[2]))
#       if right[0].isdigit() and right[1].isdigit() and not right[2].isdigit():
#         numNums += 1
#         partNums.append(int(right[0] + right[1]))
#       if left[2].isdigit() and not left[1].isdigit() and not left[0].isdigit():
#         numNums += 1
#         partNums.append(int(left[2]))
#       if right[0].isdigit() and not right[1].isdigit() and not right[2].isdigit():
#         numNums += 1
#         partNums.append(int(right[0]))
#       print(i + 1, partNums)
#       if numNums == 2:
#         gearRatio = productList(partNums)
#         sumGearRatios += gearRatio

# print(sumGearRatios)


#DAY 4

# totalPoints = 0
# copies = []

# for card in contents:
#   myWinningNums = 0
#   lenCardSubstring = card.find(':')
#   if lenCardSubstring == 6:
#     cardNumber = int(card[5])
#   elif lenCardSubstring == 7:
#     cardNumber = int(card[5] + card[6])
#   elif lenCardSubstring == 8:
#     cardNumber = int(card[5] + card[6] + card[7])
#   else:
#     continue
  
#   sets = card.split('|')
#   winningNums = sets[0].split()
#   del winningNums[0:2]
#   myNums = sets[1].split()
#   for num in myNums:
#     if num in winningNums:
#       myWinningNums += 1
#   if myWinningNums > 0:
#     for i in range(1, myWinningNums + 1):
#       contents.append(contents[cardNumber - 1 + i])
#   else:
#     continue
#   #part1
#   # if myWinningNums > 0:
#   #   points = pow(2, myWinningNums - 1)
#   # else:
#   #   points = 0
#   # totalPoints += points
# print(len(contents))

#DAY 5

