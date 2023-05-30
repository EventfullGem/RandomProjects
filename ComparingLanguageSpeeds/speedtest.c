#include <stdio.h>
#include <time.h>


int main() {
    clock_t start_time = clock();

    for (int i = 0; i < 1000000; i++) {
        printf("%d\n", i);
    }

    clock_t end_time = clock();

    double time_taken = ((double)end_time - start_time) / CLOCKS_PER_SEC;

    printf("Time taken: %f seconds\n", time_taken);

    return 0;
}

// Time taken: I dont know a good benchmark everything is so confusing

