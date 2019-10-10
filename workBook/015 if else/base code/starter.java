import pkg.*;

public class starter //implements InputKeyControl 
{
		
		static int user;
		
		 
		
        public static void main(String args[])
        {
			int r = Canvas.rand(1000);
			
			System.out.println("Guess what number I'm thinking of!");
			EasyReader joe_in;
			joe_in = new EasyReader();
			user = joe_in.readInt();
			boolean dylan = (user==r);
			if(dylan)
			{
			System.out.println("You are really smart!");

			}
			else
			{
				System.out.println("Sorry, Charlie. You are a failure. Like Daniel.");
			}			
		}
		public void keyPress(String user)
		{

		}

 }

