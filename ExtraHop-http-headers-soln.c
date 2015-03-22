/*
# Author: Ly Nguyen
# Location: Seattle, WA
# LinkedIn: www.linkedin.com/in/lynguyen60

Thoughts: 
The best way to process the file is if we go through it once - O(n) complexity.
A hash table is good for that. It also allows for fast retrieval - O(1) complexity
as well as insertion - O(1) complexity. I did not built my own hash table (uthash) 
because I did not want to reinvent the wheel. I hope that was an acceptable assumption.

Compilation:
gcc c_lynguyen.c -o c_lynguyen -Wall -ansi
*/


#include <stdio.h>
#include <stdlib.h>  /* malloc */
#include "uthash.h"

/* defines for bool */
typedef int bool;
#define true 1
#define false 0

/* hashable struct for uthash */
struct header_struct {
    char id[40];               /* key */
    int count;
    UT_hash_handle hh;         /* makes this structure hashable */
};

/* hash table */
struct header_struct *headers = NULL; 

/* function prototypes */
bool populate_hash(char *file_name);
bool count_headers(char *file_name);

int main(int argc, char *argv[])
{
	/* command line parsing */
	if ( argc != 3 )
    {
        printf( "usage: %s {file} {headers-of-interest-file}\n", argv[0]);
        printf( "Ex: %s ExtraHop-http-headers.txt ExtraHop-http-headers-of-interest.txt\n", argv[0]);
        exit(EXIT_FAILURE);
    }

    /* build hash table with http headers in file */
	if (false == populate_hash(argv[1]))
	{
		exit(EXIT_FAILURE);
	}

	/* check how many of each header of interest is in the file */
	if (false == count_headers(argv[2]))
	{
		exit(EXIT_FAILURE);
	}

	exit(EXIT_SUCCESS);
}


/* build hash table with http headers in file */
bool populate_hash(char *file_name)
{
	/* declare variables */
	char * line = NULL;
	size_t len = 0;
	ssize_t read;

	/* read file */
	FILE *fp;
	fp = fopen(file_name, "r");
	if (fp == NULL)
	{
        return false;
    }

    /* parse each line */
	while ((read = getline(&line, &len, fp)) != -1) 
	{
		/* take only http headers, not value */
		char * p;
        p = strchr(line,':');

        /* if possible http header found */
        if (p != 0)
        {
        	/* length of string from beginning to ':' character */
            size_t  key_length = 0;
            key_length = p - line;

            /* initialize string array */
            char key_text[40];
            memset( key_text, 0, (40)*sizeof(char) );
            strncpy(key_text, line, key_length);
            key_text[key_length] = '\0';

            /* fine if header already exists in hash table */
            struct header_struct *s;
		    HASH_FIND_STR(headers, key_text, s);

		    /* not found, insert new key */
		    if (s==NULL) {
		      s = malloc(sizeof(struct header_struct));
		      strncpy(s->id, key_text, 40);
		      s->count = 1;
		      HASH_ADD_STR( headers, id, s );
		    }
		    /* found, increase count */
		    else {
		    	s->count++;
		    }
        }
    }
	fclose(fp);

	return true;
}


/* check how many of each header of interest is in the file */
bool count_headers(char *file_name)
{
	/* declare variables */
	char * line = NULL;
	size_t len = 0;
	ssize_t read;

	/* read file */
	FILE *fp;
	fp = fopen(file_name, "r");
	if (fp == NULL)
	{
        return false;
    }

    /* parse each line */
	while ((read = getline(&line, &len, fp)) != -1) 
	{
		/* read until end of line, exclude carriage-returns */
		char * p;
        p = strchr(line,'\n');

        /* length of string from beginning to carriage-return */
        size_t  key_length = strlen(line);
        if (p != 0)
        {
            key_length = p - line;
        }

        /* initialize string array */
        char key_text[40];
        memset( key_text, 0, (40)*sizeof(char) );
        strncpy(key_text, line, key_length);
        key_text[key_length] = '\0';

        /* find if header exists in hash table */
		struct header_struct *s;
	    HASH_FIND_STR(headers, key_text, s); 

	    /* not found, count is 0 */
	    if (s==NULL) {
	    	printf("%s  0\n", key_text);
	    }
	    /* found, print count */
	    else{
	    	printf("%s  %d\n",s->id, s->count);
	    }
	}

	fclose(fp);

	return true;
}