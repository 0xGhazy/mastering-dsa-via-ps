package org.example;

public class Main {
    public static void main(String[] args) {

        int[] arr1 = {1,4,2};
        int[] arr2 = {5,4,4};
        int[] arr3 = {5,0,0};

        if (fillCups(arr1) == 4)
            System.out.println("Pass 1");
        else if (fillCups(arr2) == 7)
            System.out.println("Pass 2");
        else if (fillCups(arr3) == 5)
            System.out.println("Pass 3");

    }

    public static int fillCups(int[] amount) {
        int result = 0;
        byte zerosCount = 0;
        int maxNumber = 0;

        for(int i = 0; i < 3; i++)
        {
            if (amount[i] == 0)
                zerosCount += 1;
            maxNumber = Math.max(maxNumber, amount[i]);
        }

        if (zerosCount == 2 || zerosCount == 3)
            return maxNumber;

        return result;
    }
}