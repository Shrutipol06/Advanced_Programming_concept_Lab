s="shruti"
old_char="h"
new_char="f"
result=""
for ch in s:
    if ch==old_char:
        result+=new_char
    else:
        result+=ch
print("updated string: ",result)