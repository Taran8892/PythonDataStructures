
def productOfArray1(pof):
    print(pof)
    print(len(pof))
    if len(pof) == 0:
        return 1
    else:
        return pof[0] * productOfArray1(pof[1:])


# without recurssion
# def productOfArray(pof):
#     temp = 1

#     for i in pof:
#         temp = temp * i

#     print(temp)

print(productOfArray1([4,5,6]))