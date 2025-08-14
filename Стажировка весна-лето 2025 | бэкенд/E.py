def build_letter_to_code():
    return {
        'A': '2', 'B': '22', 'C': '222',
        'D': '3', 'E': '33', 'F': '333',
        'G': '4', 'H': '44', 'I': '444',
        'J': '5', 'K': '55', 'L': '555',
        'M': '6', 'N': '66', 'O': '666',
        'P': '7', 'Q': '77', 'R': '777', 'S': '7777',
        'T': '8', 'U': '88', 'V': '888',
        'W': '9', 'X': '99', 'Y': '999', 'Z': '9999'
    }


def load_dictionary(n, letter_to_code):
    dictionary = []
    for _ in range(n):
        word = input().strip()
        code = ''.join(letter_to_code[c] for c in word)
        dictionary.append((code, word))
    return dictionary


def decode_message(s, dictionary):
    length = len(s)
    dp = [False] * (length + 1)
    prev = [-1] * (length + 1)
    word_at = {}

    dp[0] = True

    for i in range(length):
        if dp[i]:
            for code, word in dictionary:
                if s.startswith(code, i):
                    j = i + len(code)
                    if not dp[j]:
                        dp[j] = True
                        prev[j] = i
                        word_at[j] = word

    result = []
    pos = length
    while pos > 0:
        result.append(word_at[pos])
        pos = prev[pos]

    return ' '.join(reversed(result))


def main():
    s = input().strip()
    n = int(input().strip())
    letter_to_code = build_letter_to_code()
    dictionary = load_dictionary(n, letter_to_code)
    decoded = decode_message(s, dictionary)
    print(decoded)


if __name__ == "__main__":
    main()
