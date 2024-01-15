package u1;

public class Funciones {

	public static int Sumatoria(int n) {
		return (int) (n * (n + 1) / 2);
	}

	public static int Factorial(int n) {
		int total;
		total = 1;
		for (int i = 1; i <= n; i++)
			total = total * i;
		return total;
	}

	public static int[] Ordena(int[] vec) {
		int i, j, n;
		int x, y;
		int sal[];
		n = vec.length;
		sal = new int[n];
		for (i = 0; i <= n - 1; i++)
			sal[i] = vec[i];
		
		for (i = 0; i <= n - 2; i++)
			for (j = 0; j <= n - 2; j++) {
				x = sal[j];
				y = sal[j + 1];
				// if (x.compareTo(y) > 0) {
				if (x > y) {
					sal[j] = y;
					sal[j + 1] = x;
				}
			}
		return sal;
	}

	public static int[] Inverso(int[] vec) {
		int i, n;
		int sal[];
		n = vec.length;
		sal = new int[n];
		for (i = 0; i <= n - 1; i++)
			sal[n - i - 1] = vec[i];
		return sal;
	}

	public static int Max(int vec[]) {
		int n, mayor;
		n = vec.length;
		mayor = 0;
		for (int i = 0; i <= n - 1; i++)
			if (vec[i] > mayor)
				mayor = vec[i];
		return mayor;
	}

	public static int Min(int vec[]) {
		int n, menor;
		n = vec.length;
		menor = vec[0];
		for (int i = 0; i <= n - 1; i++)
			if (vec[i] < menor)
				menor = vec[i];
		return menor;
	}

	public static double promedio(int vec[]) {
		int sum = 0;
		double prom;
		int n = vec.length;
		for (int i = 0; i <= n - 1; i++)
			sum = sum + vec[i];
		prom = sum / (double) n;
		return prom;
	}

	static String Dec2Bin(int N) {
		int iRes;
		String sBin;
		sBin = Integer.toBinaryString(N);
		sBin = "";
		while (N > 0) {
			iRes = N % 2;
			N /= 2;
			sBin = Integer.toString(iRes) + sBin;
		}
		return sBin;
	}

	static int Bin2Dec(String sBin) {
		char cDig;
		int i, L, iDig, suma = 0, base = 1;
		sBin = " " + sBin; // agrega un blanco
		L = sBin.length() - 1;
		for (i = 1; i <= L; i++) {
			cDig = sBin.charAt(L - i + 1);
			iDig = Character.getNumericValue(cDig);
			suma = suma + (iDig * base);
			base = base * 2;
		}
		return suma;
	}

	static String Dec2Rom(int iNum) {
		String sUni[] = { "", "I", "II", "III", "IV", "V", "VI", "VII", "VIII",
				"IX" };
		String sDec[] = { "", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX",
				"XC" };
		String sCen[] = { "", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC",
				"CM" };
		int iDig, L, Pos, i;
		char caracter;
		String sNum, sChar, sRom;

		sNum = Integer.toString(iNum);

		caracter = sNum.charAt(0);
		sChar = Character.toString(caracter);
		iDig = Character.getNumericValue(caracter);
		L = sNum.length();

		for (i=1; i<=3-L; i++) {
			sNum = "0" + sNum;
		}
/*		
		while (L != (int) (L / 3 * 3)) {
			sNum = "0" + sNum;
			L = sNum.length();
		}
*/		
		Pos = 0;
		sRom = "";
		for (i = 0; i <= 2; i++) {
			iDig = Character.getNumericValue(sNum.charAt(i));
			if (iDig > 0) {
				switch (i) {
				case 0:
					sRom = sRom + sCen[iDig];
					break;
				case 1:
					sRom = sRom + sDec[iDig];
					break;
				case 2:
					sRom = sRom + sUni[iDig];
					break;
				}
			}
		}
		return sRom;
	}

	static boolean esprimo(int iNum) {
		int divisor = 2;
		boolean primo = true;
		do {
			primo = (iNum % divisor) != 0;
			divisor++;
		} while (divisor < iNum && primo);
		return primo;
	}

	public static int Max(int a, int b) {
		int mayor;
		if (a > b)
			mayor = a;
		else
			mayor = b;
		return mayor;
	}

}