def isPalindrome(random_string):

    if len(random_string) == 0:
        return True

    if random_string[0] != random_string[len(random_string)-1]:
        return False

    return isPalindrome(random_string[1:-1])

print(isPalindrome('nitin'))

