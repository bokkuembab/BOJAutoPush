#include <stdio.h>

int main(){
//	freopen("input.txt", "rt", stdin);
	
	int len, i, m, c=0;
	char a[50];
	
	scanf("%d", &len);
	for(i=0; i<len; i++){
		c=0;
		scanf("%s", a);
		for(m=0; a[m] != '\0'; m++){
			if(a[m]=='(')	c++;
			else if(a[m]==')')	c--;
		
			if(c<0)	break;
		}
		if(c==0)	printf("YES\n");
		else	printf("NO\n");
	}
	
	return 0;
}