let boxes = readLine()!.split() { $0 == "," }
let target = readLine()!

for i in 0..<boxes.count {
    if boxes[i] == target {
        print( ( i + 1 ) * 5 )
    }
}
