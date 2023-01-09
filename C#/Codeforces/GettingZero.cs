using System;

namespace Codeforces;

class GettingZero
{
    static void Main()
    {
        int n = Convert.ToInt32(Console.ReadLine());
        int[] values = new int[n];
        string[] inputs = Console.ReadLine().Split();
        for (int i = 0; i < n; i++)
            values[i] = int.Parse(inputs[i]);
        foreach (int value in values)
        {
            int v = value;
            int diff = 32768 - v;
            int odd = 0;
            if (v % 2 == 1)
            {
                v++;
                odd = 1;
            }
            int t = odd + T2(v);
            int min = t < diff ? t : diff;
            for (int i = 2; i < min; i += 2)
            {
                t = odd + T2(v + i) + i;
                min = t < min ? t : min;
            }
            Console.Write(min + " ");
        }       
    }
    
    static int T2(int v)
    {
        int i = 0;
        while (++i < 16 && v / 2 == v / 2.0)
            v /= 2;
        return 16 - i;
    }
}