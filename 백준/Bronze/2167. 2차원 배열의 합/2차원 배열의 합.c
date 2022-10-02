#include <stdio.h>

int main(){

	int N, M, i, j, x, y, K;
	
	// 배열 입력 
	scanf("%d %d", &N, &M);
	int nums[301][301];
	for(int r=1; r<=N; r++){
		for(int c=1; c<=M; c++){
			scanf("%d", &nums[r][c]);
		}
	}

	// 서치 입력
	scanf("%d", &K);
	for(int c=0; c<K; c++){
		int sum=0;
		scanf("%d %d %d %d", &i, &j, &x, &y);
		for(int r=i; r<=x; r++){
			for(int c=j; c<=y; c++){
				sum += nums[r][c];	
			}
		}
		printf("%d\n", sum);
	}
	
	return 0;
}