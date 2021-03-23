package Java;

public class Question7 {
    public static void main(String[] args) {
        Sieve sieve = new Sieve(10001);
        int target = sieve.getTarget();
        System.out.println(target);
    }
}
