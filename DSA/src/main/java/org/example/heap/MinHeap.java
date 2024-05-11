package org.example.heap;

import java.lang.reflect.Array;

public class MinHeap <T extends Comparable<T>>{
    private T[] data;
    private int size;
    private int capacity = 3;
    private Class<T> heapDataType;



    @SuppressWarnings("unchecked")
    public MinHeap(Class<T> heapDataType) {
        this.heapDataType = heapDataType;
        this.data = (T[]) Array.newInstance(this.heapDataType, this.capacity);
    }

    public int size() {
        return this.size;
    }

    public void insert(T data) {
        if (size == capacity)
            resize();
        int i = size;
        size++;
        this.data[i] = data;
        int parentIndex = getParentIndex(i);
        while (i != 0 && (this.data[i].compareTo(this.data[parentIndex]) < 0) )
        {
            T temp = this.data[i];
            this.data[i] = this.data[parentIndex];
            this.data[parentIndex] = temp;
            i = parentIndex;
            parentIndex = getParentIndex(i);
        }
    }


    public T pop() {
        // handle empty heap case.
        if (this.size == 0) return null;
        int i = 0;
        T dataToBeDeleted = this.data[i];
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
                    this.data[rightIndex].compareTo(this.data[leftIndex]) < 0)
                smallerIndex = rightIndex;

            if (this.data[smallerIndex].compareTo(this.data[i]) >= 0)
                break;

            T temp = this.data[i];
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
        T[] newData = (T[]) Array.newInstance(this.heapDataType, this.capacity);
        for (int i = 0; i < size; i++) {
            newData[i] = this.data[i];
        }
        this.data = newData;
    }
}
