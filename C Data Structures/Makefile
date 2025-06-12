CC = gcc
CFLAGS = -Wall -g
OBJS = main.o dynamic_array.o hashmap.o linked_list.o graph.o binary_tree.o

all: datastructures

datastructures: $(OBJS)
	$(CC) -o datastructures $(OBJS)

%.o: %.c
	$(CC) $(CFLAGS) -c $<

clean:
	rm -f *.o datastructures
