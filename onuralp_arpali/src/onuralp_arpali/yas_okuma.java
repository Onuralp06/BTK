package onuralp_arpali;

import java.util.Scanner;

import javax.xml.crypto.dsig.spec.C14NMethodParameterSpec;

public class yas_okuma {

	public static void main(String[] args) {
		Scanner ehliyet = new Scanner (System.in);
		/*System.out.println("Lütfen Aþaðýdaki Sorularý Cevaplayýnýz.");
		System.out.print("Lütfen Yaþýnýzý Giriniz : ");
		int yas = ehliyet.nextInt();
		System.out.print("Lütfen Okulunuzu Giriniz : ");
		String okul = ehliyet.next();
		if (yas >= 18 && okul.equalsIgnoreCase("universite"))
			System.out.println("Ehliyet Alabilirsiniz!");
		else if (yas >=18 && !okul.equals("universite"))
			System.out.println("Yaþýnýz yeterli ancak universitede deðilsiniz.");
		else
			System.out.println("Ehliyet Alamazsýnýz");*/
		
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
			System.out.println("Böyle bir iþlem tanýmlý deðildir.");
		}
		
		
		
		

	}

}
