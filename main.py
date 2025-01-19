import string

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
    c_list = []
    for c in string.ascii_lowercase:
        if c in counts:
            c_list.append((c, counts[c]))

    return sorted(c_list, key= lambda x: x[1], reverse=True)

def print_report(fname: str):
    with open(fname) as f:
        content = f.read()

        word_count = count_words(content)
        letter_count = count_letters_sorted(count_chars(content))

        print(f"--- Begin report of {fname} ---")
        print(f"{word_count} words found in the document\n")

        for c, cnt in letter_count:
            print(f"The '{c}' character was found {cnt} times")
        print("--- End report ---")

def main():
    print_report("books/frankenstein.txt")

main()