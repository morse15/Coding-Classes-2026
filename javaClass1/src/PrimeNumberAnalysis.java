import java.util.*;
public class PrimeNumberAnalysis {
    public static void main(String[] args) {
        List<Integer> prime = new ArrayList<>(Arrays.asList(1, 2, 3));
        for(int x = 4;x < 51;x++) {
            if (x % 2 != 0) {
                if (x % 3 != 0) {
                    if (x % 5 != 0) {
                        if (x % 7 != 0) {
                            prime.add(x);
                        }
                    }
                }
            }
        }
        System.out.println("Prime numbers: "+ prime);
        int length = prime.size();
        System.out.println("Amount of primes: "+ length);
        int z = 0;
        for (int y = 0;y < length;y++) {
            z = z + prime.get(y);
        }
        System.out.println("Sum of all primes"+ z);

    }
}