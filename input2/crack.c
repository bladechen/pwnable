#include <stdio.h>
#include <unistd.h>
int main()
{
    char* argv[101] ;
    for (int i = 0;i < 100;i ++)
    {
        argv[i] = "A";
    }
    argv[100] = 0;
    argv['A'] = "\x00";
    argv['B'] = "\x20\x0a\x0d";
    argv['C'] = "26958";
    char* envp[2] = {"\xde\xad\xbe\xef=\xca\xfe\xba\xbe", NULL};



    /* char *envp[2] = {NULL}; */
    envp[0] = "\xde\xad\xbe\xef=\xca\xfe\xba\xbe";
    envp[1] = NULL;
    FILE* fp = fopen("\x0a", "w");
    fwrite("\x00\x00\x00\x00", 4, 1, fp);
    fclose(fp);
    int p1[2],p2[2];
    pipe(p1);
    pipe(p2);

    int pid = fork();
    if (pid == 0)
    {

        dup2(p1[0], 0);
        dup2(p2[0], 2);
        execve("fuck", argv, envp);
    }
    else
    {
        write(p1[1], "\x00\x0a\x00\xff", 4);
        write(p2[1], "\x00\x0a\x02\xff", 4);
        sleep(30);
    }
    return 0;
}
