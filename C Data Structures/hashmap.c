#include "hashmap.h"
#include <stdlib.h>
#include <string.h>

static unsigned int hash(const char *key) {
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
