package org.example.PriorityQueue;

import lombok.AllArgsConstructor;
import lombok.Data;

import java.lang.reflect.Array;

public class PriorityQueue <T extends Comparable<T>> {
    private QueueNode<T>[] data;
    private int size;
    private int capacity = 3;
    private final Class<T> heapDataType;


    @SuppressWarnings("unchecked")
    public PriorityQueue(Class<T> heapDataType) {
        this.heapDataType = heapDataType;
        this.data = (QueueNode<T>[]) Array.newInstance(QueueNode.class, this.capacity);
    }

    public int size() {
        return this.size;
    }

    public void print() {
        for (int i = 0; i < this.size; i++) {
            System.out.print("[" + this.data[i].priority + "] " + this.data[i].data + " - ");
        }
    }

    public void insert(int priority, T data) {
        if (size == capacity)
            resize();
        int i = size;
        size++;
        this.data[i] = new QueueNode<T>(priority, data);
        int parentIndex = getParentIndex(i);
        while (i != 0 && (this.data[i].priority < this.data[parentIndex].priority))
        {
            QueueNode<T> temp = this.data[i];
            this.data[i] = this.data[parentIndex];
            this.data[parentIndex] = temp;
            i = parentIndex;
            parentIndex = getParentIndex(i);
        }
    }


    public QueueNode<T> pop() {
        // handle empty heap case.
        if (this.size == 0) return null;
        int i = 0;
        QueueNode<T> dataToBeDeleted = this.data[i];
        this.data[i] = this.data[size - 1];
        this.data[size - 1] = null; // Remove data
        this.size--;

        int leftIndex = getLeftIndex(i);
        while (leftIndex < this.size)
        {
            int rightIndex = getRightIndex(i);
            leftIndex = getLeftIndex(i);
            int smallerIndex = leftIndex;

            if (this.data[rightIndex] != null &&
                    this.data[rightIndex].priority < this.data[leftIndex].priority)
                smallerIndex = rightIndex;
            
            if (this.data[smallerIndex].priority >= this.data[i].priority)
                break;

            QueueNode<T> temp = this.data[i];
            this.data[i] = this.data[smallerIndex];
            this.data[smallerIndex] = temp;
            i = smallerIndex;
            leftIndex = getLeftIndex(i);
        }
        return dataToBeDeleted;
    }

    //////////////////////////////////////////////////
    // The following methods are the helper methods //
    //////////////////////////////////////////////////

    private int getLeftIndex(int i){ return (2 * i) + 1; }

    private int getRightIndex(int i){ return (2 * i) + 2; }

    private int getParentIndex(int i){ return (int) Math.floor((i-1) / 2); }

    @SuppressWarnings("unchecked")
    private void resize() {
        this.capacity *= (int) (capacity * 1.5);
        QueueNode<T>[] newData = (QueueNode<T>[]) Array.newInstance(QueueNode.class, this.capacity);
        for (int i = 0; i < size; i++) {
            newData[i] = this.data[i];
        }
        this.data = newData;
    }

    @Data
    private static class QueueNode <T>{
        public Integer priority;
        public T data;

        public QueueNode(Integer priority, T data) {this.priority = priority; this.data = data;}
    }
}



