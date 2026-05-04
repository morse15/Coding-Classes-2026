import java.util.*;

class PersonalExpenseTracker {
    Scanner sc = new Scanner(System.in);
    List<PersonalExpenseTracker> customers = new ArrayList<>();
    String expenseName;
    double amount;
    String category;
    PersonalExpenseTracker(String expenseName, double amount, String category) {
        this.expenseName = expenseName;
        this.amount = amount;
        this.category = category;
    }

    void addExpense() {
        System.out.print("Expense Name: ");
        this.expenseName = sc.nextLine();
        System.out.print("Amount: ");
        this.amount = sc.nextDouble();
        sc.nextLine();
        System.out.println("Categories: Food, Transport, Entertainment, Health, Other");
        System.out.print("Category: ");
        this.category = sc.next();
        sc.nextLine();
        PersonalExpenseTracker temp = new PersonalExpenseTracker(this.expenseName,this.amount,this.category);
        customers.add(temp);
    }

    void viewAll() {
        System.out.println("--- All Expenses ---");
        System.out.println("Name      | Category     | Amount");
        for (PersonalExpenseTracker x : customers) {
            System.out.println(x.expenseName + "  | " + x.category + "  | $" + String.format("%.2f",x.amount));
        }
    }

    void totalSpending() {
        double total = 0;
        for (PersonalExpenseTracker y : customers) {
            total = total + y.amount;
        }
        System.out.println("Total Spending: " + String.format("%.2f" , total));
    }

    void breakdown() {
        double foodSum = 0;
        double transportSum = 0;
        double entertainmentSum = 0;
        double healthSum = 0;
        double otherSum = 0;
        for (PersonalExpenseTracker z : customers) {
            if (Objects.equals(z.category.toLowerCase(), "food")) {
                foodSum = foodSum + z.amount;
            }
            if (Objects.equals(z.category.toLowerCase(), "transport")) {
                transportSum = transportSum + z.amount;
            }
            if (Objects.equals(z.category.toLowerCase(), "entertainment")) {
                entertainmentSum = entertainmentSum + z.amount;
            }
            if (Objects.equals(z.category.toLowerCase(), "health")) {
                healthSum = healthSum + z.amount;
            }
            if (Objects.equals(z.category.toLowerCase(), "other")) {
                otherSum = otherSum + z.amount;
            }
        }
        System.out.println("--- Spending by Category ---");
        System.out.println("Food: " + String.format("%.2f", foodSum));
        System.out.println("Transport: " + String.format("%.2f",transportSum));
        System.out.println("Entertainment: " + String.format("%.2f", entertainmentSum));
        System.out.println("Health: " + String.format("%.2f",healthSum));
        System.out.println("Other: " + String.format("%.2f",otherSum));
    }

    void mostExpensive () {
        double expensive = 0;
        String ans = "";
        for (PersonalExpenseTracker a : customers) {
            if (a.amount > expensive) {
                expensive = a.amount;
                ans = (a.expenseName + "   | " + a.category + "  | " + String.format("%.2f", a.amount));
            }
        }
        System.out.println("--- Most Expensive Item ---");
        System.out.println(ans);
    }
}

class ExpenseTestDrive {
    public static void main(String[] args) {
        //title
        System.out.println("===Personal Expense Tracker===");
        boolean run = true;
        Scanner sc = new Scanner(System.in);
        List<PersonalExpenseTracker> customers = new ArrayList<>();
        PersonalExpenseTracker test = new PersonalExpenseTracker("", 0.00, "");

        while (run) {
            //menu
            System.out.println("1. Add Expense");
            System.out.println("2. View All Expenses");
            System.out.println("3. Total Spending");
            System.out.println("4. Breakdown by Category");
            System.out.println("5. Most Expensive Item");
            System.out.println("6. Exit");
            System.out.print("Choice: ");
            int choice = sc.nextInt();

            if (choice == 1) {
                //add expense
                test.addExpense();
            }
            if (choice == 2) {
                //view all expenses
                test.viewAll();
            }

            if (choice == 3) {
                //total spending
                test.totalSpending();
            }

            if (choice == 4) {
                //breakdown by category
                test.breakdown();
            }

            if (choice == 5) {
                //most expensive item
                test.mostExpensive();
            }

                if (choice == 6) {
                    run = false;
                }
            }
        }
    }