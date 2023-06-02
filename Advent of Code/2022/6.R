inputs <- readLines('https://raw.githubusercontent.com/locharp/code-snippets/main/AdventOfCode/inputs/6')
firstDistinct <- function(n) {
for (i in n:nchar(inputs)) {
    if (length(unique(strsplit(substr(inputs, i-(n-1), i), '')[[1]])) == n) {
        cat(i)
        break
    }
}
}
cat(firstDistinct(4), '\n')
firstDistinct(14)