#include <fcntl.h>
int main(int argc, char* argv[]){

	
	int fd;
	if(fd=open("./password",O_RDONLY,0400) < 0){
		printf("can't open password %d\n", fd);
		return 0;
	}
	char buf[10];
	read(fd, buf, 4);
	buf[5] = 0;

	printf("%s\n", buf);
}
