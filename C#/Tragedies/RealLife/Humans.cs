namespace RealLife;

using System;

class Human
{
    internal int Age
    { get; set; }
  
    protected int DailyLife
    {
        get { return new Random().Next(10); }
    }

    internal int Flaws
    { get; set; }

    internal Human(int age)
    {
        Flaws = 0;
        Age = age;
        for (int i = 0; i < age; i++)
        {
            GrowOld();
        }
    }

    protected int LookForFlaws(Human flawed)
    {
        Random nakedEye = new Random();
        return nakedEye.Next(flawed.Flaws);
    }

    protected bool reflect()
    {
        Flaws -= Flaws > Age * 3 ? LookForFlaws(this) / 10 : 0;
        return Flaws > (Age * 3);
    }

    virtual protected void GrowOld()
    {
        if (Age > 5)
        {
            Random mature = new Random();
            for (int i = 0; i < Age; i += 10)
            {
                Flaws += mature.Next(Age);
            }
        }
    }

    internal int monitored()
    {
        return DailyLife;
    }

    internal virtual void think(Human watched) {}
}

class Kind1 : Human
{    
    internal Kind1(int age) : base(age) {}

    private bool feelGood(Human watched)
    {
        int observedFlawsOnSelf = LookForFlaws(this);
        int observedFlawsOnWatched = LookForFlaws(watched);

      while (observedFlawsOnWatched <= observedFlawsOnSelf)
        {
            observedFlawsOnWatched += watched.monitored();
        }

        return observedFlawsOnWatched > observedFlawsOnSelf;
    }
 
    internal override void think(Human watched)
    {
        if (feelGood(watched))
        {
            Console.WriteLine("Kind1: That MF needs to be re-educated!");
        }
    }

   protected override void GrowOld()
    {
        base.GrowOld();
        feelGood(new Human(new Random().Next(10 + Age)));
    }
}

class Kind2 : Human
{
    internal Kind2(int age) : base(age) {}

    internal override void think(Human watched)
    {
        if (reflect())
        {
            Console.WriteLine("Kind2: I'm not good enough.");
        }
    }

    protected override void GrowOld()
    {
        base.GrowOld();
        reflect();
    }
}