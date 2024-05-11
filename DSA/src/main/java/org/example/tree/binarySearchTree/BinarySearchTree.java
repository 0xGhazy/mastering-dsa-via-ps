package org.example.tree.binarySearchTree;


import lombok.Data;

import java.util.LinkedList;
import java.util.Queue;

/**
 * A generic binary search tree implementation that supports nodes of type T that implements the Comparable interface.
 *
 * @param <T> the type of data stored in the binary search tree
 */ 
public class BinarySearchTree<T extends Comparable<T>> {


    @Data
    private class NodeAndParent{
        TreeNode<T> node;
        TreeNode<T> parent;
        boolean isLeftNode;

        @Override
        public String toString() {
            return "NodeAndParent{" +
                    "node=" + node.getData() +
                    ", parent=" + parent.getData() +
                    ", isLeftNode=" + isLeftNode +
                    '}';
        }
    }
    private TreeNode<T> root;



    /**
     * Inserts a new node with the given data into the binary search tree.
     *
     * @param data the data to insert
     */
    public void insert(T data) {
        TreeNode<T> newNode = new TreeNode<>(data);
        if (root == null) {
            root = newNode;
            return;
        }

        TreeNode<T> current = root;
        while (true) {
            int compareResult = data.compareTo(current.getData());
            if (compareResult < 0) {
                if (current.getLeft() == null) {
                    current.setLeft(newNode);
                    break;
                }
                current = current.getLeft();
            } else {
                if (current.getRight() == null) {
                    current.setRight(newNode);
                    break;
                }
                current = current.getRight();
            }
        }
    }

    /**
     * Calculates the height of the tree.
     *
     * @return the height of the tree
     */
    public int height() {
        return _internalHeight(root);
    }

    /**
     * Searches for a node with the specified data in the binary search tree.
     *
     * @param data the data to search for
     * @return the node with the specified data, or null if the node is not found
     */
    public TreeNode<T> find(T data) {
        TreeNode<T> current = root;
        while (current!= null) {
            int compareResult = data.compareTo(current.getData());
            if (compareResult == 0)
                return current;
            else if (compareResult < 0)
                current = current.getLeft();
            else
                current = current.getRight();
        }
        return null;
    }


    private NodeAndParent findNodeAndParent(T _data) {
        TreeNode<T> current = this.root;
        TreeNode<T> parent = null;
        NodeAndParent nodeAndParent = new NodeAndParent();
        boolean isLeft = false;
        while (current!= null) {
            int compareResult = _data.compareTo(current.getData());
            if (compareResult == 0){
                nodeAndParent.node = current;
                nodeAndParent.parent = parent;
                nodeAndParent.isLeftNode = isLeft;
                break;
            }
            else if (compareResult < 0){
                parent = current;
                isLeft= true;
                current = current.getLeft();
            }
            else{
                parent = current;
                isLeft= false;
                current = current.getRight();
            }
        }
        return nodeAndParent;
    }

    public void delete(T data) {
        NodeAndParent target = findNodeAndParent(data);
        TreeNode<T> current = target.getNode();
        if (current == null) return;

        if (current.getLeft() != null && current.getRight() != null)
            hasTwoChild(current);
        else if (current.getLeft() != null ^ current.getRight() != null)
            hasOneChild(current);
        else
            hasNoChild(target);
    }




    public void printLevelOrder() {
        if (root == null) {
            return;
        }

        Queue<TreeNode<T>> queue = new LinkedList<>();
        queue.offer(root);

        while (!queue.isEmpty()) {
            int levelNodes = queue.size();

            for (int i = 0; i < levelNodes; i++) {
                TreeNode<T> current = queue.poll();
                System.out.print(current.getData() + " ");

                if (current.getLeft() != null) {
                    queue.offer(current.getLeft());
                }

                if (current.getRight() != null) {
                    queue.offer(current.getRight());
                }
            }

            System.out.println(); // Move to the next level
        }
    }




    /**
     * Performs a pre-order traversal of the tree, printing the data of each node.
     */
    public void preorder() {
        _internalPreorder(root);
    }



    /**
     * Performs an in-order traversal of the tree, printing the data of each node.
     */
    public void inorder() {
        _internalInorder(root);
    }



    /**
     * Performs a post-order traversal of the tree, printing the data of each node.
     */
    public void postorder() {
        _internalPostorder(root);
    }



    /**
     * A helper method for performing a pre-order traversal of the tree.
     *
     * @param node the root of the subtree to be traversed
     */
    private void _internalPreorder(TreeNode<T> node) {
        if (node == null) {
            return;
        }
        System.out.print(node.getData() + " ");
        _internalPreorder(node.getLeft());
        _internalPreorder(node.getRight());
    }



    /**
     * A helper method for performing an in-order traversal of the tree.
     *
     * @param node the root of the subtree to be traversed
     */
    private void _internalInorder(TreeNode<T> node) {
        if (node == null) {
            return;
        }
        _internalInorder(node.getLeft());
        System.out.print(node.getData() + " ");
        _internalInorder(node.getRight());
    }



    /**
     * A helper method for performing a post-order traversal of the tree.
     *
     * @param node the root of the subtree to be traversed
     */
    private void _internalPostorder(TreeNode<T> node) {
        if (node == null) {
            return;
        }
        _internalPostorder(node.getLeft());
        _internalPostorder(node.getRight());
        System.out.print(node.getData() + " ");
    }



    /**
     * A helper method for calculating the height of the tree.
     *
     * @param node the root of the subtree to be measured
     * @return the height of the subtree
     */
    private int _internalHeight(TreeNode<T> node) {
        if (node == null) {
            return 0;
        }
        return 1 + Math.max(_internalHeight(node.getLeft()), _internalHeight(node.getRight()));
    }



    private void hasTwoChild(TreeNode<T> nodeToDelete) {
        TreeNode<T> current = nodeToDelete.getRight();
        TreeNode<T> parent = null;
        // find the smallest node
        while (current.getLeft() != null)
        {
            parent = current;
            current = current.getLeft();
        }
        if (parent != null)
            parent.setLeft(current.getRight());
        else
            nodeToDelete.setRight(current.getRight());
        nodeToDelete.setData(current.getData());
    }


    private void hasOneChild(TreeNode<T> nodeToDelete) {
        TreeNode<T> nodeToReplace;
        if (nodeToDelete.getLeft() != null)
            nodeToReplace = nodeToDelete.getLeft();
        else
            nodeToReplace = nodeToDelete.getRight();
        nodeToDelete.setData(nodeToReplace.getData());
        nodeToDelete.setLeft(nodeToReplace.getLeft());
        nodeToDelete.setRight(nodeToReplace.getRight());
    }



    private void hasNoChild(NodeAndParent nodeAndParent) {
        if (nodeAndParent.parent == null)
            root = null;
        else {
            if (nodeAndParent.isLeftNode())
                nodeAndParent.getParent().setLeft(null);
            else
                nodeAndParent.getParent().setRight(null);
        }
    }

}
