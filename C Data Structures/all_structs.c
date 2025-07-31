#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/// --- 1. Dynamic Array ---

typedef struct {
    int *data;
    int size;
    int capacity;
} DynamicArray;

void initArray(DynamicArray *arr) {
    arr->capacity = 4;
    arr->size = 0;
    arr->data = malloc(arr->capacity * sizeof(int));
}

void append(DynamicArray *arr, int value) {
    if (arr->size == arr->capacity) {
        arr->capacity *= 2;
        arr->data = realloc(arr->data, arr->capacity * sizeof(int));
    }
    arr->data[arr->size++] = value;
}

void printArray(DynamicArray *arr) {
    for (int i = 0; i < arr->size; i++) {
        printf("%d ", arr->data[i]);
    }
    printf("\n");
}

void freeArray(DynamicArray *arr) {
    free(arr->data);
}

/// --- 2. Associative Array (Simple Hash Map) ---

#define TABLE_SIZE 10

typedef struct Entry {
    char *key;
    int value;
    struct Entry *next;
} Entry;

typedef struct {
    Entry *buckets[TABLE_SIZE];
} HashMap;

unsigned int hash(const char *key) {
    unsigned int hash = 0;
    while (*key) hash = (hash * 31) + *key++;
    return hash % TABLE_SIZE;
}

void insertMap(HashMap *map, const char *key, int value) {
    unsigned int idx = hash(key);
    Entry *new_entry = malloc(sizeof(Entry));
    new_entry->key = strdup(key);
    new_entry->value = value;
    new_entry->next = map->buckets[idx];
    map->buckets[idx] = new_entry;
}

int getMap(HashMap *map, const char *key) {
    unsigned int idx = hash(key);
    Entry *entry = map->buckets[idx];
    while (entry) {
        if (strcmp(entry->key, key) == 0) return entry->value;
        entry = entry->next;
    }
    return -1;
}

int deleteMap(HashMap *map, const char *key) {
    unsigned int idx = hash(key);
    Entry *entry = map->buckets[idx];
    Entry *prev = NULL;

    while (entry) {
        if (strcmp(entry->key, key) == 0) {
            if (prev) {
                prev->next = entry->next;
            } else {
                map->buckets[idx] = entry->next;
            }
            free(entry->key);
            free(entry);
            return 1; // Success
        }
        prev = entry;
        entry = entry->next;
    }

    return 0; // Not found
}

/// --- 3. Singly Linked List ---

typedef struct Node {
    int data;
    struct Node *next;
} Node;

void push(Node **head, int data) {
    Node *new_node = malloc(sizeof(Node));
    new_node->data = data;
    new_node->next = *head;
    *head = new_node;
}

void printList(Node *head) {
    while (head) {
        printf("%d -> ", head->data);
        head = head->next;
    }
    printf("NULL\n");
}

/// --- 4. Graph (Adjacency List) ---

#define MAX_VERTICES 5

typedef struct GNode {
    int vertex;
    struct GNode *next;
} GNode;

typedef struct {
    GNode *adjLists[MAX_VERTICES];
} Graph;

Graph *createGraph() {
    Graph *graph = malloc(sizeof(Graph));
    for (int i = 0; i < MAX_VERTICES; i++)
        graph->adjLists[i] = NULL;
    return graph;
}

void addEdge(Graph *graph, int src, int dest) {
    GNode *new_node = malloc(sizeof(GNode));
    new_node->vertex = dest;
    new_node->next = graph->adjLists[src];
    graph->adjLists[src] = new_node;
}

void printGraph(Graph *graph) {
    for (int v = 0; v < MAX_VERTICES; v++) {
        GNode *temp = graph->adjLists[v];
        printf("Vertex %d:", v);
        while (temp) {
            printf(" -> %d", temp->vertex);
            temp = temp->next;
        }
        printf("\n");
    }
}

/// --- 5. Binary Tree ---

typedef struct TreeNode {
    int data;
    struct TreeNode *left, *right;
} TreeNode;

TreeNode *createNode(int data) {
    TreeNode *node = malloc(sizeof(TreeNode));
    node->data = data;
    node->left = node->right = NULL;
    return node;
}

void insertTree(TreeNode **root, int data) {
    if (*root == NULL)
        *root = createNode(data);
    else if (data < (*root)->data)
        insertTree(&(*root)->left, data);
    else
        insertTree(&(*root)->right, data);
}

void inorder(TreeNode *root) {
    if (root) {
        inorder(root->left);
        printf("%d ", root->data);
        inorder(root->right);
    }
}

/// --- MAIN FUNCTION ---

int main() {
    // --- Dynamic Array ---
    printf("Dynamic Array:\n");
    DynamicArray arr;
    initArray(&arr);
    for (int i = 0; i < 10; i++) append(&arr, i * 2);
    printArray(&arr);
    freeArray(&arr);
    printf("\n");

    // --- Associative Array ---
    printf("Associative Array (Hash Map):\n");
    HashMap map = {0};
    insertMap(&map, "apple", 5);
    insertMap(&map, "banana", 7);
    printf("apple: %d\n", getMap(&map, "apple"));
    printf("banana: %d\n", getMap(&map, "banana"));
    deleteMap(&map, "apple");
    printf("apple after delete: %d\n", getMap(&map, "apple")); // -1

    printf("\n");

    // --- Linked List ---
    printf("Linked List:\n");
    Node *head = NULL;
    for (int i = 0; i < 5; i++) push(&head, i);
    printList(head);
    printf("\n");

    // --- Graph ---
    printf("Graph (Adjacency List):\n");
    Graph *graph = createGraph();
    addEdge(graph, 0, 1);
    addEdge(graph, 0, 4);
    addEdge(graph, 1, 2);
    addEdge(graph, 1, 3);
    addEdge(graph, 1, 4);
    printGraph(graph);
    printf("\n");

    // --- Binary Tree ---
    printf("Binary Tree (Inorder Traversal):\n");
    TreeNode *root = NULL;
    int values[] = {5, 3, 8, 1, 4};
    for (int i = 0; i < 5; i++) insertTree(&root, values[i]);
    inorder(root);
    printf("\n");

    return 0;
}
