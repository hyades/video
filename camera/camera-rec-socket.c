#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <unistd.h>
#include <string.h>


char ip[] = "127.0.0.1";
int port = 4501;
//CONTROL = 0 => start recording
//CONTROL = 1 => stop recording


int controlRecording(int control)
{

	int clnt_fd;
	struct sockaddr_in serv_addr;
	char c[10];
	if(control == 0) 
	{
		strcpy(c,"$start\0");
		printf("CAMERA: Trying to start recording on server at %s\n",ip);
	}
	if(control == 1) 
	{
		strcpy(c,"$stop\0");
		printf("CAMERA: Trying to stop recording on server at %s\n",ip);
	}
	// create socket
	clnt_fd = socket(AF_INET, SOCK_STREAM, 0);
	// prepare for connect
	serv_addr.sin_family = AF_INET;
	serv_addr.sin_port = htons(port);
	serv_addr.sin_addr.s_addr = inet_addr(ip);
	// connect to server
	int fd = connect(clnt_fd, (struct sockaddr *) &serv_addr, sizeof(serv_addr));
	if(fd<0)printf("ERROR: Error connecting to server\n");
	// write to server
	int i = write(clnt_fd, &c, sizeof(c)); // write
	if(i<=0)printf("ERROR: Eroor writing data\n");
	
	close(clnt_fd);	
}


int main(int argc, char **argv) 
{	
	int i=atoi(argv[1]);
	controlRecording(i);
	return 0;
}