def reverse(random_string):

    if len(random_string) == 1:
        return random_string
    else:
        return reverse(random_string[1:]) +  random_string[0]

print(reverse('taran'))