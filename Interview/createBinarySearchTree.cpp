//
//  createBinarySearchTree.cpp
//  BinarySearchTree
//
//  Created by LiuFangGuo on 9/16/18.
//  Copyright © 2018 LiuFangGuo. All rights reserved.
//

//#include <stdio.h>
//  完成二叉树的创建
//  第一步：定义数据结构。
//  规范：1.1 前三个字母+下划线是 struct 的定义；1.2 最终的缩写是，最终的定义
//  使用中序遍历做测试。。

#include <iostream>
using namespace std;

typedef struct Bin_Search_Tree {
    int data;
    Bin_Search_Tree* left;
    Bin_Search_Tree* right;
} BinSearchTree;

BinSearchTree* ConstructTree(BinSearchTree* root, int value){
    //创建新的节点
    BinSearchTree* node = new BinSearchTree;
    node->data = value;
    node->left = NULL;
    node->right = NULL;
    //插入节点
    if (root == NULL) {
        root = node;
    } else {
        //查找节点合适的位置。
        BinSearchTree* temp = root;
        BinSearchTree* insertParent = root;
        while (temp != NULL) {
            while (temp != NULL && value < temp->data ) {
                insertParent = temp;
                temp = temp->left;
            }
            while (temp != NULL && value >= temp->data) {
                insertParent = temp;
                temp = temp->right;
            }
        }
        //这里的时候，其实已经到达插入节点的位置了。只需要二次判断一下就好
        if (value < insertParent->data) {
            insertParent->left = node;
        } else {
            insertParent->right = node;
        }
    }
    
    return root;
}

//二叉搜索树，中序遍历输出，有序数组。。
void MiddleOrderTraversal(BinSearchTree* root){
    if (root != NULL) {
        MiddleOrderTraversal(root->left);
        //先遍历左子树，然后是访问节点数据，最后遍历右子树.
        cout<<root->data<<endl;
        MiddleOrderTraversal(root->right);
    }
}

int main(){
    cout<<"测试代码"<<endl;
    BinSearchTree* tree = NULL;
    int dataArray[] = {5,6,1,2,3,4,7,8,9,10};
    for (int i = 0; i < sizeof(dataArray)/sizeof(int); i++) {
        tree = ConstructTree(tree, dataArray[i]);
    }
    MiddleOrderTraversal(tree);
}