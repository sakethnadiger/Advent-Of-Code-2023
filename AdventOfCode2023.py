
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

 
# seeds = [int(seed) for seed in contents[0][7:].split(' ')]

# mapsList = contents[2:]
# maps = []
# temp = []
# for i in mapsList:
  
#   if len(i) != 0:
#     temp.append(i)
#   else:
#     del temp[0]
#     maps.append(temp)
#     temp = []

# del temp[0]
# maps.append(temp)
# for x in maps:
#   for idj, j in enumerate(x):
#     splitmap = [int(y) for y in str(j).split()]
#     x[idj] = splitmap
    
# newSeeds = []
# for t, u in enumerate(seeds):
#   if t % 2 == 0:
#     newSeedRange = [b for b in range(u, u + seeds[t + 1])]
#     newSeeds.extend(newSeedRange)
    

# items = seeds
# for m in maps:
#   newseeds = []
#   for v in items:
#     newv = v
#     for destsourceranvals in m:
#       dest = destsourceranvals[0]
#       source = destsourceranvals[1]
#       ran = destsourceranvals[2]
#       difference = v - source
#       if source <= v < source + ran:
#         newv = difference + dest
#         print(newv)
#         break
#     newseeds.append(newv)
#     print(newseeds)
#   items = newseeds



#Not completed

#DAY 6


# times = contents[0].split()
# del times[0]
# part2times = ''
# for time in times:
#   part2times += time

# part2times = int(part2times)

# def findBonds(num):
#   ls = []
#   for i in range(num + 1):
#     temp = [i, num - i]
#     ls.append(temp)
#   return ls


# records = contents[1].split()
# del records[0]
# part2record = ''
# for record in records:
#   part2record += record

# part2record = int(part2record)




# #combinations = []

# # for i, time in enumerate(times):
# #   combosAboveRecord = 0
# #   bonds = findBonds(int(time))
# #   for pair in bonds:  
# #     distance = pair[0] * pair[1]
# #     if distance > int(records[i]):
# #       combosAboveRecord += 1
# #   combinations.append(combosAboveRecord)
  
# combosAboveRecord = 0
# bonds = findBonds(part2times)


# for pair in bonds:
#   distance = pair[0] * pair[1]
#   if distance > part2record:
#     part2 = (pair[1] - pair[0]) + 1
#     break
  
# print(part2)
# # part1 = 1
# # for c in combinations:
# #   part1 *= c

# # print(part1)
    
#DAY 7

# handBid = {}
# #This code may not do anything
# def get_nth_key(dictionary, n=0):
#   if n < 0:
#     n += len(dictionary)
#   for i, key in enumerate(dictionary.keys()):
#     if i == n:
#       return key
#   raise IndexError("dictionary index out of range")

# def findType(myHands):
#   types = []
#   for i in myHands:
#     if len(set(i)) == len(i):
#       if 'J' in i:
#         types.append('OnePair')
#       else:
#         types.append('High')
#     counts = {j: i.count(j) for j in i}
#     dupecounter = 0
#     triplePresent = False
#     quadPresent = False
#     allSame = False
#     for x in counts:
#       if counts[x] == 2:
#         dupecounter += 1
#       if counts[x] == 3:
#         triplePresent = True
#       if counts[x] == 4:
#         quadPresent = True
#     if len(counts) == 1:
#       allSame = True
#     if dupecounter == 1:
#       if triplePresent:
#         if 'J' not in counts:
#           types.append('FullHouse')
#         else:
#           if counts['J'] == 2:
#             types.append('Five')
#           if counts['J'] == 3:
#             types.append('Five')
#       else:
#         if 'J' in counts:
#           types.append('Three')
#         else:
#           types.append('OnePair')
#     elif dupecounter == 2:
#       if 'J' in counts:
#         if counts['J'] == 2:
#           types.append('Four')
#         if counts['J'] == 1:
#           types.append('FullHouse')
#       else:
#         types.append('TwoPair')
#     else:
#       if triplePresent:
#         if 'J' in counts:
#           types.append('Four')
#         else:
#           types.append('Three')
#       if quadPresent:
#         if 'J' in counts:
#           types.append('Five')
#         else:
#           types.append('Four')
#       if allSame:
#         types.append('Five')
#     print(i)
#   return types


