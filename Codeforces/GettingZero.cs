using System;

namespace Codeforces_with_comments;
class GettingZero
{
    internal static void Main()
    {
        // Read and make use of the first input – number of integers.
        Int16 n = Convert.ToInt16(Console.ReadLine());
        Int16[] values = new Int16[n];
        // Read the second line – integer inputs.
        string[] inputs = Console.ReadLine().Split();
        // Cast the inputs to integers.
        for (Int16 i = 0; i < n; i++)
            values[i] = Int16.Parse(inputs[i]);
        // For every input,
        foreach (Int16 value in values)
        {
            // Make a mutable copy of the integer.
            Int16 v = value;
            // Save how many +1 operations is needed to make it 0.
            Int16 diff = (Int16)(32768 - v);
            // If it is odd, make it even.
            Int16 odd = 0;
            if (v % 2 == 1)
            {
                v = (Int16)(v++);
                odd = (Int16)(odd++);
            }
            // Use a custom method to check how many x2 it needs to become 0.
            Int16 t = (Int16)(odd + T2(v));
            // Get the min of +1 operation and x2 operation.
            Int16 min = t < diff ? t : diff;
            // Check if there is a combination need fewer operations.
            // Odd number won't always take more operations, skip them
            for (Int16 i = 2; i < min; i += (Int16)(2))
            {
                t = (Int16)(odd + T2((Int16)(v + i)) + i);
                min = t < min ? t : min;
            }
            // Outout the number of operations needed for the current value with a blank space but no newline.
            Console.Write(min + " ");
        }
    }

    // The method that find no. of x2 operations needed to get zero.
    static Int16 T2(Int16 v)
    {
        Int16 i = 0;
        while (++i < 16 && v / 2 == v / 2.0)
            v /= 2;
        return (Int16)(16 - i);
    }
}