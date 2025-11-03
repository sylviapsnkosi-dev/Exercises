public class passwordValidator {
    public static void main(String args){
    
    //call the method
    isValidPassword("mypassword");

        
    }

    static boolean isValidPassword(String password){
        // counters
        int upper = 0;
        int lower = 0;
        int num = 0;
        int spec = 0;


        //1 the length of the password must be greater than 8
        int size = password.length();


        // go through every character and add to counters
        for (int x = 0; x < size; x++){
            char i = password.charAt(x);

            if(Character.isUpperCase(i)){
                upper += 1;

            }else if (Character.isLowerCase(i)){
                lower += 1;

            }else if(Character.isDigit(i)){
                num += 1;

            }else if ((!Character.isLetter(i))&&(Character.isDigit(i))){
                spec += 1; 
            }
        }

        // now i use an if statement to determine whether is the password contains atleast on of (lower letter, uppercase letter, number, special character and length > 8)
        return upper > 0 && lower > 0 && num > 0 && spec > 0 && size > 8;

    }

    
}
