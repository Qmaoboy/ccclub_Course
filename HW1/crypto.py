word,shift,res= input(),input(),""
for idx,i in enumerate(word):
    res+=chr(ord(i)+int(shift[idx%len(shift)]))
print(res)