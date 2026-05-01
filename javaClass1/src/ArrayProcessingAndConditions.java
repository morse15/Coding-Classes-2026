import java.util.Arrays;

public class ArrayProcessingAndConditions {
    public static void main(String[] args) {
        int[] numbers = {12, 7, 9, 20, 5, 14, 3, 18};
        System.out.println("The largest number is " + Arrays.stream(numbers).max().getAsInt());
        System.out.println("The smallest number is " + Arrays.stream(numbers).min().getAsInt());
        int countEven = 0;
        int sumMoreThanTen = 0;
        for (int x = 0; x < numbers.length; x++) {
            if (numbers[x] % 2 == 0) {
                countEven = countEven + 1;
            }
            if (numbers[x] > 10) {
                sumMoreThanTen = sumMoreThanTen + numbers[x];
            }
        }
        System.out.println("There are " + countEven + " even numbers");
        System.out.println("The sum of numbers greater than 10 is " + sumMoreThanTen);


    }
}