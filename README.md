# Codeforces-test-cases

After Cloning run pip install requirements.txt


Made this to avoid copy pasting the test cases and validating them one by one when we have python at our disposal.

Assumptions :
1. It will make an Input folder , so make sure you are not using such a folder
2. It will make Ouput folder , so make sure you are not using such a folder
3. It will make file output_expected.txt so make sure you don't use the file which is named same
4. If multiple output can be there for an output it obviously won't work.


Changes you need to make : 
1. In line 61 you need to write whatever command you use to execute your code. eg for my case it's : g++ a.cpp -o a
    so you write the command accordingly in the code.
2. In line 67 where you pipe the output to the output_expected.txt you need to write the command that works for your program to run. for eg ./a (where a.exe is the executable file).

Usage:
After writing the code just copy the url of the problem you are working on. for eg : https://codeforces.com/contest/1370/problem/D.

Then type on terminal -> run.py https://codeforces.com/contest/1370/problem/D 

That's it

Changes and issues are welcomed, want to see how much can it be improved
