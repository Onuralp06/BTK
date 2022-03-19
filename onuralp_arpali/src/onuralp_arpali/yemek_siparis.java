package onuralp_arpali;

import java.util.Scanner;

public class yemek_siparis {
	
	/*String yemek = siparis.next();
	yemek = yemek.toLowerCase();
	if(yemek.equalsIgnoreCase("lahmacun"))
		System.out.println("Hesabýnýz 15 Liradýr.");
	else if(yemek.equalsIgnoreCase("hamburger"))
		System.out.println("Hesabýnýz 40 Liradýr.");
	else if(yemek.equalsIgnoreCase("pizza"))
		System.out.println("Hesabýnýz 55 Liradýr.");
	else
		System.out.println("Lütfen Düzeltiniz.");*/
	
	public static void main(String[] args) {
		Scanner siparis = new Scanner(System.in);
		System.out.println("Lütfen Sipariþinizi Giriniz: \nLahmacun,Hamburger,Pizza");
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
	System.out.println("Sipariþiniz : "+temp+ " Hesabýnýz: "+hesap);
		

	}

}
