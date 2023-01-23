inputs <- readLines('https://raw.githubusercontent.com/locharp/code-snippets/main/AdventOfCode/inputs/3')
sum <- 0
for (input in inputs) {
    len <- nchar(input)
    items <- strsplit(input, NULL)
    item <- intersect(items[[1]][1:(len/2)], items[[1]][(len/2+1):len])
    priority <- utf8ToInt(item)
    sum <- sum + ifelse(priority > 96, priority - 96, priority - 38)
}
sum