# vals = {
#   "A":14,
#   "K":13,
#   "Q":12, 
#   "J":1,
#   "T":10,
#   "9":9,
#   "8":8,
#   "7":7,
#   "6":6,
#   "5":5,
#   "4":4,
#   "3":3,
#   "2":2
  
# }

# hands = []
# for i in contents:
#   hand, bid = i.split()
#   hands.append(hand)
#   handBid[hand] = int(bid)

# types = findType(hands)
# print(types)

# strengthsList = []
# for hand in hands:
#   strengthHand = []
#   for card in hand:
#     strengthHand.append(vals[card])
#   strengthsList.append(strengthHand)


# for idb, b in enumerate(hands):
#   print(b, types[idb])

# highs = []
# ones = []
# twos = []
# threes = []
# fullhouse = []
# fours = []
# fives = []

# for idh, h in enumerate(strengthsList):
#   correspondingType = types[idh]
#   if correspondingType == 'High':
#     highs.append(h)
#   if correspondingType == 'FullHouse':
#     fullhouse.append(h)
#   if correspondingType == 'OnePair':
#     ones.append(h)
#   if correspondingType == 'TwoPair':
#     twos.append(h)
#   if correspondingType == 'Three':
#     threes.append(h)
#   if correspondingType == 'Four':
#     fours.append(h)
#   if correspondingType == 'Five':
#     fives.append(h)

# allCards = [highs, ones, twos, threes, fullhouse, fours, fives]

# for cardSet in allCards:
#   cardSet.sort(reverse=True)

# allCards.reverse()
# flatList = [j for subList in allCards for j in subList]



# reversedVals = {
#   14: "A",
#   13: "K",
#   12: "Q",
#   1: "J",
#   10: "T",
#   9: "9",
#   8: "8",
#   7: "7",
#   6: "6",
#   5: "5",
#   4: "4",
#   3: "3",
#   2: "2",
# }

# OGHands = []
# for ids, s in enumerate(flatList):
#   OGHand = []
  
#   for v in s:
#     OGHand.append(reversedVals[v])
#   OGHands.append(OGHand)

# total = 0
# for index, OG in enumerate(OGHands):
#   myHandInString = OG[0] + OG[1] + OG[2] + OG[3] + OG[4]
#   winning = ((len(OGHands) + 1) - (index + 1)) * handBid[myHandInString]
#   total += winning  
  
# print(total)

#Day 8 - only part 1 completed

# instruction = [i for i in contents[0]]
# del contents[0]
# del contents[0]
# def findPos(node):
#   for i in range(len(contents)):
#     if contents[i][0:3] == node:
#       pos = i
#   return pos
# startpos = findPos('AAA')


# foundZZZ = False

# currentLine = contents[startpos]
# path = []
# while foundZZZ == False:
#   for inst in instruction:
#     if inst == 'R':
#       if currentLine[12:15] == 'ZZZ':
#         foundZZZ = True
#       next = findPos(currentLine[12:15])
#     if inst == 'L':
#       if currentLine[7:10] == 'ZZZ':
#         foundZZZ = True
#       next = findPos(currentLine[7:10])
#     currentLine = contents[next]
#     path.append(currentLine)
# print(len(path))

#Day 9 - part 2 was a small modification of part 1

# extrapolatedValTotals = 0
# for sequence in contents:
#   currentSequence = [int(i) for i in sequence.split()]
#   differences = []
#   currentDiff = currentSequence
#   diffResolved = False
#   while diffResolved is False:
#     newDiff = []
#     for b in range(6):
#       for val in range(len(currentDiff)):
#         try:
#           newDiff.append(currentDiff[val + 1] - currentDiff[val])
#         except:
#           continue
#       differences.append(newDiff)
#       currentDiff = newDiff
#       newDiff = []
#       if set(currentDiff) == {0}:
#         diffResolved = True
#         break
#   differences.reverse()
#   for diff in range(len(differences)):
#     try:
#       differences[diff + 1].append(differences[diff + 1][0] - differences[diff][-1])
#     except:
#       continue
#   differences.append(currentSequence)
#   extrapolatedVal = currentSequence[0] - differences[-2][-1]
#   extrapolatedValTotals += extrapolatedVal
# print(extrapolatedValTotals)

