inputs <- readLines('https://raw.githubusercontent.com/locharp/code-snippets/main/AdventOfCode/2022/inputs/9')
xHi <- 0L
xLo <- 0L
yHi <- 0L
yLo <- 0L
x <- 0L
y <- 0L
for (input in inputs) {
    mv <- strsplit(input, ' ')[[1L]]
    steps <- strtoi(mv[[2L]])
    if (mv[[1L]] == 'L') {
        x <- x - steps
        xLo <- min(xLo, x)
    } else if (mv[[1L]] == 'R') {
        x <- x + steps
        xHi <- max(xHi, x)
    } else if (mv[[1L]] == 'D') {
        y <- y - steps
        yLo <- min(yLo, y)
    } else if (mv[[1L]] == 'U') {
        y <- y + steps
        yHi <- max(yHi, y)
    } else {
        cat('Unknown input: ', mv[[1L]], steps)
    }
}

diff <- function(x1, x2) {
    if (x1 == x2) {
        return (0L)
    } else if (x1 > x2) {
        return (1L)
    } else {
    return (-1L)
    }
}

m <- matrix(0L, nrow = yHi - yLo + 1L, ncol = xHi -xLo + 1L)
x <- 1L - xLo
y <- 1L - yLo
hx <- x
hy <- y
m[y,x] <- 1L
for (input in inputs) {
    mv <- strsplit(input, ' ')[[1L]]
    steps <- strtoi(mv[[2L]])
    if (mv[[1L]] == 'L') {
        hx <- hx - steps
    } else if (mv[[1L]] == 'R') {
        hx <- hx + steps
    } else if (mv[[1L]] == 'D') {
        hy <- hy - steps
    } else if (mv[[1L]] == 'U') {
        hy <- hy + steps
    } else {
        cat('Unknown input:', mv[[1L]], steps)
    }
    while (abs(hx - x) > 1L | abs(hy -  y) > 1L) {
        x <- x + diff(hx, x)
        y <- y + diff(hy, y)
        m[y,x]] <- 1L
    }
}
sum(m)