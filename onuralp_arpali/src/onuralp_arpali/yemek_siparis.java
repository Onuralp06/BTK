package onuralp_arpali;

import java.util.Scanner;

public class yemek_siparis {
	
	/*String yemek = siparis.next();
	yemek = yemek.toLowerCase();
	if(yemek.equalsIgnoreCase("lahmacun"))
		System.out.println("Hesab�n�z 15 Lirad�r.");
	else if(yemek.equalsIgnoreCase("hamburger"))
		System.out.println("Hesab�n�z 40 Lirad�r.");
	else if(yemek.equalsIgnoreCase("pizza"))
		System.out.println("Hesab�n�z 55 Lirad�r.");
	else
		System.out.println("L�tfen D�zeltiniz.");*/
	
	public static void main(String[] args) {
		Scanner siparis = new Scanner(System.in);
		System.out.println("L�tfen Sipari�inizi Giriniz: \nLahmacun,Hamburger,Pizza");
	String yemek = siparis.nextLine();
	yemek = yemek.toLowerCase();
	int hesap = 0;
	String temp ="";
	if(yemek.indexOf("lahmacun")!=-1) {
		hesap+=15;
		temp+="lahmacun";
	}
	if(yemek.indexOf("hamburger")!=-1) {
		hesap+=40;
		temp+=" hamburger";
	}
	if(yemek.indexOf("pizza")!=-1) {
		hesap+=35;
		temp+=" pizza";
	}
	System.out.println("Sipari�iniz : "+temp+ " Hesab�n�z: "+hesap);
		

	}

}
