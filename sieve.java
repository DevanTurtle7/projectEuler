import java.util.Arrays;

class sieve {
	public static void main(String[] args) {
		int[] sieve = makeSieve(10);
		System.out.println(Arrays.toString(sieve));
	}

	public static int[] makeSieve(int size) {
		int[] sieve = new int[size];
		
		for (int i = 0; i < size; i++) {
			if (i == 0 || i == 1) {
				sieve[i] = 1;
			} else {
				int multiple = i * 2;

				while (multiple < size) {
					sieve[multiple] = 1;
					multiple += i;
				}
			}
		}
		return sieve;
	}
}
