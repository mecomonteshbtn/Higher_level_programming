#include "lists.h"
#include <string.h>
#include <stdio.h>
#include <stdlib.h>

/**
  * is_palindrome - A function that checks if a list is a palindrome.
  * @head: The pointer to the head of the list.
  * Return: 0 if list not a palindrome, 1 if it is.
  */
int is_palindrome(listint_t **head)
{
	listint_t *tmp = *head;
	int nodes = 0, i = 0, *array = NULL;

	if (*head == NULL || head == NULL || (*head)->next == NULL)
		return (1);
	while (tmp)
	{
		nodes++;
		tmp = tmp->next;
	}
	array = malloc(sizeof(int) * nodes);
	tmp = *head;
	while (tmp)
	{
		array[i++] = tmp->n;
		tmp = tmp->next;
	}
	for (i = 0; i < nodes / 2; i++)
	{
		if (array[i] != array[nodes - 1 - i])
		{
			free(array);
			return (0);
		}
	}
	free(array);
	return (1);
}
