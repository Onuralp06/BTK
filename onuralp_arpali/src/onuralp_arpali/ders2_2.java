package onuralp_arpali;

import java.util.Scanner;

public class ders2_2 {

	//public static void main(String[] args) {
			
		/*int a = 5 ;
		if (a > 9 )
			System.out.println("Rakam de�il");
		else
			System.out.println("Rakam");*/
		
		//Girilen say� 35' e�itmi kontrol ediniz.
		
		/* a = 25 ;
		if (a == 35) {
			System.out.println("35'e e�ittir.");
		}
		else {
			System.out.println("35'e e�it de�ildir.");
		}
		
		/* if (a==b){
		 * a==b
		 * a!=b
		 * a<b
		 * a>b
		 * a<=b
		 * a>=b
		 * boolean b1 = true;
		 * boolean b2 = false;
		 * if(b1&&b2==1)
		 * if (b1 || b2)
		 *
		 */
		
		public static void main(String[] args) {
			Scanner kb = new Scanner(System.in);
		int a = kb.nextInt() ;
		if (a > 0) {
			System.out.println("say� pozitif");
		}
		else if (a < 0) {
			System.out.println("say� negatif");
		}
		else {
			System.out.println("Say� 0'd�r");
		}

	}

}
