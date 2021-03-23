package Java;

import java.util.ArrayList;
import java.util.List;

public class Sieve {
    private int target;
    private List<Integer> primes;

    public Sieve(int target) {
        this.target = target;
        this.primes = new ArrayList<>();
        for (int i = 2; i < 4; i++) {primes.add(i);};

        generateSieve();
    }

    private void generateSieve() {
        int current = 4;

        while (this.primes.size() < this.target) {
            boolean isPrime = true;

            for (int prime : this.primes) {
                if (current % prime == 0) {
                    isPrime = false;
                    break;
                }
            }

            if (isPrime) {
                this.primes.add(current);
            }

            current++;
        }
    }

    public int getTarget() {
        return this.primes.get(this.primes.size() - 1);
    }
}
