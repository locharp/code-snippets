comp_pair <- function(string) {
    pair <- strsplit(string, ',')[[1]]
    first <- strsplit(pair[[1]], '-')[[1]]
    second <- strsplit(pair[[2]], '-')[[1]]
    return (length(intersect(seq(from=strtoi(first[1]), to=strtoi(first[2])), seq(from=strtoi(second[1]), to=strtoi(second[2]))))) 
}

inputs <- readLines('https://raw.githubusercontent.com/locharp/code-snippets/main/AdventOfCode/inputs/4')
count <- 0
for (input in inputs) {
    if (comp_pair(input)) {
        count <- count + 1
    }
}
count