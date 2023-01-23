inputs <- read.table('https://raw.githubusercontent.com/locharp/code-snippets/main/AdventOfCode/inputs/3', sep='\n')[[1L]]
sum <- 0
for (i in seq(from=1, to= length(inputs), by=3)) {
    priority <- utf8ToInt(intersect(intersect(strsplit(inputs[i], '')[[1L]], strsplit(inputs[i+1L], '')[[1L]]), strsplit(inputs[i+2L], '')[[1L]]))
    sum <- sum + ifelse(priority > 96, priority - 96, priority - 38)
}
sum