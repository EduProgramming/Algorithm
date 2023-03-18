#include<stdio.h>
#include<stdlib.h>
#include<stdbool.h>

int main() {
    int money;
    scanf("%d", &money);
    money = 1000 - money;

    int maxChange = 500;
    bool isTen = false;

    int result = 0;
    while (maxChange > 0)
    {
        int cnt = money / maxChange;
        money = money % maxChange;
        result = result + cnt;

        if (isTen) {
            maxChange = maxChange / 2;
        } else {
            maxChange = maxChange / 5;
        }
        isTen = !isTen;
    }

    printf("%d", result);

    return 0;
}