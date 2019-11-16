#include "stdio.h"
//by the way don't use conio.h when you only use it for _getch();


//What is a binary tree 
typedef struct NODE
{
    int data; //in your code is info (data is more approriate)
    NODE* left;//for clarity, could do NODE* right, *left;
    NODE* right;  
}NODE; 
//so a NODE need to have left and right
//to access to the tree
struct NODE * root = NULL;

int main(void) //if your main doesn't take any argv or arg
{

}


bool isTreeEmpty(NODE* aTree) 
{
    if (aTree == NULL)
    {
        return true;
    }
    else
        return false;
}


NODE* createABinaryTree(NODE* aBinaryTree)  
{
    //First create a node
    NODE* root = NULL;
    NODE* something = new NODE;
    //a node that = NULL, s1mple is that
    while(isTreeEmpty(aBinaryTree))
    {
        //should add the thing that you read in the file in to the tree
        //you should not 
    }
}


NODE* addANodeToBinaryTree()










