import math
def MarvellousEucDistance(p1, p2):

  ans = math.sqrt((p1['x'] - p2['x'])**2 + (p1['y'] - p2['y'])**2)

  return ans


def MarvellousKNNClassifier(k = 3):

  data = [
    {'point': 'A', 'x' : 2, 'y' : 60, 'Result' : 'Fail'},
    {'point': 'B', 'x' : 5, 'y' : 80, 'Result' : 'Pass'},
    {'point': 'C', 'x' : 6, 'y' : 85, 'Result' : 'Pass'},
    {'point': 'D', 'x' : 1, 'y' : 50, 'Result' : 'Fail'}
  ]

  study_hours = int(input("Enter Study Hours: "))
  attendance = int(input("Enter Attendance: "))

  new_point = {'x' : study_hours, 'y' : attendance}

  for d in data:
    d['distance'] = MarvellousEucDistance(d, new_point)

  sorted_data = sorted(data, key= lambda item : item['distance'])

  nearest = sorted_data[:k]

  #Voting
  votes = {}

  for neighbors in nearest:
    Result = neighbors['Result']
    votes[Result] = votes.get(Result, 0) + 1

  i_max = 0
  name = ""

  for d in votes:
    if votes[d] > i_max:
      i_max = votes[d]
      name = d


  print("Predicted Result: ", name)

def main():
  MarvellousKNNClassifier(3)

if __name__ == "__main__":
  main()