import os
import mysql.connector

input_vcf_path = "./input"
output_path = "./output"

input_vcf_files = []
output_vcf_folders = []


def divide_chunks(l, n): 
    for i in range(0, len(l), n):  
        yield l[i:i + n] 

#create directories in output folder if they don't exist
if os.listdir(input_vcf_path):
    for csv_file in os.listdir(input_vcf_path):
        folder_name = csv_file.split('.')[0]
        if not os.path.isdir(folder_name) in os.listdir(output_path) and not folder_name in os.listdir(output_path):
            os.makedirs(os.path.join(output_path,folder_name))

for file in os.listdir(input_vcf_path):
    division_index = 0
    line_index = 0
    print('Opening file {}'.format(file))
    csv_file = open(os.path.join(input_vcf_path,file), 'r')
    
    print('Reading file...')
    txt = csv_file.read().split('\n')[1:]

    print('Dividing file...')
    sub_txt = list(divide_chunks(txt, 10000))

    for sub in sub_txt:
        path = os.path.join(output_path,file.split('.')[0],file.split('.')[0]+'-'+str(division_index)+'.csv')
        print('Writing data in {}'.format(path))
        division_index += 1
        sub_file = open(path, 'w')
        for s in sub:
            sub_file.write(s+'\n')
        # print(output_path,file.split('.')[0],'-',division_index,'.txt')
        # division_index += 1
    
    


