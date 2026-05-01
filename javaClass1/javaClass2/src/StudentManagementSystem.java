import java.util.ArrayList;
import java.util.List;
import java.util.Objects;
import java.util.Scanner;

class StudentManagement {
    String name;
    int age;
    double cgpa;
    StudentManagement(String name,int age,double cgpa) {
        this.name = name;
        this.age = age;
        this.cgpa = cgpa;
    }

    void isExcellent() {
        boolean excellent;
        if (cgpa >= 4.5) {
            excellent = true;
        }
        else {
            excellent = false;
        }
    }
}

class StudentManagementTestDrive {
    public static void main(String[] args) {
        List<StudentManagement> temp = new ArrayList<>();
        Scanner sc = new Scanner(System.in);
        boolean run = true;
        while (run) {
            System.out.println("1. Add Student");
            System.out.println("2. View All Students");
            System.out.println("3. Find Best Student");
            System.out.println("4. Search Student by Name");
            System.out.println("5. Exit");
            System.out.print("Choice: ");
            int choice = sc.nextInt();
            String name = null;
            int age = 0;
            double cgpa = 0;
            if (choice == 1) {
                System.out.print("Student Name: ");
                name = sc.next();
                System.out.print("Student Age: ");
                age = sc.nextInt();
                System.out.print("Student CGPA: ");
                cgpa = sc.nextDouble();
                StudentManagement students = new StudentManagement(name, age, cgpa);
                temp.add(students);
            }
            if (choice == 2) {
                for (StudentManagement s : temp) {
                    System.out.println("Name: " + s.name + " Age: " + s.age + " CGPA: " + s.cgpa);
                }
            }
            if (choice == 3) {
                double best = 0;
                String ans = "";
                for (StudentManagement x : temp) {
                    if (x.cgpa > best) {
                        best = x.cgpa;
                        ans = ("Name: " + x.name + " | Age: " + x.age + " | CGPA: " + x.cgpa);
                    }
                }
                System.out.println("Best Student: " + ans);
            }
            if (choice == 4) {
                System.out.print("Enter Name: ");
                String nameSearch = sc.next();
                for (StudentManagement y : temp) {
                    if (Objects.equals(y.name, nameSearch)) {
                        System.out.println("Name: " + y.name + " | Age: " + y.age + " | CGPA: " + y.cgpa);
                    }
                }
            }
            if (choice == 5) {
                run = false;
            }
        }
    }
}