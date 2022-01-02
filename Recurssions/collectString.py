def collectString(obj):
    result = []

    for key in obj:
        if type(obj[key]) is str:
            result.append(obj[key])
        elif type(obj[key]) is dict:
            result = result + collectString(obj[key])
    return result


obj = {"name":"taran",
"age": 26,
"dob": 31,
"employment":
{
    "company":"infosys",
    "tenure": 2,
    "doj": 13
}}
print(collectString(obj))