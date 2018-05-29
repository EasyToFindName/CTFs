//this broke the game

#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>
#include <sys/types.h>
#include <sys/socket.h>

int main() {
    int fd = 0;
    char buf[1024];
    char buf2[2048];
    int length = 0;
    

    struct timeval tv;
    tv.tv_sec = 2;  
    tv.tv_usec = 0;  
    
    for(fd = 0; fd < 30; ++fd) {
	
        memset(buf, 0, 1024);
	setsockopt(fd, SOL_SOCKET, SO_RCVTIMEO, (const char*)&tv,sizeof(struct timeval));
	
	send(fd, "$SHELL\n", 7, 0);
        length = recv(fd, buf, 1023, 0);
        length = sprintf(buf2, "fd = %d [%s]\n", fd, buf);
	send(1, buf2, length, 0);
    }

    return 0;
}
