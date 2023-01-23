inputs <- readLines('https://raw.githubusercontent.com/locharp/code-snippets/main/AdventOfCode/2022/inputs/1')
elves <- c()
elf <- c()
for (input in inputs) {
    if (input != '') {
        elf[length(elf)+1L] <- as.integer(input)
    } else {
        elves[length(elves)+1L] <- sum(elf)
        elf <- c()
    }
}
cat(max(elves),'\n')