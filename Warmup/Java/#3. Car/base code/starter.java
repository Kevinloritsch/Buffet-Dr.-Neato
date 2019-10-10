import pkg.*;
public class starter implements InputControl, InputKeyControl


{
		
static Rectangle car;
static Ellipse one;
static Ellipse two;
static Ellipse three;
static Picture bat;
static Ellipse window;
static Rectangle bob;
static Rectangle light;
static Picture driver;
static Rectangle jim;
static Rectangle fred;


        public static void main(String args[])
        {
		
			// following line is necessary for onMouseClick, don't change
			MouseController mC = new MouseController(Canvas.getInstance(),new starter());
			car = new Rectangle(100, 100, 260, 100);
			car.fill();
			one = new Ellipse(100, 50, 260, 140);
			one.fill();
			two = new Ellipse(120, 180, 50, 50);
			two. setColor(Color.YELLOW);
			two.fill();
			three = new Ellipse(300, 180, 50, 50);
			three. setColor(Color.YELLOW);
			three.fill();
			bob = new Rectangle(200,100,80,100);
			bob.fill();
			window = new Ellipse(155,60,150,73);
			window.setColor(Color.GRAY);
			window.fill();
			light = new Rectangle(360,180,15,15);
			light.setColor(Color.ORANGE);
			light.fill();
			jim = new Rectangle(208,20,60,20);
			jim.fill();
			fred = new Rectangle(208,40,20,60);
			fred.fill();
			
			
			
			driver = new Picture("alfred.jpg");
			driver.draw();
			driver.translate(208,62);
			bat = new Picture("batsymbol.jpg");
			
			bat.draw();
			bat.translate(157,100);
					
			
			

			// please leave following line alone, necessary for keyboard input
			KeyController kC = new KeyController(Canvas.getInstance(),new starter());
			
			
		}
		
		public void onMouseClick(double x, double y){
			// and/or here
	
		}
		
		public void keyPress(String s)
		{
			// temp holds the enter character
			
			char done = (char)10;
			String temp = Character.toString(done);
			
		}
}
