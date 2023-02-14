int solution(int number) {
  if(number<3)
    return 0;
  else {
    int sum=0;
    for(int i=3;i<number;i++)
      {
        if((i%3==0)||(i%5==0))
          sum+=i;
      }
    return sum;
  }
}