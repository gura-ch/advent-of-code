inputs: list[tuple[str, str]] = []

with open("../inputs/02.txt") as f:
  for line in f:
    line = line.strip()

    if line == "":
      continue

    [opponent, me] = line.split(" ")
    inputs.append((opponent, me))


# Part 1

score = 0

choice_points = {
  "X": 1,
  "Y": 2,
  "Z": 3
}

for (opponent, me) in inputs:
  score += choice_points[me]

  match (opponent, me):
    case ("A", "X") | ("B", "Y") | ("C", "Z"):
      score += 3 # draw
    case ("A", "Y") | ("B", "Z") | ("C", "X"):
      score += 6 # won

print("Part 1:", score)


# Part 2

score = 0

responses = {
  "X": { # lose
    "A": "Z",
    "B": "X",
    "C": "Y"
  },
  "Y": { # draw
    "A": "X",
    "B": "Y",
    "C": "Z"
  },
  "Z": { # win
    "A": "Y",
    "B": "Z",
    "C": "X"
  }
}

for (opponent, outcome) in inputs:
  me = responses[outcome][opponent]
  score += choice_points[me]
  
  match outcome:
    case "Y":
      score += 3
    case "Z":
      score += 6

print("Part 2:", score)
