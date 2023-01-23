inputs <- readLines('stdin')
elves <- c()
elf <- c()
for (input in inputs) {
     (input != '') {
        elf[length(elf)+1] = as.integer(input)
    } else {
        elves[length(elves)+1] = sum(elf)
        elf <- c()
    }
}
cat(sum(sort(elves)[(length(elves)-2):length(elves)]))