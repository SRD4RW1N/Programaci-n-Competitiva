package contest;

import java.util.Scanner;

public class Contest {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int n = input.nextInt();
        int k = input.nextInt();
        int d = input.nextInt();
        int s = input.nextInt();
        double x = ((n*d) - (s*k)) / (double) (n - k);
        if (x < 0 || x > 100) {
            System.out.println("impossible");
        } else {
            System.out.printf("%.7f", x);
        }
    }

}
