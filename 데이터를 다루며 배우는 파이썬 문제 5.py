word = 'X-DSPAM-Confidence:0.8475'
index = word.find(':')
A = word[index+1: ]
print(float(A))