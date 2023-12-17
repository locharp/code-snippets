public class Person
{
    private string _name;
    private int _age;
    
    public Person( string name, int age )
    {
        _name = name;
        _age = age;
    }
    
    public string Info
    {
        get
        {
            return _name + "s age is " + _age;
        }
    }
}
