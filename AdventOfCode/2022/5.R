# day 5
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
    f <- strtoi(procedure[[4L]])
    t <- strtoi(procedure[[6L]])
    for (i in 1L:strtoi(procedure[[2L]])) {
        crate <- crates[[f]][[length(crates[[f]])]]
        crates[[t]][length(crates[[t]])+1L] <- crate
        crates[[f]] <- crates[[f]][-length(crates[[f]])]
    }
}

for (c in crates) {
    cat(c[[length(c)]])
}