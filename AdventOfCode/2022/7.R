inputs <- readLines('https://raw.githubusercontent.com/locharp/code-snippets/main/AdventOfCode/2022/inputs/7')

dirs <- list('/'=0L)
wd <- c()
for (input in inputs) {
    cmd <- strsplit(input, ' ')[[1L]]
    if (cmd[[2L]] == 'cd') {
        if (cmd[[3L]] == '..') {
            wd <- wd[-length(wd)]
        } else {
            wd[length(wd)+1L] <- cmd[[3L]]
        }
    } else if (cmd[[1L]] == 'dir') {
        tmp <- c(wd, cmd[[2L]])
        if (is.null(dirs[[toString(tmp)]])) {
            dirs[toString(tmp)] <- 0L
        }
    } else if (grepl('^[0-9]+', cmd[[1L]])) {
        dirs[[toString(wd)]] <- dirs[[toString(wd)]] + strtoi(cmd[[1L]])
    }
}

total <- 0L
for (name1 in names(dirs)) {
    size <- 0L
    for (name2 in names(dirs)) {
        if (grepl(name1, name2)) {
            size <- size + dirs[[name2]]
        }
    }
    if (size <= 100000L) {
        total <- total + size
    }
}
total