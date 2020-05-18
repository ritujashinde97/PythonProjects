
try:
    g = open('my_text.txt','w')
except FileNotFoundError as error:
    print(error)

else:
    while True:
        user_input = input('Enter student records in one line (q to Quit): ')
        user_input = user_input + '\n'
        if user_input == 'q\n':
            break
        g.write(user_input)
    g.close()
finally:
    print('Record saved.')

try:
    f = open('my_text.txt','r')
except FileNotFoundError as error:
    print(error)
else:
    record_list = f.readlines()
    f.close()
    for item in record_list:
        print(item)
finally:
    print('Record printed. ')


