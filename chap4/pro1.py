import random
mood = random.randrange(4)
print('you are ..')
if mood == 0:
    print('-----------\n|  ^  ^   |\n| //   // |\n|   --    |\n-----------')
#happy
elif mood == 1:
    print('----------\n|  o  o |\n|       |\n|    o  |\n----------')
#nuetral
elif mood == 2:
    print('------------\n|   -    -     |\n|               |\n|    / -- \   |\n------------')
# sad
else:
    print('Illegal mood value!')
print('...today.')
