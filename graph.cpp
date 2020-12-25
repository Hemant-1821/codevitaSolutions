#include <iostream>

using namespace std;

int main()
{
    int num,i,n,count,num2,n1,n2,nOne,hcf;
    cin>>num;
    cin>>num2;
    int arr[1000000];
    n=0;
    n1=num;
    n2=num2;
    while(n1 != n2)
    {
        if(n1 > n2)
            n1 -= n2;
        else
            n2 -= n1;
    }
    hcf=n1;
   for(i=2;i<=num;i++){
       if(num%i==0){
           arr[n]=num;
           n++;
           num=num/i;
           i=1;
       }
   }
    for(i=2;i<=num2;i++){
       if(num2%i==0){
           arr[n]=num2;
           n++;
           num2=num2/i;
           i=1;
       }
   }
   int j,k;
   	for(i=0;i<n;++i)
		for(j=i+1;j<n;)
		{
			if(arr[i]==arr[j])
			{
				for(k=j;k<n-1;++k)
					arr[k]=arr[k+1];
					
				--n;
			}
			else
				++j;
		}
   count=0;
   for(int k=0;k<n;k++){
       
       if(arr[k]>hcf){
           count++;
       }
   }
   cout<<count;
   return 0;
}