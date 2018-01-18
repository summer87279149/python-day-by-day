#! python3
# .pyw 扩展名意味着 Python 运行该程序时，不会显示终端窗口
# 假定你有一个无聊的任务，要填充一个网页或软件中的许多表格，其中包含一 些文本字段。
# 剪贴板让你不必一次又一次输入同样的文本，但剪贴板上一次只有一 个内容。
# 如果你有几段不同的文本需要拷贝粘贴，就不得不一次又一次的标记和拷 贝几个同样的内容。

# 下面是程序要做的事:
# 针对要检查的关键字，提供命令行参数。
# 如果参数是 save，那么将剪贴板的内容保存到关键字。
# 如果参数是 list，就将所有的关键字拷贝到剪贴板。
# 否则，就将关键词对应的文本拷贝到剪贴板。

# 使用:
# python multiclipboard.pyw save <keyword>
# python multiclipboard.pyw <keyword>
import shelve, pyperclip, sys
mcbShelf = shelve.open('multiclipboard')
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])