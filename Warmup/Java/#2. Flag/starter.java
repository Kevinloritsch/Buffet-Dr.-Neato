// Kevin Loritsch 9/4/19
import pkg.*;

public class starter //implements InputControl 
{

	

	public static void main(String args[])
        {
			// following line is necessary for onMouseClick, don't change
			// put your code here:
			Rectangle r=new Rectangle (50, 20, 100, 200);
			r. setColor(Color.RED);
			r.fill();
			Rectangle e=new Rectangle (50, 20, 300, 200);
			e.draw();
			
			
			Rectangle c=new Rectangle (250, 20, 100, 200);
			c. setColor(Color.GREEN);
			c.fill();
			Rectangle p=new Rectangle (35, 20, 15, 1000);
			p.fill();
		}


		public void onMouseClick(double x, double y){
			// and/or here
			
	
		}
}
