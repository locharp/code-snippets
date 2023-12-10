class Solution
{
    func countTestedDevices( _ batteryPercentages: [Int] ) -> Int
    {
        var ans = 0
        
        batteryPercentages.forEach { battery in
            if battery > ans
            {
                ans = ans + 1
            }        
        }
        
        return ans
    }
}
