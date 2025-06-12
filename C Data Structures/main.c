#include <stdio.h>
#include "dynamic_array.h"
#include "hashmap.h"
#include "linked_list.h"
#include "graph.h"
#include "binary_tree.h"

int main() {
    printf("Dynamic Array:\n");
    DynamicArray arr;
    initArray(&arr);
    for (int i = 0; i < 5; i++) append(&arr, i * 10);
    printArray(&arr);
    freeArray(&arr);

    printf("\nHash Map:\n");
    HashMap map = {0};
    insertMap(&map, "alpha", 10);
    insertMap(&map, "beta", 20);
    printf("alpha: %d\n", getMap(&map, "alpha"));

    printf("\nLinked List:\n");
    Node *head = NULL;
    for (int i = 1; i <= 3; i++) push(&head, i);
    printList(head);

    printf("\nGraph:\n");
    Graph *graph = createGraph();
    addEdge(graph, 0, 1);
    addEdge(graph, 1, 2);
    printGraph(graph);

    printf("\nBinary Tree (Inorder):\n");
    TreeNode *root = NULL;
    int values[] = {7, 3, 9, 1, 5};
    for (int i = 0; i < 5; i++) insertTree(&root, values[i]);
    inorder(root);
    printf("\n");

    return 0;
}
