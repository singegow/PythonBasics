weight = input("Weight: ")
weight_type = input("(L)bs ir (K)g:")
if weight_type == "L" or weight_type == "l":
# or we can use upper.. if weight_type.upper == "L"
    print(int(weight)*2)
elif weight_type.upper() == "K":
    print(int(weight)*3)
else:
    print("please enter proper intput")
