package onuralp_arpali;

import java.util.Scanner;

public class ders2_2 {

	//public static void main(String[] args) {
			
		/*int a = 5 ;
		if (a > 9 )
			System.out.println("Rakam deðil");
		else
			System.out.println("Rakam");*/
		
		//Girilen sayý 35' eþitmi kontrol ediniz.
		
		/* a = 25 ;
		if (a == 35) {
			System.out.println("35'e eþittir.");
		}
		else {
			System.out.println("35'e eþit deðildir.");
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
			System.out.println("sayý pozitif");
		}
		else if (a < 0) {
			System.out.println("sayý negatif");
		}
		else {
			System.out.println("Sayý 0'dýr");
		}

	}

}
