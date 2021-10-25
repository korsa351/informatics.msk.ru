a, b, c, n = map(int, input().split())
shopping_options = []
for ka in range((n // a)+1):
    if ka * a > n:
        break
    elif ka * a == n:
        shopping_options.append([ka, 0, 0])
        break
    for kb in range((n // b)+1):
        if ka * a + kb * b > n:
            break
        elif ka * a + kb * b == n:
            shopping_options.append([ka, kb, 0])
            break
        for kc in range((n // c)+1):
            if ka*a+kb*b+kc*c == n:
                shopping_options.append([ka, kb, kc])
            elif ka*a+kb*b+kc*c > n:
                break

# shopping_options = sorted(shopping_options)
print(len(shopping_options))
for index in range(len(shopping_options)):
    print(*shopping_options[index])
