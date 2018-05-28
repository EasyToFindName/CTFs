#include <stdio.h>
int main() {	
	char buf[4];
	FILE* f = fopen("stdio_log", "w");
	
	read(0, buf, 4);
	
	printf("0x%08x", buf);
	if(memcmp(buf, "\x00\x0a\x00\xff", 4)) {
		fputs("1 FAIL\n", f);
		fclose(f);
		return 0;
	}
	fputs("OK", f);

	read(2, buf, 4);
        if(memcmp(buf, "\x00\x0a\x02\xff", 4)) {
		fputs("2 FAIL\n", f);
		fclose(f);
		return 0;
	}
	fputs("OK\n", f);
	printf("Stage 2 clear!\n");
	fclose(f);
	return 0;
}
