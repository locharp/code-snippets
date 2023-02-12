using System;
using RealLife;
using System.Collections.Generic;

class Tragedy1
{
    public static void Main(string[] args)
    {
        List<Human> soc = new List<Human>
        {
            new Kind1(RandomAge()),
            new Kind2(RandomAge()),
            new Kind1(RandomAge()),
            new Kind2(RandomAge()),
            new Kind2(RandomAge()),
            new Kind2(RandomAge()),
            new Kind2(RandomAge()),
            new Kind1(RandomAge())
        };
        List<Human> reEduCtr = new List<Human>();

        Console.Write("There are two kinds of people in this world...");
        Census(soc, reEduCtr);
        AsTimeGoes(soc, reEduCtr);
        Console.Write("\nSomething is happening when we are not paying attention...");
        Census(soc, reEduCtr);
        
        // AsTime...
        
    }

    static int RandomAge()
    {
        return 20 + new Random().Next(30);
    }

    static Human turn(Human scared)
    {
        Kind1 turned = new Kind1(scared.Age);
        turned.Flaws = scared.Flaws;
        return turned;
    }

    static void AsTimeGoes(List<Human> soc, List<Human> cc)
    {
        int tgt = -1;
        Human terr;

        for (int i = 0; i < soc.Count; i++)
        {
            if (soc[i].GetType().Name != "Kind1")
            {
                tgt = i;
                break;
            }
        }

        Console.WriteLine("\nSome reflect, some attack...");
        foreach (Human h in soc)
        {
            if (h.GetType().Name == "Kind1")
            {
                h.think(soc[tgt]);
            }
            else
            {
                h.think(h);
            }
        }

        terr = soc[tgt];
        cc.Add(terr);
        cc[cc.Count - 1].Flaws = terr.Flaws;
        soc.Remove(terr);

        for (int i = 0; i < soc.Count; i++)
        {
            if (soc[i].GetType().Name != "Kind1")
            {
                soc[i] = turn(soc[i]);
                break;
            }
        }
    }

    static void Census(List<Human> soc, List<Human> cc)
    {
        Console.WriteLine("\nsoc");
        foreach (Human h in soc)
        {
            Console.WriteLine($"{h.GetType().Name} Age: {h.Age}, Flaws: {h.Flaws}");
        }
        
        Console.WriteLine("\"reEduCtr\"");
        foreach (Human h in cc)
        {
            Console.Write($"{h.GetType().Name} Flaws: {h.Flaws}");
        }
    }
}