package sample;
import java.util.Scanner;
import java.util.Random;




public class RockPaperScissor {

    public static void UserWon(){

        System.out.println("You Won !!!!!!!! Computer Lost !!!!!!!!!!!");
    }

    public static void UserLost(){

        System.out.println("Computer Won!!!!!! You Lost!!!!!!#####");
    }
    
    public static void Tie(){
        
     System.out.println("Its a tie.");   
    }    
        
        


    public static void main(String[] args) {
        System.out.println("Welcome you brand new Java Rock Paper Scissor game");
        System.out.println(" Please enter Rock Paper or Scissor. ");




        Random rand = new Random();
        int ComChoice = rand.nextInt(3);
//        System.out.println(ComChoice);

        Scanner Scan = new Scanner(System.in);
        String str = Scan.nextLine();

        // rock is 0
        // paper is 1
        // scissor is 2




        if ((ComChoice==0) && (str.equals("Paper"))){
            UserWon();
        }

        else if((ComChoice==1)  && (str.equals("Scissor"))){

            UserWon();
        }

        else if((ComChoice==2)  && (str.equals("Rock"))){

            UserWon();
        }

        else if((ComChoice==0)  && (str.equals("Scissor"))){

            UserLost();
        }

        else if((ComChoice==1)  && (str.equals("Rock"))){

            UserLost();
        }

        else if((ComChoice==2)  && (str.equals("Paper"))){

            UserLost();
        }
        
         else if((ComChoice==0)  && (str.equals("Rock"))){

            Tie();
        }
        
         else if((ComChoice==1)  && (str.equals("Paper"))){

            Tie();
        }
        
         else if((ComChoice==2)  && (str.equals("Scissor"))){

            Tie();
        }
        
        
    

        else{

            System.out.println("Enter a valid decision Rock, Paper or Scissor");
        }












    }

}

