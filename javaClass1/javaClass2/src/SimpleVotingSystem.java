import java.util.Scanner;

class Candidate {
    String name1;
    String name2;
    int vote1;
    int vote2;
    String winner;

    void addVote1() {
     vote1 = vote1 + 1;
    }

    void addVote2() {
        vote2 = vote2 + 1;
    }

    void displayVotes() {
        System.out.println(" ");
        System.out.println(name1 + ": " + vote1 + " votes");
        System.out.println(name2 + ": " + vote2 + " votes");
        if (vote1 > vote2) {
            winner = name1;
        }
        if (vote2 > vote1) {
            winner = name2;
        }
        if (vote1 == vote2) {
            winner = ("Draw");
        }
        System.out.println("Winner: " + winner);
        System.out.println(" ");
    }
}

class VotingTestDrive {
    public static void main(String[] args) {
        boolean run = true;
        Candidate f = new Candidate();
        Scanner sc = new Scanner(System.in);
        System.out.print("Who's the first candidate: ");
        f.name1 = sc.nextLine();
        System.out.print("Who's the second candidate: ");
        f.name2 = sc.nextLine();

        while (run) {
            System.out.println(" ");
            System.out.println("1. Vote " + f.name1);
            System.out.println("2. Vote " + f.name2);
            System.out.println("3. Show Results");
            System.out.println("4. Exit");
            System.out.print("Choice: ");
            int choice = sc.nextInt();
            if (choice == 1) {
                f.addVote1();
            }
            if (choice == 2) {
                f.addVote2();
            }
            if (choice == 3) {
                f.displayVotes();
            }
            if (choice == 4) {
                run = false;
            }
        }
    }
}