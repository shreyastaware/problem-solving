import java.util.*;

public class minimum_absolute_difference_in_an_array {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int[] a = new int[n];
        for(int arr_i=0; arr_i < n; arr_i++){
            a[arr_i] = in.nextInt();
        }
        in.close();
        
        Arrays.sort(a);
        int minDiff = a[n - 1] - a[0];
        for (int i = 0; i < n - 1; i++) {
            int tmpDiff = a[i + 1] - a[i];
            if (tmpDiff < minDiff) {
                minDiff = tmpDiff;
            }
        }
        
        System.out.println(minDiff);
    }
}
