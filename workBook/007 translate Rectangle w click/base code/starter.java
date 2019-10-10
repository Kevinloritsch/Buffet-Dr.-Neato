import pkg.*;

public class starter implements InputControl {
			static Rectangle r; 
	

	public static void main(String args[])
        {
			// following line is necessary for onMouseClick, don't change
			MouseController mC = new MouseController(Canvas.getInstance(),new starter());
			// put your code here:
			  r = new Rectangle(10, 30, 100, 200);
			r.fill();
			
		}


		public void onMouseClick(double x, double y){
			// and/or here
			r.translate(10,5);
	
		}
}
