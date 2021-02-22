with open('file.txt', 'r', encoding='utf-8') as f:
    word = []
    f.readlines()
    words = [f"{word}. {''.join(word.split())} - {len(word.split())}"]
    for ind, el, count in enumerate(data, 1):
        print(f"{ind} {el} {count}", end='')
