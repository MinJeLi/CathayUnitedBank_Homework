def count_letters(text):
    # 將文字轉換為全部大寫，以便不區分大小寫
    # Convert the text to all uppercase for case-insensitivity
    text = text.upper()
    letter_count = dict()

    for char in text:
        # 字元為空格則不計算
        # Do not count characters if they are spaces
        if char == ' ':
            continue
        # 計算各字元的出現次數
        # Calculate the frequency of each character
        if char in letter_count:
            letter_count[char] = letter_count[char] + 1
        else:
            letter_count[char] = 1

    # 對字母作排序
    # Sort the letters
    sorted_keys = sorted(letter_count)
    sorted_dict = dict()

    for key in sorted_keys:
        sorted_dict[key] = letter_count[key]

    return sorted_dict


# 測試函數
# Test the function
text = "Hello welcome to Cathay 60th year anniversary"
counted_letters = count_letters(text)

# 按字母順序輸出結果
# Output the results in alphabetical order
print("輸出：")
for letter in counted_letters:
    print(f"{letter} {counted_letters[letter]}")
