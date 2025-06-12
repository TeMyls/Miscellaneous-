#ifndef BINARY_TREE_H
#define BINARY_TREE_H

typedef struct TreeNode {
    int data;
    struct TreeNode *left, *right;
} TreeNode;

TreeNode *createNode(int data);
void insertTree(TreeNode **root, int data);
void inorder(TreeNode *root);

#endif
