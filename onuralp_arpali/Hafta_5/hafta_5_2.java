package ders_4;

import java.util.Scanner;

public class hafta_5_2 {

	public static void main(String[] args) {
		int []array;
		Scanner onur = new Scanner(System.in);
		int elemanSayisi = onur.nextInt();
		array = new int[elemanSayisi];
		
		for(int i=0; i<array.length; i++) {
			System.out.println("L�tfen not giriniz: ");			
			array[i] = onur.nextInt();
		}
		int toplam = 0;
		for(int i=0; i<array.length; i++) {
			System.out.println(i+".��rencinin notu: "+array[i]);
			toplam+= array[i];
		}
		double ort = (double)toplam / elemanSayisi;
		System.out.println("Ortalama: "+ort);
	}

}