#Day 15 Completed
# with open('myfile.txt') as f:
#   contents = f.read()

# strings = contents.split(',')

# def findVal(string):
#   currentVal = 0
#   for character in string:
#     currentVal += ord(character)
#     currentVal *= 17
#     currentVal %= 256
#   return currentVal

# totalVal = 0

# for i in strings:
#   totalVal += findVal(i)
  
# print(totalVal)

# with open('myfile.txt') as f:
#   contents = f.read()

# strings = contents.split(',')
# def findVal(string):
#   currentVal = 0
#   for character in string:
#     currentVal += ord(character)
#     currentVal *= 17
#     currentVal %= 256
#   return currentVal

# boxes = [[] for _ in range(256)]

# for s in strings:
#   if '=' in s:
#     label, focalLength = s.split('=')
#     boxNum = findVal(label)
#     if [label] in boxes[boxNum]:
#       positionLabel = boxes[boxNum].index([label])
#       boxes[boxNum][positionLabel + 1] = [focalLength]
#     else:
#       boxes[boxNum].append([label])
#       boxes[boxNum].append([focalLength])
#   if '-' in s:
#     label = s.split('-')[0]
#     boxNum = findVal(label)
#     if [label] in boxes[boxNum]:
#       positionLabel = boxes[boxNum].index([label])
#       boxes[boxNum].pop(positionLabel + 1)
#       boxes[boxNum].pop(positionLabel)

# totalFocusingPower = 0
# for box in range(len(boxes)):
#   boxNumber = box + 1
#   if len(boxes[box]) > 0:
#     counter = 0
#     for labelAndFocus in range(len(boxes[box])):
#       if labelAndFocus % 2 == 0:
#         counter += 1
#         labelSlot = counter
#         focalLengthNum = int(boxes[box][labelAndFocus + 1][0])
#         currentFocusingPower = boxNumber * labelSlot * focalLengthNum
#         totalFocusingPower += currentFocusingPower
#   else:
#     continue

# print(totalFocusingPower)

#Day 10 Part 1 Completed
# graph = [[] for l in contents]

# for lineNum in range(len(contents)):
#   for item in contents[lineNum]:
#     graph[lineNum].append([item])

# for x in range(len(graph)):
#   if ['S'] in graph[x]:
#     startPosition = [x, graph[x].index(['S'])]
    

# currentPos = startPosition

# possibleConnectors_N = {'|': ['|', 'F', '7', 'S'], '-': None, 'L': ['|', 'F', '7', 'S'], 'J': ['|', 'F', '7', 'S'], '7': None, 'F' : None}
# possibleConnectors_S = {'|': ['|', 'J', 'L', 'S'], '-': None, 'L': None, 'J': None, '7': ['|', 'J', 'L', 'S'], 'F' : ['|', 'J', 'L', 'S']}
# possibleConnectors_E = {'|': None, '-': ['J', '7', '-', 'S'], 'L': ['J', '7', '-', 'S'], 'J': None, '7': None, 'F' : ['J', '7', '-', 'S']}
# possibleConnectors_W= {'|': None, '-': ['F', 'L', '-', 'S'], 'L': None, 'J': ['F', 'L', '-', 'S'], '7': ['F', 'L', '-', 'S'], 'F' : None}



# if graph[currentPos[0] - 1][currentPos[1]][0] in ['|', 'F', '7']:
#   currentPos = [currentPos[0] - 1, currentPos[1]]
# elif graph[currentPos[0] + 1][currentPos[1]][0] in ['|', 'J', 'L']:
#   print("yes")
#   currentPos = [currentPos[0] + 1, currentPos[1]]
# elif graph[currentPos[0]][currentPos[1] - 1][0] in ['-', 'F', 'L']:
#   currentPos = [currentPos[0], currentPos[1] - 1]
# elif graph[currentPos[0]][currentPos[1] + 1][0] in ['-', 'J', '7']:
#   currentPos = [currentPos[0], currentPos[1] + 1]

