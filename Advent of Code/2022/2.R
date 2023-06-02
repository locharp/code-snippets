inputs <- readLines('https://raw.githubusercontent.com/locharp/code-snippets/main/AdventOfCode/2022/inputs/2')
choices <- list('A'=1L, 'B'=2L, 'C'=3L,
                'X'=1L, 'Y'=2L, 'Z'=3L)
total <- 0L
for (input in inputs) {
    inp <- strsplit(input, " ")
    res <- choices[[inp[[1L]][2L]]] - choices[[inp[[1L]][1L]]]
    if (res == 1L | res == -2L) {
        total <- total + 6L
    } else if (res == 0L) {
        total <- total + 3L
    }
    total <- total + choices[[inp[[1L]][2L]]]
}

total