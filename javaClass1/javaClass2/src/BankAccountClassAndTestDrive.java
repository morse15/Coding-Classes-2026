import java.util.ArrayList;
import java.util.List;
import java.util.Objects;
import java.util.Scanner;

class BankAccount {
    String accountName;
    double balance;
    BankAccount(String accountName,double balance) {
        this.accountName = accountName;
        this.balance = balance;
    }

    void deposit(BankAccount account, double amount) {
        account.balance = account.balance + amount;
        System.out.println("worked");
    }

    void withdraw(double amount) {
        System.out.print(this.balance);
        if (amount > this.balance) {
            System.out.println("Insufficient funds");
        } else {
            this.balance = this.balance - amount;
        }
    }

    void displayBalance() {
        System.out.println("Account: " + this.accountName);
        System.out.println("Balance: " + this.balance);
    }

    void transfer(BankAccount account,BankAccount otherAccount, double amount) {
        if (amount > account.balance) {
            System.out.println("Unsuccessful: Insufficient funds");
        } else {
            account.balance = account.balance - amount;
            otherAccount.balance = otherAccount.balance + amount;
            System.out.println("Successful");
        }
    }
}

//take in input
//view all bank accounts
//find the richest account
class BankAccountTestDrive {
    public static void main(String[] args) {
        List<BankAccount> temp = new ArrayList<>();
        Scanner sc = new Scanner(System.in);
        boolean run = true;
        while (run) {
//            System.out.println("1. Add Account");
//            System.out.println("2. Deposit");
//            System.out.println("3. Withdraw");
//            System.out.println("4. Display Balance");
//            System.out.println("5. Transfer");
//            System.out.println("6. Show all accounts");
//            System.out.println("7. Find richest account");
//            System.out.println("8. Exit");
            System.out.print("Choice: ");
            int choice = sc.nextInt();

            String accountName = "";
            double balance = 0;
            BankAccount customers = new BankAccount(accountName, balance);

            if (choice == 1) {
                System.out.print("Account Name: ");
                customers.accountName = sc.next();
                System.out.print("Balance: ");
                customers.balance = sc.nextInt();
                temp.add(customers);
            }

            if (choice == 2) {
                System.out.print("Account Name: ");
                String name = sc.next();
                System.out.print("Amount: ");
                BankAccount account = null;
                double amount = sc.nextDouble();
                for (BankAccount x : temp) {
                    if (Objects.equals(x.accountName, name)) {
                        account = x;
                    }
                }
                customers.deposit(account,amount);
            }

            if (choice == 3) {
                System.out.print("Account Name: ");
                String name = sc.next();
                System.out.print("Amount: ");
                double amount = sc.nextDouble();
                for (BankAccount y : temp) {
                    if (Objects.equals(y.accountName,name)) {
                        if (amount > y.balance) {
                            System.out.println("Insufficient funds");
                        }
                        else {
                            y.balance = y.balance - amount;
                        }
                    }
                }
            }

            if (choice == 4) {
                System.out.print("Account: ");
                String name = sc.next();
                for (BankAccount z : temp) {
                    if (Objects.equals(z.accountName,name)) {
                        System.out.println("Balance: " + z.balance);
                    }
                }
            }

            if (choice == 5) {
                System.out.print("What is your account: ");
                String name = sc.next();
                System.out.print("What account do you want to transfer to: ");
                String otherAccountName = sc.next();
                BankAccount otherAccount = null;
                BankAccount account = null;
                System.out.print("Amount: ");
                double amount = sc.nextDouble();
                for (BankAccount acc : temp) {
                    if (Objects.equals(acc.accountName, otherAccountName)) {
                        otherAccount = acc;
                    }
                    if (Objects.equals(acc.accountName,name)) {
                        account = acc;
                    }
                }
                customers.transfer(account,otherAccount,amount);

            }

            if (choice == 6) {
                for (BankAccount a : temp) {
                    System.out.println("Account Name: " + a.accountName + " Balance: " + a.balance);
                }
            }

            if (choice == 7) {
                double richest = 0;
                String answer = "";
                for (BankAccount b : temp) {
                    if (b.balance > richest) {
                        richest = b.balance;
                        answer = ("Account Name: " + b.accountName + " Balance: " + b.balance);
                    }
                }
                System.out.println(answer);
            }

            if (choice == 8) {
                run = false;
            }
        }
    }
}