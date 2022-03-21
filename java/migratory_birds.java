import java.util.*;

public class migratory_birds {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int[] types = new int[n];
        for(int arr_i=0; arr_i < n; arr_i++){
            types[arr_i] = in.nextInt();
        }
        int[] frequencies = new int[6]; //A
        for (int i = 0; i < types.length; i++) { //B
            frequencies[types[i]] += 1; //C
        }
        int mostCommon = 0;
        for (int i = 1; i < frequencies.length; i++) { //D
            if (frequencies[mostCommon] < frequencies[i]) {
                mostCommon = i; //E
            }
        }
        System.out.println(mostCommon);
    }
}
