import java.util.*;

public class counting_sort {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();
        char[] hike = scan.next().toCharArray();
        
        int count = 0;
        int altitude = 0;
        
        for(char c : hike) {
            // Step up
            if(c == 'U') {
                if(altitude == -1) {
                    count++;
                }
                altitude++;
            }
            // Step down
            else {
                altitude--;
            }
        }

        scan.close();
        
        System.out.println(count);
    }
}