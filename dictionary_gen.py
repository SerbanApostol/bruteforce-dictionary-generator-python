char_set = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM!@#$%&*/._-=+1234567890"  # modify to fit the possible characters
char_min = 8      #modify to select the minimal number of characters
char_max = 10     #modify to select the maximum number of characters




char_len = len(char_set)
for_index = [0] * char_max
which_for = 0
for i in range(char_min,char_max+1):
  word = [""] * i
  which_for = 0
  not_done = True
  while not_done:
    if which_for + 1 < i:
      word[which_for]=char_set[for_index[which_for]]
      for_index[which_for] = for_index[which_for] + 1
      which_for = which_for + 1
    else:
      word[which_for]=char_set[for_index[which_for]]
      word_str = ""
      for j in range(i):
        word_str = word_str + word[j]
      with open("dictionary.txt", "a") as f:
        if not word_str.isalpha() and not word_str.isnumeric():   #rule to choose words to have both letters and digits, modify to further fine tune the selection of words
          f.write(word_str + "\n")
      for_index[which_for] = for_index[which_for] + 1
      while for_index[which_for] == char_len:
        for_index[which_for] = 0
        which_for = which_for - 1
        if which_for == -1:
          not_done = False
