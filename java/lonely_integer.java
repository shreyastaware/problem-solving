import java.util.*;

public class lonely_integer {
    
    public static int lonelyInteger(int[] a) {
        
        int result = 0;
        
        for(int i : a) {
            result = result ^ i;
        }
        
        return result;
    }
    
    public static void main(String[] args) {
        
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int[] a = new int[n];
        
        for (int i = 0; i < n; i++) {
            a[i] = scanner.nextInt();
        }
        
        scanner.close();
        
        System.out.println(lonelyInteger(a));
        
    }
}
