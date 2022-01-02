def stringifyNumbers(obj):
    
    for key in obj:
        if type(obj[key]) is int:
            obj[key] = str(obj[key])
        elif type(obj[key]) is dict:
            stringifyNumbers(obj[key])
    return obj


obj = {"name":"taran",
"age": 26,
"dob": 31,
"employment":
{
    "company":"infosys",
    "tenure": 2,
    "doj": 13
}}

print(stringifyNumbers(obj))