def kai_kai_stack_(layer,first_layer_num):
    string_count,res=[0]*3,[]
    layers=[i+int(first_layer_num) for i in range(int(layer))]
    # print(layers)
    for idx,transnum in enumerate(layers):
        if (idx+1) %3==1:
            layer_tran=[(string_count[0]+i)%26+65 for i in range(transnum)]
            string_count[0]=(string_count[0]+transnum)%26
            # res.append("".join(map(chr,layer_tran))) ## uppercase A
            print("".join(map(chr,layer_tran))) ## uppercase A
        if (idx+1) %3==2:
            layer_tran=[(string_count[1]+i)%26+97 for i in range(transnum)]
            string_count[1]=(string_count[1]+transnum)%26
            # res.append("".join(map(chr,layer_tran))) ## uppercase A ## uppercase A
            print("".join(map(chr,layer_tran))) ## uppercase A ## uppercase A
        if (idx+1) %3==0:
            layer_tran=[((string_count[2]+i+1)%10) for i in range(transnum)]
            string_count[2]=(string_count[2]+transnum)%10
            # res.append("".join(map(str,layer_tran)))
            print("".join(map(str,layer_tran)))
    
    # return "\n".join(res)
layer= input()
first_layer_num = input()
# print(kai_kai_stack_(layer,first_layer_num))
kai_kai_stack_(layer,first_layer_num)