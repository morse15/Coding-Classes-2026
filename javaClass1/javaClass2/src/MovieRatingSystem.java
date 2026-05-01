import java.util.Scanner;

class Movie {
    String title;
    int rating;

    void displayMovie() {
        System.out.println("Title: " + title);
        System.out.println("Rating: " + rating);
    }

    void getCategory() {
        System.out.print("Category: ");
        if (rating >= 8) {
            System.out.print("Excellent");
        }

        else {
            if (rating >= 5) {
                System.out.print("Average");
            }

            else {
                System.out.print("Poor");
            }
        }
    }
}

class TestDrive {
    public static void main(String[] args) {
        Movie e = new Movie();
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter Movie Title: ");
        e.title = sc.nextLine();
        System.out.print("Enter Rating: ");
        e.rating = sc.nextInt();
        e.displayMovie();
        e.getCategory();
    }
}