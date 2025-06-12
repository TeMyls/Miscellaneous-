#include "graph.h"
#include <stdio.h>
#include <stdlib.h>

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
