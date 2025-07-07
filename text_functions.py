
def count_domains(emails):
    # no of domains
    return list(map(lambda x: x.split('@')[-1],emails))       
def count_vowels(str):
    vowels = "aeiou"
    count = 0
    for i in str:
        if i.lower() in vowels:
            count += 1
    print(f"Number of vowels in {str} is {count}")
def text_search(original_text,search_text='i'):
    print(f"for the string '{original_text}'")
    for i in range(len(original_text)):
        if original_text[i] ==search_text:
            print(f"Found i at index {i}")



    



        