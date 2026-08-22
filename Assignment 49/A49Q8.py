
def main():

  actual = [1,1,1,1,0,0,0,0]
  predicted = [1,1,0,1,0,1,0,0]   

  tp = 0
  tn = 0
  fp = 0
  fn = 0

  for a,p in zip(actual, predicted):

    if a == 1 and p == 1:
      tp += 1
    elif a == 0 and p == 0:
      tn += 1
    elif a == 0 and p == 1:
      fp += 1
    elif a == 1 and p == 0:
      fn += 1

  print("True Positive: ", tp)
  print("True Negative: ", tn)
  print("False Positive: ", fp)
  print("False Negative: ", fn)


if __name__ == "__main__":
  main()