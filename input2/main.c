#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>
#include <arpa/inet.h>

int main(int argc, char* argv[], char* envp[]){
        printf("Welcome to pwnable.kr\n");
        printf("Let's see if you know how to give input to program\n");
        printf("Just give me correct inputs then you will get the flag :)\n");

        for (int i = 0; i < argc; i ++)
        {
            for (int j = 0; argv[i][j] ;j ++)
            {
                printf ("%x.", argv[i][j]);

            }
            printf ("]\n");
        }
        // argv
        if(argc != 4) return 0;
        printf ("hello[\x20]\n");
        if(strcmp(argv[1],"\x00")) return 0;
        printf ("hello[\x20]\n");
        if(strcmp(argv[2],"\x20\x0a\x0d")) return 0;
        printf("Stage 1 clear!\n");
}
