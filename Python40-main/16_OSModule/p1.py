import os

# getCurrentWorkingDirectory
# print(os.getcwd())  # /Users/sajeedsaif/Documents/DL Classes/Python40/16_OSModule

# makeDirectory
# os.mkdir('FolderOne')

# makeSubDirectory/
# os.mkdir('FolderOne/SubFolderOne')

# makeDirectory and inside of Directory make one more Directory
# os.makedirs('FolderTwo/SubFolderTwo')

# rename the existing folder
# os.rename('FolderOne', 'RenameFolderOne')

# makeDirectory
# os.mkdir('FolderThree')

# removeDirectory
# os.rmdir('FolderThree')

# remove subdirectory
# os.rmdir('RenameFolderOne/SubFolderOne')

# remove directory and subdirectory
# os.removedirs('FolderTwo/SubFolderTwo')

# absolute path
# os.mkdir('E:\\FolderOne\\Python')
# os.mkdir('/Users/sajeedsaif/Documents/DL Classes/Python40/01_Fundamentals/FolderOne')

# change dir
# os.chdir('/Users/sajeedsaif/Documents/DL Classes/Python40/01_Fundamentals/FolderOne')
# print(os.getcwd())  # /Users/sajeedsaif/Documents/DL Classes/Python40/01_Fundamentals/FolderOne

# list dir
o = os.listdir()
print(o)



