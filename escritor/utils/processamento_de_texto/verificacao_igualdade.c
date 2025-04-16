#include <stdio.h>
#include <string.h>

int* max_time_len(const char* word) {
    int len_word = strlen(word);
    int max_len;
    int max_time;

    if (len_word <= 5) {
        max_len = len_word / 2;
        max_time = 2;
    }
    else {
        max_len = len_word / 3;
        max_time = 3;
    }

    static int array_len_time[2];
    array_len_time[0] = max_len;
    array_len_time[1] = max_time;
    
    return array_len_time;
}