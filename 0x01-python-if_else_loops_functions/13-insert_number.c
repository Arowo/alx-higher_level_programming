#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - insert node in a sorted list
 * @head: head of the list
 * @number: number to check and insert in the node
 * 
 * Return: return newnode
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *posNode;
	listint_t *newNode;
	listint_t *prevNode;

	newNode = malloc(sizeof(listint_t));
	posNode = *head;
	newNode->n = number;
	if (head == NULL || *head == NULL)
	{
		*head = newNode;
		return (newNode);
	}
	if(newNode == NULL)
		return (NULL);
	if (number < posNode->n)
	{
		newNode->next = posNode;
		*head = newNode;
		return (newNode);
	}
	while (posNode != NULL)
	{
		if (posNode->n > number)
			break;
		prevNode = posNode;
		posNode = posNode->next;
	}
	prevNode->next = newNode;
	newNode->next = posNode;
	return (newNode);
}
