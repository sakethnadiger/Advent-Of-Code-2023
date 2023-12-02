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
