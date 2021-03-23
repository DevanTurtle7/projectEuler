package Java;

public class Question7 {
    public static void main(String[] args) {
        NthPrime sieve = new NthPrime(100001);
        int target = sieve.getTarget();

        System.out.println(target);
    }
}
