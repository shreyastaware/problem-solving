import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class permuting_two_arrays {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int q = scan.nextInt();
        
        while(q-- > 0) {
            int n = scan.nextInt();
            int k = scan.nextInt();
            boolean doesPermute = true;
            int[] a = new int[n];
            int[] b = new int[n];
            
            for(int i = 0; i < n; i++) {
                a[i] = scan.nextInt();
            }
            
            for(int i = 0; i < n; i++) {
                b[i] = scan.nextInt();
            }
            
            Arrays.sort(a);
            Arrays.sort(b);
            
            for(int i = 0, j = b.length - 1; i < n; i++, j--) {
                if(a[i] + b[j] < k) {
                    doesPermute = false;
                    break;
                }
            }
            
            System.out.println( (doesPermute) ? "YES" : "NO" );
        }
        
        scan.close();
    }
}