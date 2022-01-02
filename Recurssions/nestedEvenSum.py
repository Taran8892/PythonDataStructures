def nestedEvenSum(obj):
    sum = 0
    for key in obj:

        if type(obj[key]) is dict:
            sum += nestedEvenSum(obj[key])

        if type(obj[key]) is int and obj[key]%2 == 0:
            sum += obj[key]
    
    return sum


obj = {"name":"taran",
"age": 26,
"dob": 31,
"employment":
{
    "company":"infosys",
    "tenure": 2,
    "doj": 13
}}
print(nestedEvenSum(obj))
