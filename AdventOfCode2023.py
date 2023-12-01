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
