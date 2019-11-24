# IMPORTS
from readCSV import open_and_read_CSV
from getColumns import getColumns
from getUnique import getUnique

# 1 # Get User's .csv Data
# 1.1 # Create Prompt
userInputPrompt = f'Please enter the absolute file path for your downloaded .cvs \n'
userInputPrompt += f'Note: This can be found by dragging the file from your downloads and dropping it into your terminal\n'
userInputPrompt += f'Enter File Path Here:  '

# 1.2 # Send Prompt
userFilePath = input(userInputPrompt)
print('User Entered Absolute File Path: ',userFilePath, type(userFilePath))

# 2 # Open & Read .csv Data --> returns List
userFile = open_and_read_CSV(userFilePath)
# print('__mainFunction__: userFile',userFile)
print('__mainFunction__: readCSV type == ', type(userFile), len(userFile))

# 3 # Filter For Specific Columns
userFile = getColumns(userFile)
print('__mainFunction__: Filtered UserFile type == ', type(userFile), len(userFile))

# 4 # Get Unique Students
uniqueStudent = getUnique(userFile)
print('__mainFunction__: uniqueStudent type == ', type(uniqueStudent), len(uniqueStudent))




