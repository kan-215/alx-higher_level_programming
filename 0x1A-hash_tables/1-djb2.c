#include "hash_tables.h"

/**
 * hash_djb2 - computes hash of 'str' using djb2
 * @str: string to hash
 *
 * Return:the value of the  64 bits hash
 */

unsigned long int hash_djb2(const unsigned char *str)
{
	unsigned long int hash;
	int a;

	hash = 5381;
	while ((a= *str++))
	{
		hash = ((hash << 5) + hash) + a;
	}
	return (hash);
}
