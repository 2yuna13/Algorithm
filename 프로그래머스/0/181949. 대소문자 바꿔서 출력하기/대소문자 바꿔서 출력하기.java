import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String a = sc.next();
        
        StringBuilder result = new StringBuilder();
        
        for (char x : a.toCharArray()) {
                if (Character.isLowerCase(x)) {
                    result.append(Character.toUpperCase(x));
                } else {
                    result.append(Character.toLowerCase(x));
                } 
        }
        System.out.println(result.toString());
    }
}