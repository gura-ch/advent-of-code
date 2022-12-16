elves = []

with open("input.txt") as f:
  current_elf = 0

  for line in f:
    line = line.strip()

    if line == "":
      elves.append(current_elf)
      current_elf = 0
    else:
      current_elf += int(line)

print("Part 1:", max(elves))

top_3 = sorted(elves)[-3:]

print("Part 2:", sum(top_3))
