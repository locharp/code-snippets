inputs <- read.table('https://raw.githubusercontent.com/locharp/code-snippets/main/AdventOfCode/2022/inputs/3', sep='\n')[[1L]]
sum <- 0L
for (i in seq(from=1L, to= length(inputs), by=3L)) {
    priority <- utf8ToInt(intersect(intersect(strsplit(inputs[i], '')[[1L]], strsplit(inputs[i+1L], '')[[1L]]), strsplit(inputs[i+2L], '')[[1L]]))
    sum <- sum + ifelse(priority > 96L, priority - 96L, priority - 38L)
}
sum