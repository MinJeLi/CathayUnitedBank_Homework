def correct_scores(scores):
    corrected_scores = []
    for score in scores:
        # 將成績轉換為字串
        string_score = str(score)
        # 反轉字串
        reverse_string = string_score[::-1]
        # 再轉換回整數
        corrected_score = int(reverse_string)
        corrected_scores.append(corrected_score)
    return corrected_scores

# 測試函數
original_scores = [53, 64, 75, 19, 92]
incorrect_scores = [35, 46, 57, 91, 29]

print("原始成績：", original_scores)
print("錯誤成績：", incorrect_scores)
print("修正成績：", correct_scores(incorrect_scores))