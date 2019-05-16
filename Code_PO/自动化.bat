@echo off
echo 按任意键开始
pause
echo 自动化测试执行中....

#添加路径
python ..\Code_PO\case\test_case.py

echo 按任意键结束 自动关闭当前测试.bat
pause
exit

