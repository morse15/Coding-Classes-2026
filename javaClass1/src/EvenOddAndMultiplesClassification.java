public class EvenOddAndMultiplesClassification {
    public static void main(String[] args) {
        int y = 1;
        while (y < 51) {
            if (y % 2 == 0) {
                if (y % 3 == 0) {
                    System.out.println(y + "-> EvenMultipleOf3");
                } else {
                    System.out.println(y + "-> Even");
                }
            }
            else {
                if (y % 5 == 0) {
                    System.out.println(y + "-> OddMultipleOf5");
                } else {
                    System.out.println(y +"-> Odd");
                }
            }
            y = y + 1;
        }
    }
}