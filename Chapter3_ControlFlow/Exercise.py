# 14 Exercise

count = 0
for number in range(1, 10):
    if not number % 2:
        print(number)
        count += 1
else:
    print(f"We have {count} even numbers")
