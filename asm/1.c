char *s="hello";
int main()
{
     char buf[100];
     int len = read(0, buf, 99);
     buf[len -1] = 0;
     /* printf ("%s %d\n", buf, len); */
     int fd = open( buf, 0);
     /* perror(""); */
     /* printf ("%d\n", fd); */
     len = read(fd, buf, 100);
     write(1, s, 5);

}
