import math
def MarvellousEucDistance(p1, p2):

  ans = math.sqrt((p1['x'] - p2['x'])**2 + (p1['y'] - p2['y'])**2)

  return ans


def MarvellousKNNClassifier(k = 3):
  border = "-"*80
  data = [
    {'point': 'A', 'x' : 1, 'y' : 2, 'label' : 'Red'},
    {'point': 'B', 'x' : 2, 'y' : 3, 'label' : 'Red'},
    {'point': 'C', 'x' : 3, 'y' : 1, 'label' : 'Blue'},
    {'point': 'D', 'x' : 5, 'y' : 6, 'label' : 'Blue'}
  ]

  print(border)
  print("Marvellous KNN Classifier")
  print(border)


  for i in data:
    print(i)

  print(border)


  x_coordinate = int(input("Enter X coordinate: "))
  y_coordinate = int(input("Enter y coordinate: "))

  new_point = {'x' : x_coordinate, 'y' : y_coordinate}

  print("Distances of all points: ")
  print(border)

  for d in data:
    d['distance'] = MarvellousEucDistance(d, new_point)

  for d in data:
    print(d)
  print(border)
  

  sorted_data = sorted(data, key= lambda item : item['distance'])

  print("Sorted Data: ")
  print(border)


  for d in sorted_data:
    print(d)

  print(border)


  nearest = sorted_data[:k]

  print("Nearest Neighbors: ")

  print(border)

  for d in nearest:
    print(f"{d['point']} - Distance: {d['distance']:.2f}")
  
  print(border)

  #Voting
  votes = {}

  for neighbors in nearest:
    label = neighbors['label']
    votes[label] = votes.get(label, 0) + 1

  print("Voting Result is: ")
  print(border)

  for d in votes:
    print("Name: ", d, "; Number of Votes: ", votes[d])

  print(border)

  i_max = 0
  name = ""

  for d in votes:
    if votes[d] > i_max:
      i_max = votes[d]
      name = d


  print("Predicted Class: ", name)
  print(border)


def main():
  MarvellousKNNClassifier(3)

if __name__ == "__main__":
  main()