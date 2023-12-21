def count_letters(text):
    # 將文字轉換為全部大寫，以便不區分大小寫
    text = text.upper()
    letter_count = dict()

    for char in text:
        # 字元為空格則不計算
        if char == ' ':
            continue
        # 計算各字元的出現次數
        if char in letter_count:
            letter_count[char] = letter_count[char] + 1    
        else:
            letter_count[char] = 1

    # 對字母作排序
    sorted_keys = sorted(letter_count)
    sorted_dict = dict()
    
    for key in sorted_keys:
        sorted_dict[key] = letter_count[key]
        
    return sorted_dict
    

# 測試函數
text = "Hello welcome to Cathay 60th year anniversary"
counted_letters = count_letters(text)

# 按字母順序輸出結果
print("輸出：")
for letter in counted_letters:
    print(f"{letter} {counted_letters[letter]}")
