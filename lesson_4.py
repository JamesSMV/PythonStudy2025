list_ex = ["asdf", "kmjhgf", "vfgbhghnjk", "smfu", "lskjskdjnfnfj", "AAAAAAAAAAAAAA", "aaaaaaaaaaaaaa", "wwwwwwwwwww"]
print(max(list_ex))

lens = 0
for word in list_ex:
    if len(word) > lens:
        lens = len(word)
        word_max = word
print(lens, word_max)

lst = [4, 6, 2, 7]
[print(f"{i} to {v}") for i, v in enumerate(lst)]

out_app = []
out_ext = []
for i, v in enumerate(lst):
    # print(f"{i} to {v}")
    out_app.append([i, v])
    out_ext.extend([i, v])
print(f"строка 20:  {out_app}")
print(f"строка 21:  {out_ext}")

print()
out = "\n".join(f"{i} to {v}" for i, v in enumerate(lst))
print(out)

num = 69.87987
