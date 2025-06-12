#ifndef HASHMAP_H
#define HASHMAP_H

#define TABLE_SIZE 10

typedef struct Entry {
    char *key;
    int value;
    struct Entry *next;
} Entry;

typedef struct {
    Entry *buckets[TABLE_SIZE];
} HashMap;

void insertMap(HashMap *map, const char *key, int value);
int getMap(HashMap *map, const char *key);

#endif
