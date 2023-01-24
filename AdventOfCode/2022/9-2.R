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
    } else {
        y <- y + steps
        yHi <- max(yHi, y)
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
xs <- rep.int(x, 10L)
ys <- rep.int(y, 10L)
m[y,x] <- 1L
for (input in inputs) {
    mv <- strsplit(input, ' ')[[1L]]
    steps <- strtoi(mv[[2L]])
    for (s in 1L:steps) {
        if (mv[[1L]] == 'L') {
            xs[1L] <- xs[1L] - 1L
        } else if (mv[[1L]] == 'R') {
            xs[1L] <- xs[1L] + 1L
        } else if (mv[[1L]] == 'D') {
            ys[1L] <- ys[1L] - 1L
        } else {
            ys[1L] <- ys[1L] + 1L
        }

        for (i in 2L:length(xs)) {
            if (abs(xs[i-1L] - xs[i]) > 1L | abs(ys[i-1L] -  ys[i]) > 1L) {
                xs[i] <- xs[i] + diff(xs[i-1L], xs[i])
                ys[i] <- ys[i] + diff(ys[i-1L], ys[i])
            m[ys[10L],xs[10L]] <- 1L
            }
        }
    }
}
sum(m)