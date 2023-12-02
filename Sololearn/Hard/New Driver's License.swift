import Foundation

let me = readLine()!
let agents = Float( readLine()! )!
let s = readLine()! + " " + me
var drivers = s.components( separatedBy: " " )
drivers.sort()
let pos = drivers.index( of: me )! + 1
let groupNum = ceil( Float( pos ) / agents )

print( 20 * Int( groupNum ) )
