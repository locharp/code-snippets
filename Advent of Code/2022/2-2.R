inputs <- readLines('https://raw.githubusercontent.com/locharp/code-snippets/main/AdventOfCode/2022/inputs/2')
choices <- list('A'=1L, 'B'=2L, 'C'=3L,
                'X'=-1L, 'Y'=0L, 'Z'=1L)
total <- 0L
for (input in inputs) {
    inp <- strsplit(input, " ")
    res <- choices[[inp[[1L]][2L]]]
    choice <- choices[[inp[[1L]][1L]]] + res
    if (choice == 4L) {
        choice <- 1L
    } else if (choice == 0L) {
        choice <- 3L
    }
    res <- res * 3L + 3L
    total <- total + res + choice
}

total