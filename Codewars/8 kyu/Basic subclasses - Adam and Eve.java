public class God
{

    public static Human[] create()
    {
        Human[] ans = new Human[2];
        ans[0] = new Man();
        ans[1] = new Woman();
        
        return ans;
    }
    
}





class Human {}
class Man extends Human {}
class Woman extends Human {}
