#! python3
# 假定你的老板用电子邮件发给你上千个文件，文件名包含美国风格的日期 (MM-DD-YYYY)，需要将它们改名为欧洲风格的日期(DD-MM-YYYY)。
# 手工完成这个无聊的任务可能需要几天时间!让我们写一个程序来完成它。
import shutil, os, re
datePattern = re.compile(r"""^(.*?)((0|1)?\d)-((0|1|2|3)?\d)-((19|20)\d\d)(.*?)$ """, re.VERBOSE)
for amerFilename in os.listdir('.'):
    mo = datePattern.search(amerFilename)
    if mo == None:
        continue
    beforePart = mo.group(1)
    monthPart = mo.group(2)
    dayPart = mo.group(4)
    yearPart = mo.group(6)
    afterPart = mo.group(8)
    euroFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart
    shutil.move(amerFilename,euroFilename)
    absWorkingDir = os.path.abspath('.')
    amerFilename = os.path.join(absWorkingDir, amerFilename)
    euroFilename = os.path.join(absWorkingDir, euroFilename)
    print("把美国风格日期'%s'改变为欧洲风格日期'%s'" % (amerFilename,euroFilename ))