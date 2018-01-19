#! python3
# 假定你正在做一个项目，它的文件保存在 C:\AlsPythonBook 文件夹中。
# 你担心工作 会丢失，所以希望为整个文件夹创建一个 ZIP 文件，作为“快照”
# 。你希望保存不同的版 本，希望 ZIP 文件的文件名每次创建时都有所变化。
# 例如 AlsPythonBook_1.zip、 AlsPythonBook_2.zip、AlsPythonBook_3.zip，等等。
# 你可以手工完成，但这有点烦人， 而且可能不小心弄错 ZIP 文件的编号。
# 运行一个程序来完成这个烦人的任务会简单得多。
import zipfile, os


def backupToZip(folder):
    folder = os.path.abspath(folder)
    number = 1
    while True:
        zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipFilename):
            break
        number = number + 1
    print('Creating %s...' % (zipFilename))
    backupZip = zipfile.ZipFile(zipFilename, 'w')
    for foldername, subfolders, filenames in os.walk(folder):

        print('foldername %s,  \n subfolders=%s\n filenames=%s...' % (foldername,subfolders,filenames))
        backupZip.write(foldername)
        for filename in filenames:
            newBase = os.path.basename(folder) + '_'
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue
            backupZip.write(os.path.join(foldername, filename))
    backupZip.close()
    print('Done.')


backupToZip('/Users/mc/Desktop/python-day-by-day')
