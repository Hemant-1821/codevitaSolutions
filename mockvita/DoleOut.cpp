#include <iostream>

using namespace std;

int cad(int l,int b){
    int count = 0;
    int temp = 0;
    while(true){
        if (l%b == 0){
            count += l/b;
            break;
        }
        else{
            temp = l%b;
            count += l/b;
            l = b;
            b = temp;
        }
    }
    return count;
}

int main()
{
    int P,Q,R,S;
    int stud = 0;
    cin >> P >> Q >> R >> S;
    for(int i = P; i<= Q;i++ ){
        for(int j = R;j<= S;j++){
            stud += cad(i,j);
        }
    }
    cout << stud;
   
    return 0;
}