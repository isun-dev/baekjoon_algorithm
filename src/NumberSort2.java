import java.util.*;
import java.io.*;

// 2021년 4월 18일.
// 수 정렬하기 2
public class NumberSort2 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(
                new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(
                new OutputStreamWriter(System.out)
        );

        int n = Integer.parseInt(br.readLine());

        // 리스트를 만든다.
        ArrayList<Integer> list = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            list.add(Integer.parseInt(br.readLine()));
        }

        Collections.sort(list);

        for (int value : list) {
           bw.write(value + "\n");
        }

        bw.flush();
        br.close();
        bw.close();
    }
}
