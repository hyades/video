#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <unistd.h>
#include <sys/types.h>
#include <signal.h>
#define port 4500
char command[] = "/usr/bin/gst-launch v4l2src  ! videorate  ! video/x-raw-yuv, width=320, height=240  ! clockoverlay halign=right valign=bottom ! theoraenc drop-frames=false ! oggmux ! queue !  tcpserversink port=5000";
char * const parm[] = { "/usr/bin/gst-launch",
					"v4l2src" , "!", 
					"videorate","!",
					"video/x-raw-yuv,width=320,height=240" , "!",
					"clockoverlay", "halign=right","valign=bottom", "!",
					"theoraenc", "drop-frames=false", "!",
					"oggmux", "!",
					"queue", "!",
					"tcpserversink", "port=5000"
					,NULL };


int contains(char * a, int i)
{
	if(i==0)
	{
		if(a[0]=='$' && a[1] == 's' && a[2] == 't' && a[3] == 'a' && a[4] == 'r' && a[5] == 't')
			return 1;
	}
	if(i==1)
	{
		if(a[0]=='$' && a[1] == 's' && a[2] == 't' && a[3] == 'o' && a[4] == 'p')
			return 1;
	}
	return 0;
}

int main() 
{
	int serv_fd, clnt_fd;
	struct sockaddr_in serv_addr;
	char c[10];
	pid_t pid;

// create socket
	serv_fd = socket(AF_INET, SOCK_STREAM, 0);
// prepare for bind
	serv_addr.sin_family = AF_INET;
	serv_addr.sin_port = htons(port);
	serv_addr.sin_addr.s_addr = INADDR_ANY;
// bind
	int s = bind(serv_fd, (struct sockaddr *) &serv_addr, sizeof(serv_addr));
	if(s<0)
	{
		printf("ERROR: Error binding to port\n");
		return 0;
	}

// listen only 1 queue
	listen(serv_fd, 1);
	printf("CAMERA: Listening on port %d\n",port);
// accept only 1 client
	
// read and write until ^D (from client)
	while(1) 

	{ // read from client
		clnt_fd = accept(serv_fd, NULL, NULL);
		printf("Connection Recieved on file descriptor:%d\n",clnt_fd);
		int rs = read(clnt_fd, &c, sizeof(c)); 
		if(rs<0)
		{
			printf("ERROR: Error reading from socket\n");
			continue;
		}

		printf("Recieved content:%s\n",c);
		if(contains(c,0))
		{
			pid = fork();
			if(pid==0)
			{
				printf("CAMERA: Starting streaming\n");
				int i = execv(
					"/usr/bin/gst-launch",
					parm);
				if(i<0) printf("ERROR: Could not setup video stream\n");
			}
			else if(pid<0)
				printf("ERROR: Error in forking");
		}
		else if(contains(c,1))
		{
			if(pid)
			{
				printf("CAMERA: Stopping streaming\n");
				kill(pid,SIGKILL);
			}
		}
		else 
		{
			printf("Camera: Recieved Unknown Message\n");
		}
	}
	// close connection from client and stop echo server
	close(clnt_fd);
	close(serv_fd);
	return 0;
}