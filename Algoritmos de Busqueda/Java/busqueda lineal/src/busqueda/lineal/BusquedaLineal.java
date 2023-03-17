package busqueda.lineal;

import java.util.Scanner;

public class BusquedaLineal {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int numeros[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12};
        int x, index = 0, position = -1;
        boolean found = false;
        x = sc.nextInt();

        while (!found && index < numeros.length) {
            if (numeros[index] == x) {//va comparando en cada posicion del arreglo
                found = true;
                position = index;
            } else {
                index += 1;
            }
        }
        System.out.println(position);//retorna la posicion
    }
}