#!/usr/bin/py

#load the data, choose those related to the calculation temp and sort them in order to perform the numerical integration

with open ('input_test_sort.txt', 'r') as f:
    with open('output_test_sort.txt', 'w') as f2:

        for line in f:
            for i in line:
                # if line.startswith('P, BAR') or line.startswith('T, K') or  line.startswith('H, KJ/KG') or line.startswith('Cp, KJ/(KG)(K)'):
                if i.startswith('P, BAR'):
                    print(i)
                # else:
                #     print('N/A')             
                
                
                # print(line.rstrip())
                # with open('output_test_sort.txt', 'w') as f2:
                    # f2.write(line.rstrip())
                    # print(f2)
