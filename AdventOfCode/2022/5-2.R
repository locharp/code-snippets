inputs <- readLines('https://raw.githubusercontent.com/locharp/code-snippets/main/AdventOfCode/inputs/5')

crates <- list()
for (k in seq(from=2L, to=34L, by= 4L)) {
    i = (k + 2L) / 4L
    tmp <- c()
    for (j in 8L:1L) {
        ch <- substr(inputs[j], k, k)
        if (ch != ' ') {
            tmp[length(tmp)+1L] <- ch
        } else {
            break
        }
    }
    crates[[i]] <- tmp
}

for (input in inputs[11L:length(inputs)]) {
    procedure <- strsplit(input, ' ')[[1L]]
    mv <- strtoi(procedure[[2L]])
    f <- strtoi(procedure[[4L]])
    t <- strtoi(procedure[[6L]])
    len <- length(crates[[f]])
    c <- (len-mv+1):len
    crates[[t]] <- c(crates[[t]], crates[[f]][c])
    crates[[f]] <- crates[[f]][-c]
}

for (c in crates) {
    cat(c[[length(c)]])
}