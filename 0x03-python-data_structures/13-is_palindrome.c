#include <stdio.h>
#include "lists.h"

/**
 * reverse_list - reversed fucntion
 * @state: state where the current middle head points
 */
void reverse_list(listint_t **state)
{
	listint_t *current = *state;
	listint_t *next = NULL;
	listint_t *prev = NULL;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	*state = prev;
}

/**
 * is_palindrome - check if a linked list is palindrome or not
 * @head: head pointer
 * Return: return 0 or 1
 */
int is_palindrome(listint_t **head)
{
	listint_t *fast = *head, *slow = *head, *middle_point = NULL;
	listint_t *old_track = *head;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	while (1)
	{
		fast = fast->next->next;
		if (fast == NULL)
		{
			middle_point = slow->next;
			break;
		}
		else if (fast->next == NULL)
		{
			middle_point = slow->next->next;
			break;
		}
		slow = slow->next;
	}
	reverse_list(&middle_point);
	while (middle_point != NULL && old_track != NULL)
	{
		if (middle_point->n != old_track->n)
			return (0);
		middle_point = middle_point->next;
		old_track = old_track->next;
	}
	return (1);
}
