import java.util.List;

public class UsernameValidation{
    public static void main(String[] args){

        //try method 
        String result = usernameValidation("SyvliaNkosi10");
        System.out.println(result);
    }


    public static String usernameValidation(String username){

        //1. The username is between 4 and 25 characters.
        int size = username.length();

       //2. It must start with a letter.
        char start = username.charAt(0);

      //3. It can only contain letters, numbers, and the underscore character. no special characters only _
        int special = 0;

     //4. It cannot end with an underscore character.
        char end = username.charAt(size-1);

        //look for illigal characters
        for (int x = 1; x < size; ++x){
            char currentChar = username.charAt(x);
                if((!Character.isLetter(currentChar)) && (!Character.isDigit(currentChar)) && (!List.of('_').contains(currentChar))){
                    special += 1;  
                }
        }


        if ((!Character.isLetter(start)) ||(special > 0) || (end == '_') || (size < 4 ) || (size > 26)){
            return " invalid username";

        }else{
            return "username is valid";
        }

    } 
}

/*
NOTES
1. In JAVA Strings and characters are not the same, 
   - " " double quotations for strings
   - ' ' single quotations for char

2. Always use charAt() method to get a character from a string  - string[index] - does not work in Java

3. charAt(length - 1) → gets the last character in java string[-1] does not work the last element is length - 1
 */
 