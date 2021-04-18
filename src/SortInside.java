// 2021년 4월 18일
// 백준 1427번 소트인사이드
// 문제: 주어진 수를 내림차순으로 정렬해서 출력.

import java.io.*;
import java.util.Arrays;

public class SortInside {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        char[] n = br.readLine().toCharArray(); // char형 배열로 변환
        Arrays.sort(n);
        for (int i = n.length - 1; i >= 0; i--) {
            System.out.print(n[i]);
        }

    }

}
