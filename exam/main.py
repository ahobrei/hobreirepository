def count_vowels(s):
    vowels = 'aeiou'
    
    count = sum(1 for char in s.lower() if char in vowels)
    
    return count

if __name__ == "__main__":
    test_string = "AbCdeEfGh"
    result = count_vowels(test_string)
    print(f"Кількість голосних букв у рядку '{test_string}': {result}")
