
with open('D:\pythonprogramms\even&odd.py', 'r') as fh:
     lines = fh.readlines()

     for line in lines:
        print(line.rstrip())

with open('D:\pythonprogramms\copy_even&odd.py', 'w') as fh_w:
             
        for line in lines:
            fh_w.write(line)
        
        print('{}'.format(lines))



