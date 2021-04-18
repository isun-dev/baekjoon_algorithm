import java.util.Scanner;

public class NumberSort {
    static void swap(int[] arr, int idx1, int idx2) {
        int tmp = arr[idx1];
        arr[idx1] = arr[idx2];
        arr[idx2] = tmp;
    }

    static void quicksort(int[] arr, int left, int right) {
        int pl = left;
        int pr = right;
        int pivot = arr[(left + right) / 2];

        do {
            while (arr[pl] < pivot) pl++;
            while (arr[pr] > pivot) pr--;
            if (pl <= pr) {
                swap(arr, pl++, pr--);
            }
        } while (pl <= pr);
        if (left < pr) {
            quicksort(arr, left, pr);
        }
        if (pl < right) {
            quicksort(arr, pl, right);
        }
    }


    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];

        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }

        quicksort(arr, 0, n - 1);

        for (int i = 0; i < n; i++) {
            System.out.println(arr[i]);
        }
    }
}
