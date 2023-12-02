if let s = readLine()
{
    let a = s.split() { $0 == " " }
    
    a.forEach()
    {
        print( $0.dropFirst(), $0[$0.startIndex], "ay", separator: "", terminator: " " )
    }
}
