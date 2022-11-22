dictionary = ['-', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
              'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'W', 'X', 'Y', 'Z', '_', 'a', 'b', 'c', 'd', 'e',
              'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

lines = ['kJCC0S8WJboYYiJaIa6lhSiNB8x_lg',
         'C-6EGqjx4k4XmmKE749jYf93Mi22Kg',
         'PNrK0PCh32SX6kf7VldmsvLgPtTn_Q',
         'r7CLfvlEjUt5_BKqof-HGYHiY-dz2Q',
         'q9XsyYBpudl0TeqDydLBlmtmzUSSqw',
         'SB9wFIcbD6U2vjWAwC6rKxtZwpsx1Q',
         'E93DlUdTzt1Mwyu-5-IIbNicUVbf1w',
         '2UTwF9yGSUsgbOZtXtdKrad7nkknQA',
         'vFeggUot6JE2RMqSkfGLsrxmzkPQDw',
         '6mUby8X1ZrNYxvaIy8F6D6L8PUqkyA',
         'yYlDp3jsNX6wPuDn0lBGj65RKJOBMg',
         '87wfwTeEsQTlexmLEAwkxaQtrYpMMcGA']
res = ''

for line in lines:
    for i in line:
        res += ("%6s" % "{0:b}".format(ord(i))).replace(' ', '0')
    full = ("%256s" % res).replace(' ', '0')
    prev = 0
    arr = []
    for i in range(8, 256, 8):
        if i != 8:
           arr.append(str(int(full[-i:-prev], 2)))
        else:
            arr.append(str(int(full[-i:], 2)))
        prev = i
    res = ' '.join(arr)
    print(res)
    res = ''

# 1100111101001011000110111011011101110011011000101111111010110110101011001101001110100101011010100111011011101100111101001101101010010001111010111010111100001010100101000010010001010001110010011100101110111
# 111001110010110111111110110100001110011001110000110001010100111100101000011101100011110101111001101101101001011000110010011111010100010010100111000111110110110010101101011010111101101100000110010011100111