# prevPos = startPosition
# notLooped = graph[currentPos[0]][currentPos[1]] == ['S']

# print(currentPos)
# count = 0
# while graph[currentPos[0]][currentPos[1]] != ['S']:
#   count += 1
#   print(graph[currentPos[0]][currentPos[1]])
#   if graph[currentPos[0]][currentPos[1]][0] == '|':
#     if graph[currentPos[0] - 1][currentPos[1]][0] == 'S' and [currentPos[0] - 1, currentPos[1]] != prevPos:
#       notLooped = True
#       break
#     if graph[currentPos[0] + 1][currentPos[1]][0] == 'S' and [currentPos[0] + 1, currentPos[1]] != prevPos:
#       notLooped = True
#       break
#     if graph[currentPos[0] - 1][currentPos[1]][0] in possibleConnectors_N[graph[currentPos[0]][currentPos[1]][0]] and [currentPos[0] - 1, currentPos[1]] != prevPos:
#       prevPos = currentPos
#       currentPos = [currentPos[0] - 1,currentPos[1]]

#     elif graph[currentPos[0] + 1][currentPos[1]][0] in possibleConnectors_S[graph[currentPos[0]][currentPos[1]][0]] and [currentPos[0] + 1, currentPos[1]] != prevPos:
#       prevPos = currentPos
#       currentPos = [currentPos[0] + 1,currentPos[1]]
      
#   elif graph[currentPos[0]][currentPos[1]][0] == '-':
#     if graph[currentPos[0]][currentPos[1] - 1][0] == 'S' and [currentPos[0], currentPos[1] - 1] != prevPos:
#       notLooped = True
#       break
#     if graph[currentPos[0]][currentPos[1] + 1][0] == 'S' and [currentPos[0], currentPos[1] + 1] != prevPos:
#       notLooped = True
#       break
#     if graph[currentPos[0]][currentPos[1] - 1][0] in possibleConnectors_W[graph[currentPos[0]][currentPos[1]][0]] and [currentPos[0], currentPos[1] - 1] != prevPos:
#       prevPos = currentPos
#       currentPos = [currentPos[0],currentPos[1] - 1]
      
#     elif graph[currentPos[0]][currentPos[1] + 1][0] in possibleConnectors_E[graph[currentPos[0]][currentPos[1]][0]] and [currentPos[0], currentPos[1] + 1] != prevPos:
#       prevPos = currentPos
#       currentPos = [currentPos[0],currentPos[1] + 1]
      
#   elif graph[currentPos[0]][currentPos[1]][0] == 'F':
#     if graph[currentPos[0] + 1][currentPos[1]][0] == 'S' and [currentPos[0] + 1, currentPos[1]] != prevPos:
#       notLooped = True
#       break
#     if graph[currentPos[0]][currentPos[1] + 1][0] == 'S' and [currentPos[0], currentPos[1] + 1] != prevPos:
#       notLooped = True
#       break
#     if graph[currentPos[0] + 1][currentPos[1]][0] in possibleConnectors_S[graph[currentPos[0]][currentPos[1]][0]] and [currentPos[0] + 1, currentPos[1]] != prevPos:
#       prevPos = currentPos
#       currentPos = [currentPos[0] + 1,currentPos[1]]
      
#     elif graph[currentPos[0]][currentPos[1] + 1][0] in possibleConnectors_E[graph[currentPos[0]][currentPos[1]][0]] and [currentPos[0], currentPos[1] + 1] != prevPos:
#       prevPos = currentPos
#       currentPos = [currentPos[0],currentPos[1] + 1]
      
