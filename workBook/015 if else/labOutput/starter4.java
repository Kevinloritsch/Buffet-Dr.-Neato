
public class starter// implements InputKeyControl 

{
		
		static int user;
		static int random  = 5;//(Canvas.rand(5));
		
        public static void main(String args[])
        {
			
			
			System.out.println("Guess what number I'm thinking of!");
			EasyReader joe_in;
			joe_in = new EasyReader();
			user = joe_in.readLine();
			boolean dylan = (user==random);
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

