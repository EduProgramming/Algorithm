#include<stdio.h>
#include<stdlib.h>

int main() {
    int N, M;
    scanf("%d %d", &N, &M);
    // N의 범위가 3 <= N <= 100이기에 여유로 101까지 설정
    int CARDS[101];

    for (int i=0; i < N; i++)
    {
        scanf("%d", &CARDS[i]);
    }

    int maxV = 0;
    for (int i=0; i < N-2; i++)
    {
        for (int j=i+1; j < N-1; j++)
        {
            for (int k=j+1; k < N; k++)
            {
                int sumV = CARDS[i] + CARDS[j] + CARDS[k];
                if (sumV > M) continue;
                else if (sumV > maxV) maxV = sumV;
            }
        }
    }

    printf("%d", maxV);

    return 0;
}