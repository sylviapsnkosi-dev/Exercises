import java.util.HashMap;

public class cashRegister{
    public static void main (String[] args){
        System.out.println("hello");

    }

    public static HashMap myChange(double total, double due){

        // Create array list of possible notes
        double[] denominations = {200_00, 100_00, 50_00, 20_00, 10_00, 5_00, 2_00, 1_00, 50, 20, 10,5};

        // now initialize the variables
        double amountDue = total;
        double payment = due;
        double change = 0 ;


        // create the hashmap to store the note as key and how many times it should be given as a value
        // question to note, why should i ues Double whereas i normally use double for variable and Integer instead of int
        // new HashMap<>() , vs code corrected me i had new Hashmap<Double, Integer>(); why 

        HashMap<Double, Integer> notes = new HashMap<>(); 



        // now check if the customer is eligible for change then calculate it
        if (payment > amountDue){
            change = payment - amountDue;
        
            // now we want to check which minimum notes should be given to the customer as change, start checking from the highest note(biggest amount)
            for(int x = 0; x < denominations.length; ++x){
                double currentNote = denominations[x];
                // now check if this note should be given back
                double n  = change / currentNote; 
                int times =  double(n) ;      // remember change and currentNote are doubles

                if(times > 0){
                    // append this note and times into the map 
                    // subtract from change currentNote * times
                }
            }
            // once done return the map
            return notes;
        } else{
            return notes;
        } 
    }
}
