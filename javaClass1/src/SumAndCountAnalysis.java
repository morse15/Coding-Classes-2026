public class SumAndCountAnalysis {
    public static void main(String[] args) {
        int z = 1;
        int evenSum = 0;
        int oddSum = 0;
        int CountOfMultiplesOfSeven = 0;
        while (z < 101) {
            if (z % 2 == 0) {
                evenSum = evenSum + z;
            }
            if (z % 2 != 0) {
                oddSum = oddSum + z;
            }
            if (z % 7 == 0) {
                CountOfMultiplesOfSeven = CountOfMultiplesOfSeven + 1;
            }
            z = z + 1;
        }
        System.out.println("Sum of even numbers from 1-100: " + evenSum);
        System.out.println("Sum of odd numbers : " + oddSum);
        System.out.println("Numbers divisible by 7 : " + CountOfMultiplesOfSeven);
    }
    }