#   elif graph[currentPos[0]][currentPos[1]][0] == '7':
#     if graph[currentPos[0] + 1][currentPos[1]][0] == 'S' and [currentPos[0] + 1, currentPos[1]] != prevPos:
#       notLooped = True
#       break
#     if graph[currentPos[0]][currentPos[1] - 1][0] == 'S' and [currentPos[0], currentPos[1] - 1] != prevPos:
#       notLooped = True
#       break
#     if graph[currentPos[0] + 1][currentPos[1]][0] in possibleConnectors_S[graph[currentPos[0]][currentPos[1]][0]] and [currentPos[0] + 1, currentPos[1]] != prevPos:
#       prevPos = currentPos
#       currentPos = [currentPos[0] + 1,currentPos[1]]
    
#     elif graph[currentPos[0]][currentPos[1] - 1][0] in possibleConnectors_W[graph[currentPos[0]][currentPos[1]][0]] and [currentPos[0], currentPos[1] - 1] != prevPos:
#       prevPos = currentPos
#       currentPos = [currentPos[0],currentPos[1] - 1]
      
#   elif graph[currentPos[0]][currentPos[1]][0] == 'L':
#     if graph[currentPos[0]][currentPos[1] + 1][0] == 'S' and [currentPos[0], currentPos[1] + 1] != prevPos:
#       notLooped = True
#       break
#     if graph[currentPos[0] - 1][currentPos[1]][0] == 'S' and [currentPos[0] - 1, currentPos[1]] != prevPos:
#       notLooped = True
#       break
#     if graph[currentPos[0] - 1][currentPos[1]][0] in possibleConnectors_N[graph[currentPos[0]][currentPos[1]][0]] and [currentPos[0] - 1, currentPos[1]] != prevPos:
#       prevPos = currentPos
#       currentPos = [currentPos[0] - 1,currentPos[1]]
      
#     elif graph[currentPos[0]][currentPos[1] + 1][0] in possibleConnectors_E[graph[currentPos[0]][currentPos[1]][0]] and [currentPos[0], currentPos[1] + 1] != prevPos:
#       prevPos = currentPos
#       currentPos = [currentPos[0],currentPos[1] + 1]
      
#   elif graph[currentPos[0]][currentPos[1]][0] == 'J':
#     if graph[currentPos[0]][currentPos[1] - 1][0] == 'S' and [currentPos[0], currentPos[1] - 1] != prevPos:
#       notLooped = True
#       break
#     if graph[currentPos[0] - 1][currentPos[1]][0] == 'S' and [currentPos[0] - 1, currentPos[1]] != prevPos:
#       notLooped = True
#       break
#     if graph[currentPos[0] - 1][currentPos[1]][0] in possibleConnectors_N[graph[currentPos[0]][currentPos[1]][0]] and [currentPos[0] - 1, currentPos[1]] != prevPos:
#       prevPos = currentPos
#       currentPos = [currentPos[0] - 1,currentPos[1]]
      
#     elif graph[currentPos[0]][currentPos[1] - 1][0] in possibleConnectors_W[graph[currentPos[0]][currentPos[1]][0]] and [currentPos[0], currentPos[1] - 1] != prevPos:
#       prevPos = currentPos
#       currentPos = [currentPos[0],currentPos[1] - 1]


# furthest = (count // 2) + 1
# print(furthest)

#Day 14 Part 1

# grid = []
# for i in contents:
#   temp = []
#   for j in i:
#     temp.append(j)
#   grid.append(temp)

# rocks = []
# for i in range(len(grid)):
#   for j in range(len(grid[i])):
#     if grid[i][j] == "O":
#       rocks.append((i, j))




# for rock in rocks:
#   if rock[0] == 0:
#     continue
#   else:
#     current = rock
#     while (grid[current[0] - 1][current[1]] not in ['O', '#']) and current[0] - 1 >= 0:
#       grid[current[0] - 1][current[1]] = 'O'
#       grid[current[0]][current[1]] = '.'
#       current = (current[0] - 1, current[1])

# totalLoad = 0
# for rowNum in range(len(grid)):
#   numRocksInRow = grid[rowNum].count('O')
#   currentLoad = numRocksInRow * (len(grid) - rowNum)
#   totalLoad += currentLoad

# print(totalLoad)
  
