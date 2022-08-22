#1
for letter in 'abcdefghijklmnopqrstuvwxyz':
    if letter in 'coronavirus':
        print('coronavirus contains', letter)
  
#2
for letter in 'abcdefghijklmnopqrstuvwxyz':
    if letter in 'coronavirus':
        for word in ['remdesivir', 'hydroxychloroquine', 'kaletra', 'favipiravir']:
            if letter in word:
                print(letter, 'is in coronavirus and also in', word)
