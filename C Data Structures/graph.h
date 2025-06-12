#ifndef GRAPH_H
#define GRAPH_H

#define MAX_VERTICES 5

typedef struct GNode {
    int vertex;
    struct GNode *next;
} GNode;

typedef struct {
    GNode *adjLists[MAX_VERTICES];
} Graph;

Graph *createGraph();
void addEdge(Graph *graph, int src, int dest);
void printGraph(Graph *graph);

#endif
