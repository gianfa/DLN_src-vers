import sys

if len(sys.argv)<2:
    print('Please tell my your name')
    name= str(input())
    print('Nice to meet you ', name, '! :)')
    exit()

print('Glad to meet you in person ', sys.argv[1], '! :D')
print('Have a nice day!')
exit()