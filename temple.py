import os, sys
run = True
while run == True:
    command = input('Enter the command:\n')
    if (command == 'exit'):
        run = False
    else:
        os.system(command)
print('Good bye!')
