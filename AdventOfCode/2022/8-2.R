inputs <- readLines('https://raw.githubusercontent.com/locharp/code-snippets/main/AdventOfCode/2022/inputs/8')
rows <- length(inputs)
cols <- nchar(inputs[1L])
m <- t(matrix(lapply(strsplit(gsub(', ', '', toString(inputs)), '')[[1L]], strtoi), ncol=rows))
check <- function(r, c, y=0L, my=0L, x=0L, mx=0L) {
    n <- m[[r,c]]
    i <- r + y
    j <- c + x
    while (i != my & j != mx) {
        if (m[[i,j]] >= n) {
            return (abs(i-r+(j-c)))
        }
        i <- i + y
        j <- j + x
    }
    #(,'*', i-r+(j-c)
    return (abs(i-r+(j-c))-1L)
}

highestScore <- 0L
for (r in 1L:rows) {
    for (c in 1L:cols) {
        score <- 1L
        score <- score * check(r, c, x=-1L)
        score <- score * check(r, c, x=1L, mx=100L)
        score <- score * check(r, c, y=-1L)
        score <- abs(score * check(r, c, y=1L, my=100L))
        if (highestScore < score) {
            highestScore <- score
        }
    }
}
highestScore