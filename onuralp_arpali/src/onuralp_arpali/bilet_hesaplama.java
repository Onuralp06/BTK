package onuralp_arpali;

import java.util.Scanner;

public class bilet_hesaplama {

	public static void main(String[] args) {
		Scanner kb = new Scanner (System.in);
		System.out.print("Lütfen Yaþýnýzý Giriniz: ");
		int yas = kb.nextInt();
		if (yas >0 && yas < 18)
			System.out.println("Öðrenci Bileti");
		else if (yas >18 && yas < 65)
			System.out.println("Tam Bilet");
		else if (yas >65)
			System.out.println("65 Yaþ Bilet");
		else
			System.out.println("Yaþ Negatif Olamaz.");

	}

}
