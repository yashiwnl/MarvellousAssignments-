import math

def MarvellousEucDistance(p1, p2):

  ans = math.sqrt((p1['x'] - p2['x'])**2 + (p1['y'] - p2['y'])**2)

  return ans


def MarvellousKNNClassifier(x,y,k = 3):

  data = [
    {'point': 'A', 'x' : 1, 'y' : 2, 'label' : 'Red'},
    {'point': 'B', 'x' : 2, 'y' : 3, 'label' : 'Red'},
    {'point': 'C', 'x' : 3, 'y' : 1, 'label' : 'Blue'},
    {'point': 'D', 'x' : 5, 'y' : 6, 'label' : 'Blue'},
    {'point': 'E', 'x' : 6, 'y' : 6, 'label' : 'Blue'},
    {'point': 'F', 'x' : 3, 'y' : 4, 'label' : 'Red'},
    {'point': 'G', 'x' : 3, 'y' : 2, 'label' : 'Red'}
  ]

  new_point = {'x' : x, 'y' : y}

  for d in data:
    d['distance'] = MarvellousEucDistance(d, new_point)

  sorted_data = sorted(data, key= lambda item : item['distance'])

  nearest = sorted_data[:k]

  #Voting
  votes = {}

  for neighbors in nearest:
    label = neighbors['label']
    votes[label] = votes.get(label, 0) + 1

  i_max = 0
  name = ""

  for d in votes:
    if votes[d] > i_max:
      i_max = votes[d]
      name = d


  print(f"K = {k} -> {name}")


def main():
  x = int(input("Enter X coordinate: "))
  y = int(input("Enter Y coordinate: "))

  print("Predicted Results: \n")
  MarvellousKNNClassifier(x,y,1)
  MarvellousKNNClassifier(x,y,3)
  MarvellousKNNClassifier(x,y,5)


if __name__ == "__main__":
  main()