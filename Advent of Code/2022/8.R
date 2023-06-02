inputs <- readLines('https://raw.githubusercontent.com/locharp/code-snippets/main/AdventOfCode/2022/inputs/8')
rows <- length(inputs)
cols <- nchar(inputs[1L])
m <- t(matrix(lapply(strsplit(gsub(', ', '', toString(inputs)), '')[[1L]], strtoi), ncol=rows))

check <- function(r, c, y=0L, my=0L, x=0L, mx=0L) {
    n <- m[[r,c]]
    i <- r + y
    j <- c + x
    repeat {
        if (m[[i,j]] >= n) {
            return (FALSE)
        }
        i <- i + y
        j <- j + x
        if (i == my | j == mx) {
            break
        }
    }
    return (TRUE)
}

counter <- rows * 2L + cols * 2L - 4L
for (r in 2L:(rows-1L)) {
    for (c in 2L:(cols-1L)) {
        if (check(r, c, x=-1L) |
            check(r, c, x=1L, mx=100L) |
            check(r, c, y=-1L) |
            check(r, c, y=1L, my=100L)) {
            counter <- counter + 1L
            next
        }
    }
}
counter