with open('D:\pythonprogramms\A_pattern', 'r') as fh:
    lines = fh.readlines()
    
    for line in lines:
        print(line.rstrip())
        
    with open('D:\pythonprogramms\copy_A_pattern_1', 'w') as fh_w:
          
        for line in lines:
            fh_w.write(line)
        
        print('{}'.format(lines))


#output:




