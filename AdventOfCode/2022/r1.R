inputs <- file('AdventOfCode/2022//inputs/1.txt', 'r')
elves <- c()
elf <- c()
while(TRUE) {
  line = readLines(inputs, n=1)
  if (line == 'end') {
    elves[length(elves)+1] = sum(elf)
    break
  }
  if (line == '') {
    elves[length(elves)+1] = sum(elf)
    elf <- c()
  } else {
    elf[length(elf)+1] = as.integer(line)
  }
}
close(inputs)
cat(max(elves),'\n')