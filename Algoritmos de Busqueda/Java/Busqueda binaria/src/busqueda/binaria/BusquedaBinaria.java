package busqueda.binaria;

import java.util.Scanner;

public class BusquedaBinaria {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int numeros[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12};
        boolean found = false;
        int first = 0, position = -1, middle, x;
        int last = (numeros.length) - 1;
        x = sc.nextInt();

        while (found == false && first <= last) {
            middle = (int) Math.floor((first + last) / 2); //encuentra el pivote
            if (numeros[middle] == x) {//compara el pivote
                found = true;
                position = middle;
            } else if (numeros[middle] > x) {
                last = middle - 1;
            } else {                    
                first = middle + 1;
            }
        }
        System.out.println(position); //retorna la posicion
    }

}