import requests
import shutil
from bs4 import BeautifulSoup
import os
import sys

def get_test_cases(URL):

    # Scrape codeforces for test cases
    page = requests.get(URL)
    soup = BeautifulSoup(page.content,'html.parser')
    test_cases_tag = soup.find_all('pre')

    # Data cleaning
    test_cases = []
    result = []
    for i in range(0,len(test_cases_tag)):
        if not i&1 :
            test_cases.append(test_cases_tag[i].text.strip())
        else :
            result.append(test_cases_tag[i].text.strip())  

    # Deleting the Input folder 
    try:
        shutil.rmtree('./Input')
    except:
        print("No Input Directory Proceeding") 

    # Deleting Ouput folder
    try:
        shutil.rmtree('./Output')
    except:
        print("No Output Directory Proceeding") 


    # Making the folder again
    os.mkdir('./Input')
    os.mkdir('./Output')

    # Write the input test cases 
    for idx,i in enumerate(test_cases):
        file_path = './Input/test_case' + str(idx)
        file = open(file_path,'w')
        for x in test_cases[idx]:
            file.writelines(x)
        file.close()

    #writing the ouput test cases
    for idx,i in enumerate(result):
        file_path = './Output/test_case' + str(idx)
        file = open(file_path,'w')
        for x in result[idx]:
            file.writelines(x)
        file.close()

import os
import filecmp

def get_output():
    # Run the Command for building
    os.system('g++ a.cpp -o a -std=c++17 -Wall -fsanitize=address -fsanitize=undefined -Wshadow')
    idx = 0

    # Validation of test cases
    for r,d,f in os.walk('./Input'):
        for file in f:
            command = "cat ./Input/" + file + " | ./a > output_expected.txt"
            os.system(command)
            with open('output_expected.txt','r') as file:
                lines = file.readlines()
            lines[-1] = lines[-1].rstrip()
            # print(lines)
            os.remove('output_expected.txt')
            with open('output_expected.txt','w') as file:
                for line in lines:
                    file.write(line)
            print("Your Output : ")
            for line in lines :
                print(line)
            output_path = './Output/test_case' + str(idx)
            print(10*'*')
            if filecmp.cmp(output_path,'output_expected.txt') == True:
               print("Test Case " + str(idx) + " Passed ")
               print(10*'*')
            else :
                print("Test Case " + str(idx) + " Differs from expected ") 
                print(10*'*')
            idx = idx + 1

 

url = sys.argv[1]
get_test_cases(url)

get_output()
