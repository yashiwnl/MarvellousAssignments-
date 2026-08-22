import numpy as np
import math
from sklearn.preprocessing import StandardScaler


def calc_euc_distance(x1, y1, x2, y2):

  distance = math.sqrt((x2 - x1)**2 + (y2 - y1) **2)

  return distance


def main():
  data = [
    [25 , 20000],
    [30, 40000],
    [35, 80000]
    ]

  data = np.array(data)

  point1 = data[0]
  point2 = data[1]

  distance = calc_euc_distance(point1[0], point1[1], point2[0], point2[1])

  print("Distance before scaling: ",distance)

  scaler = StandardScaler()

  data = scaler.fit_transform(data)

  point1 = data[0]
  point2 = data[1]

  scaled_distance = calc_euc_distance(point1[0], point1[1], point2[0], point2[1])

  print("Distance after scaling: ", scaled_distance)


if __name__ == "__main__":
  main()

# Before scaling, the second feature dominates the Euclidean distance
# because its values are much larger than the first feature.

# After scaling, both features are on a comparable scale,
# so both contribute more equally to the distance calculation.