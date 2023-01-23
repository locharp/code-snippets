comp_pair <- function(string) {
    pair <- strsplit(string, ',')[[1]]
    first <- strsplit(pair[[1]], '-')[[1]]
    second <- strsplit(pair[[2]], '-')[[1]]
    return (strtoi(first[1]) <= strtoi(second[1]) & strtoi(first[2]) >= strtoi(second[2]) | strtoi(first[1]) >= strtoi(second[1]) & strtoi(first[2]) <= strtoi(second[2]))
}

inputs <- readLines('https://raw.githubusercontent.com/locharp/code-snippets/main/AdventOfCode/inputs/4')
count <- 0
for (input in inputs) {
    if (comp_pair(input)) {
        count <- count + 1
    }
}
count