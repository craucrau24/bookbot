def count_words(content: str):
    words = content.split()
    return len(words)

def count_chars(content: str):
    result = {}
    for c in content:
        low = c.lower()
        result[low] = result.setdefault(low, 0) + 1
    return result

def count_letters_sorted(counts: dict):
    c_lst = counts.items()

def main():
    with open("books/frankenstein.txt") as f:
        file_content = f.read()
        print(count_chars(file_content))

main()