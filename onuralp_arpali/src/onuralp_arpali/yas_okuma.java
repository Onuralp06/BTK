package onuralp_arpali;

import java.util.Scanner;

import javax.xml.crypto.dsig.spec.C14NMethodParameterSpec;

public class yas_okuma {

	public static void main(String[] args) {
		Scanner ehliyet = new Scanner (System.in);
		/*System.out.println("L�tfen A�a��daki Sorular� Cevaplay�n�z.");
		System.out.print("L�tfen Ya��n�z� Giriniz : ");
		int yas = ehliyet.nextInt();
		System.out.print("L�tfen Okulunuzu Giriniz : ");
		String okul = ehliyet.next();
		if (yas >= 18 && okul.equalsIgnoreCase("universite"))
			System.out.println("Ehliyet Alabilirsiniz!");
		else if (yas >=18 && !okul.equals("universite"))
			System.out.println("Ya��n�z yeterli ancak universitede de�ilsiniz.");
		else
			System.out.println("Ehliyet Alamazs�n�z");*/
		
		String c1 = hesaplama
		int a = 1 ;
		int b = 10;
		switch (c1)
		{
		case "+":
			System.out.println(a+b);
			break;
		case "-":
			System.out.println(a-b);
			break;
		case "/":
			System.out.println(a/b);
			break;
		case "*":
			System.out.println(a*b);
			break;
		default:
			System.out.println("B�yle bir i�lem tan�ml� de�ildir.");
		}
		
		
		
		

	}

}
