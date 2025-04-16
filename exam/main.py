def count_vowels(s):
    # Перелік голосних букв у нижньому регістрі
    vowels = 'aeiou'
    
    # Підраховуємо кількість голосних в рядку, ігноруючи регістр
    count = sum(1 for char in s.lower() if char in vowels)
    
    return count

if __name__ == "__main__":
    test_string = "AbCdeEfGh"
    result = count_vowels(test_string)
    print(f"Кількість голосних букв у рядку '{test_string}': {result}")
