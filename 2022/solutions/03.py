lines: list[str] = []
rucksacks: list[tuple[str, str]] = []

with open("../inputs/03.txt") as f:
  for line in f:
    line = line.strip()

    if line == "":
      continue

    lines.append(line)

    l = len(line) // 2
    first = line[:l]
    second = line[l:]

    assert len(first) == len(second)
    rucksacks.append((first, second))


def priority(item: str) -> int:
  lower = item.lower()
  result = ord(lower) - ord("a") + 1

  if item.isupper():
    result += 26
  
  return result


def find_common(*inputs) -> str:
  first = inputs[0]
  rest = inputs[1:]

  for c in first:
    found = True

    for other in rest:
      if c not in other:
        found = False
        break
    
    if found:
      return c
  
  raise RuntimeError("impossible!")



# Part 1

result = 0

for (first, second) in rucksacks:
  common_item = find_common(first, second)
  result += priority(common_item)

print("Part 1:", result)


# Part 2

result = 0

for i in range(len(lines) // 3):
  index = i * 3
  inputs = lines[index : index+3]
  common_item = find_common(*inputs)
  result += priority(common_item)

print("Part 2:", result)
