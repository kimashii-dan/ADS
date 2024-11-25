def quick_sort(array):
    length = len(array)
    if length <= 1:
        return array
    else:
        pivot = array.pop()
    
    greater_items = []
    smaller_items = []

    for item in array:
        if item > pivot:
            greater_items.append(item)
        else:
            smaller_items.append(item)
    return quick_sort(smaller_items) + [pivot]+ quick_sort(greater_items)



def isVowel(l): 
    if (l == 'a' or l == 'e' or
        l == 'i' or l == 'o' or l == 'u'): 
        return True
    else: 
        return False


def separation(array):
    consonant = []
    vowels = []

    for item in array:
        if (isVowel(item)):
            vowels.append(item)
        else:
            consonant.append(item)
    
    sorted_vowels = quick_sort(vowels)
    sorted_consonant = quick_sort(consonant)
    return sorted_vowels + sorted_consonant


n = int(input())
s = input()[:n]

print(''.join(separation(s)))