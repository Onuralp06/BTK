package onuralp_arpali;

import java.util.Scanner;

public class bilet_hesaplama {

	public static void main(String[] args) {
		Scanner kb = new Scanner (System.in);
		System.out.print("L�tfen Ya��n�z� Giriniz: ");
		int yas = kb.nextInt();
		if (yas >0 && yas < 18)
			System.out.println("��renci Bileti");
		else if (yas >18 && yas < 65)
			System.out.println("Tam Bilet");
		else if (yas >65)
			System.out.println("65 Ya� Bilet");
		else
			System.out.println("Ya� Negatif Olamaz.");

	}

}
