strit = input()
replaced_text = strit.replace(" ", "")
new_strit = replaced_text
if new_strit == new_strit[::-1]:
    print("YES")
else:
    print("NO")