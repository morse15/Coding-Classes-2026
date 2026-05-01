import java.util.Scanner;

class Calculator {
    double a;
    double b;

    void add() {
        System.out.println(" ");
        System.out.println("Result: " + (a + b));
    }

    void subtract() {
        System.out.println(" ");
        System.out.println("Result: " + (a - b));
    }

    void multiply() {
        System.out.println(" ");
        System.out.println("Result: " + (a * b));
    }

    void divide() {
        if (b == 0) {
            System.out.println(" ");
            System.out.println("Cannot divide by zero");
        }
        else {
            System.out.println(" ");
            System.out.println("Result: " + (a/b));
        }
    }
}

class CalculatorTestDrive {
    public static void main(String[] args) {
        Calculator g = new Calculator();
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter first number: ");
        g.a = sc.nextInt();
        System.out.print("Enter second number: ");
        g.b = sc.nextInt();

        System.out.println(" ");
        System.out.println("1. Add");
        System.out.println("2. Subtract");
        System.out.println("3. Multiply");
        System.out.println("4. Divide");
        System.out.print("Choose operation: ");
        int choice = sc.nextInt();
        if (choice == 1) {
            g.add();
        }
        if (choice == 2) {
            g.subtract();
        }
        if (choice == 3) {
            g.multiply();
        }
        if (choice == 4) {
            g.divide();
        }
    }
}