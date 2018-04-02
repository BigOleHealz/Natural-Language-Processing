bad_words = []
f1 = open("bad_words.txt", "r").readlines()
f2 = open("bad_words2.txt", "r").readlines()
for line in f1:
  line = line.replace("\n", "").strip()
  bad_words.append(line)

for line in f2:
  line = line.replace("\n", "").strip()
  line = line.replace("\'","").strip()
  if (line not in bad_words):
    bad_words.append(line)

print(bad_words)

with open("compiled_list.txt", "w") as output:
  for word in bad_words:
    if "," in word:
      word = word.replace(",","")
      output.write(str(word))
      output.write("\n")
    else:
      output.write(str(word))
      output.write("\n")
