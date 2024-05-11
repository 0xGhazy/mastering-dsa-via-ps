package org.example.tree.binarySearchTree;


import lombok.Data;

@Data
public class TreeNode<T extends Comparable<T>> implements Comparable<TreeNode<T>> {
    private T data;
    public TreeNode<T> left, right, parent;
    boolean isLeft;

    public TreeNode(T data) {
        this.data = data;
        left = right = parent = null;
    }

    private TreeNode() {}

    @Override
    public int compareTo(TreeNode<T> otherNode) {
        // Compare the data of this node with the data of the other node
        return this.data.compareTo(otherNode.data);
    }
}