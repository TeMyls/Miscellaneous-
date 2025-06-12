#include "binary_tree.h"
#include <stdio.h>
#include <stdlib.h>

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
