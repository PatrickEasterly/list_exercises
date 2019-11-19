


def letter_histogram(word):
  letters_in_word = {}
  for letter in word:
    letters_in_word[letter] = word.count(letter)

    
def histogram_sort(hist):
  mylist = []
  count = 0
  for item in hist:
    mylist.append([])
    mylist[count].append(item)
    mylist[count].append(hist[item])
    count += 1
  highest = mylist[0]
  for item in mylist:
    if item[1] > highest[1]:
      highest = item[1]
  return (highest)

  a = letter_histogram('hello')
  print(histogram_sort(a))