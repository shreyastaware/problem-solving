import java.util.*;
import java.math.*;

public class drawing_book {

    public static int solve(int n, int p) {
        int front = p >> 1;
        int back =  ((n & 1) == 1) 
                    ? (n - p) >> 1 // odd number of pages
                    : (n - p + 1) >> 1; // even number of pages

        return Math.min(front, back);
    }
    
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();
        int p = scan.nextInt();
        scan.close();
        
        System.out.println(solve(n, p));
    }
}