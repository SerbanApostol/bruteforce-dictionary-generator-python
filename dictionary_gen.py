import os
import signal

char_set = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM!@#$%&*/._-=+1234567890"  # modify to fit the possible characters
char_min = 8      #modify to select the minimal number of characters
char_max = 10     #modify to select the maximum number of characters




def exit_gracefully():
  global termination_signal
  termination_signal = True

def is_valid(word_str):
  has_small_letter = False
  has_big_letter = False
  has_number = False
  small_letters = "qwertyuiopasdfghjklzxcvbnm"
  big_letters = "QWERTYUIOPASDFGHJKLZXCVBNM"
  numbers = "1234567890"
  for x in word_str:
    if x in small_letters:
      has_small_letter = True
      pass
    if x in big_letters:
      has_big_letter = True
      pass
    if x in numbers:
      has_number = True
      pass
  return has_small_letter and has_big_letter and has_number

for_index = [0] * char_max
which_for = 0
termination_signal = False
signal.signal(signal.SIGTERM, exit_gracefully)


#check if dictionary_gen.restore exists
try:
  with open("./dictionary_gen.restore", "r") as f:
    char_set = f.readline()
    char_min = int(f.readline())
    char_max = int(f.readline())
    which_for = int(f.readline())
    for_index = f.readline().split()
    for_index = [int(x) for x in for_index]
  os.remove("./dictionary_gen.restore")
except:
  pass

def main():
 char_len = len(char_set)
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
      with open("./dictionary1.txt", "a") as f:
        if is_valid(word_str):
          f.write(word_str + "\n")
      for_index[which_for] = for_index[which_for] + 1
      while for_index[which_for] == char_len:
        for_index[which_for] = 0
        which_for = which_for - 1
        if which_for == -1:
          not_done = False
    if termination_signal:
      string = charset + "\n" + char_min + "\n" + char_max + "\n" + which_for + "\n" + ",".join(for_index)
      with open("./dictionary_gen.restore", "w") as f:
        f.write(string + "\n")
      return

main()
