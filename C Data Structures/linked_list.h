#ifndef LINKED_LIST_H
#define LINKED_LIST_H

typedef struct Node {
    int data;
    struct Node *next;
} Node;

void push(Node **head, int data);
void printList(Node *head);

#endif
