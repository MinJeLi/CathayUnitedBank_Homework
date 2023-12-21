def last_person_position(n):

    people = list(range(1, n + 1))
    index = 0
    while len(people) > 1:
        # 每次跳過2個人（報數1, 2），然後移除第3個人
        index = (index + 2) % len(people)
        people.pop(index)
    return people[0]

# 輸入範圍：0 到 100
n = int(input("Enter the number of people (0 to 100): "))
if 0 < n <= 100:
    print(f"The position of the last person is: {last_person_position(n)}")
else:
    print("Invalid input. Please enter a number between 1 and 100.")