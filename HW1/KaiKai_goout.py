H,L=map(int,[15,8])
pofrain=int(20)
index=int(8)
answer=[]

if index>=6 or pofrain>=70:
	answer.append("雨傘")
if (H + L)/2 <= 18:
	answer.append("毛帽")
elif (pofrain > 20 and pofrain < 70) and L <= 20:
	answer.append("棒球帽")
if index >= 3 and pofrain <= 20:
	answer.append("太陽眼鏡")
if not answer:
    answer=["空手出門"]
result = ' '.join(str(item) for item in answer)
print(result)
