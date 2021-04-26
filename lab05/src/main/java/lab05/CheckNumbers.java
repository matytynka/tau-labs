package lab05;

public class CheckNumbers {
    public int gcdByBruteForce(int n1, int n2) {
        int gcd = 1;
        for (int i = 1; i <= n1 && i <= n2; i++) {
            if (n1 % i == 0 && n2 % i == 0) {
                gcd = i;
            }
        }
        return gcd;
    }
    public boolean isOdd(int n) {
        return n % 2 == 1;
    }

    public String toString(int n) {
        return String.valueOf(n);
    }
}
