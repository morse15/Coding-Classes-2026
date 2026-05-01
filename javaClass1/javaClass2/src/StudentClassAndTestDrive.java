import java.util.Scanner;

class Student {
    String name;
    int age;
    String department;
    double cgpa;

    void displayInfo() {
        System.out.println("Name:" + name);
        System.out.println("Age:" + age);
        System.out.println("Department:" + department);
        System.out.println("CGPA:" + cgpa);
    }

    void isExcellent() {
        if (cgpa >= 4.5) {
            System.out.println("Status: Excellent Student");
        } else {
            System.out.println("Status: Regular Student");
        }
    }
}

class StudentTestDrive {
    public static void main(String[] args) {
        Student a = new Student();
        a.name = "Favour";
        a.age = 20;
        a.department = "Computer Science";
        a.cgpa = 4.7;
        a.displayInfo();
        a.isExcellent();

        System.out.println(" ");

        Student b = new Student();
        Scanner sc = new Scanner(System.in);
        System.out.println("Name: ");
        b.name = sc.nextLine();
        System.out.println("Age: ");
        b.age = sc.nextInt();
        System.out.println("Department: ");
        b.department = sc.nextLine();
        System.out.println("CGPA: ");
        b.cgpa = sc.nextInt();
        b.displayInfo();
        b.isExcellent();
    }
}