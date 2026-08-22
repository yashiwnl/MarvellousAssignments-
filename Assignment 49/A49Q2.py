import numpy as np

def main():
  data = np.array([6,7,8,9,10,11,12])

  variance = np.var(data)

  sd = np.std(data)

  print("Variance: ", variance)
  print("Standard Deviation: ", sd)


if __name__ == "__main__":
  main()