// 세 수 - 백준

import java.util.Scanner;
import java.util.Arrays;

class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int[] num = new int[3];
        for(int i = 0 ; i < num.length ; i++){
            num[i] = sc.nextInt();
        }
        sc.close();
        Arrays.sort(num);
        System.out.println(num[1]);
    }
}