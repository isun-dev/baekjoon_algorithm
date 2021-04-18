import java.util.Scanner;

class Atm {
    static void sort_bank(int[] arr, int n) {
        // 선택 정렬
        for (int i = 0; i < n - 1; i++) {
            // 작은값을 담는 변수를 선언한다.

            for (int j = i + 1; j < n; j++) {
                if (arr[j] < arr[i]) {
                    int tmp = arr[j];
                    arr[j] = arr[i];
                    arr[i] = tmp;
                }

            }
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];

        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }

        sort_bank(arr, n);

        int sum = 0;
        int prev = 0;
        for (int i = 0; i < n; i++) {
            sum += prev + arr[i];
            prev += arr[i];
        }
        System.out.println(sum);
    }
}