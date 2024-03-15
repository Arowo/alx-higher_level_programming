#include "lists.h"

/**
 * check_cycle - check if a linked list is a cycle
 * @list: start of the list
 *
 * Return: return 1 on sucess
 */
int check_cycle(listint_t *list)
{
	listint_t *tortoise, *hare;
	
	tortoise = hare = list;
	if (!list)
		return (0);
	while (tortoise && hare && hare->next)
	{
		tortoise = tortoise->next;
		hare = hare->next->next;
		if (tortoise == hare)
			return (1);
	}
	return (0);
}
