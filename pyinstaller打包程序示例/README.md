#有控制台 一个文件 图标
pyinstaller -c -F x.py -i favo.ico 

-c 打包生成的可执行文件以控制台应用程序的形式运行，
	而不是以图形界面应用程序的形式运行。

-w 相当于--noconsole，表示去掉控制台窗口，这在GUI界面时非常有用。
用于创建一个窗口应用程序而不是控制台应用程序。

-F 缩写形式是-F，相当于--onefile，用于生成一个单一的可执行文件。运行速度慢，不建议

-p 表示你自己自定义需要加载的类路径，一般情况下用不到

-i 相当于--icon，用于指定可执行文件的图标。

pyinstaller -i icon.ico your_script.py

pyinstaller -n your_app your_script.py

# 无命令行，多个文件
pyinstaller -w gui-hello.py -i ./logo.png
# 命令行，多个文件
pyinstaller -c hello.py -i ./logo.png