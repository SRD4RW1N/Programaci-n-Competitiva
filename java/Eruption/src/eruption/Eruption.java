
package eruption;

import java.util.Scanner;

public class Eruption {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
    int a = sc.nextInt();
    double pi = Math.PI;
    double l = 2 * pi * Math.sqrt(a / pi);
        System.out.printf("%.9f", l);
        sc.close();
    }
    
}
