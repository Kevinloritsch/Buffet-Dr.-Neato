import pkg.*;
public class starter implements InputControl, InputKeyControl 
{
	private static Car kMob;
	private static Car kMob2;
	private static Car kMob3;
	private static Car kMob4;
	private static Car kMob5;
	private static Car kMob6;
	private static Car kMob7;
	private static Car kMob8;
	private static Car kMob9;
	private static Car kMob1a;
	private static Car kMob2a;
	private static Car kMob3a;
	static Text crash;
	static Text congrats;
	

	static Emoji e;
	
        public static void main(String args[])
        {
			// following line is necessary for onMouseClick, don't change
			MouseController mC = new MouseController(Canvas.getInstance(),new starter());
			
			// please leave following line alone, necessary for keyboard input
			KeyController kC = new KeyController(Canvas.getInstance(),new starter());
			Rectangle green = new Rectangle (0,0,100000,100000);
			green.fill();
			green.setColor(Color.GREEN);
			Rectangle green2 = new Rectangle (0,0,75,100000);
			green2.fill();
			green2.setColor(Color.GREEN);
			Rectangle bone = new Rectangle (0,75,100000,100);
			bone.fill();
			Rectangle btwo = new Rectangle (0,225,100000,100);
			btwo.fill();
			Rectangle bthree = new Rectangle (0,375,100000,100);
			bthree.fill();
			Rectangle bfour = new Rectangle (0,525,100000,100);
			bfour.fill();
			
			kMob = new KrabbyMobile(1500,270,.3);
			kMob.fill();
			
			kMob2 = new KrabbyMobile(1400,770,.3);
			kMob2.fill();
			
			kMob3 = new KrabbyMobile(900,1270,.3);
			kMob3.fill();
			kMob4 = new KrabbyMobile(700,1770,.3);
			kMob4.fill();
			kMob5 = new KrabbyMobile(1800,270,.3);
			kMob5.fill();
			kMob6 = new KrabbyMobile(700,770,.3);
			kMob6.fill();
			kMob7 = new KrabbyMobile(100,1270,.3);
			kMob7.fill();
			kMob8 = new KrabbyMobile(800,1770,.3);
			kMob8.fill();
			kMob9 = new KrabbyMobile(500,270,.3);
			kMob9.fill();
			kMob1a = new KrabbyMobile(250,770,.3);
			kMob1a.fill();
			kMob2a = new KrabbyMobile(300,1270,.3);
			kMob2a.fill();
			kMob3a = new KrabbyMobile(30,1770,.3);
			kMob3a.fill();
			
			e = new Emoji(200,650,45,45);
			e.fill();
			congrats = new Text(700,250,"Congrats!");
			congrats.grow(450,500);
			congrats.setColor(Color.RED);
			crash = new Text(700,300,"Crash!");
			crash.grow(450,500);
			crash.setColor(Color.RED);
			
			
			
			while (true)
			{
				kMob.translate(Canvas.rand(150),0);
				Canvas.pause(5);
				
				if(kMob.getX()>=1400)
				{
					kMob.translate(-1400,0);
				}
				kMob2.translate(Canvas.rand(150),0);
				Canvas.pause(5);
				
				if(kMob2.getX()>=1400)
				{
					kMob2.translate(-1400,0);
				}
				kMob3.translate(Canvas.rand(15),0);
				Canvas.pause(5);
				
				if(kMob3.getX()>=1400)
				{
					kMob3.translate(-1400,0);
				}
				kMob4.translate(Canvas.rand(150),0);
				Canvas.pause(5);
				
				if(kMob4.getX()>=1400)
				{
					kMob4.translate(-1400,0);
				}
				kMob5.translate(Canvas.rand(45),0);
				Canvas.pause(5);
				
				if(kMob5.getX()>=1400)
				{
					kMob5.translate(-1400,0);
				}
				kMob6.translate(Canvas.rand(15),0);
				Canvas.pause(5);
				
				if(kMob6.getX()>=1400)
				{
					kMob6.translate(-1400,0);
				}
				kMob7.translate(Canvas.rand(45),0);
				Canvas.pause(5);
				
				if(kMob7.getX()>=1400)
				{
					kMob7.translate(-1400,0);
				}
				kMob8.translate(Canvas.rand(120),0);
				Canvas.pause(5);
				
				if(kMob8.getX()>=1400)
				{
					kMob8.translate(-1400,0);
				}
				kMob9.translate(Canvas.rand(15),0);
				Canvas.pause(5);
				
				if(kMob9.getX()>=1400)
				{
					kMob9.translate(-1400,0);
				}
				kMob1a.translate(Canvas.rand(15),0);
				Canvas.pause(5);
				
				if(kMob1a.getX()>=1400)
				{
					kMob1a.translate(-1400,0);
				}
				kMob2a.translate(Canvas.rand(50),0);
				Canvas.pause(5);
				
				if(kMob2a.getX()>=1400)
				{
					kMob2a.translate(-1400,0);
				}
				kMob3a.translate(Canvas.rand(150),0);
				Canvas.pause(5);
				
				if(kMob3a.getX()>=1400)
				{
					kMob3a.translate(-1400,0);
				}
				
				if(e.crash(kMob))
			{
				crash.draw();
				break;
			}
			if(e.crash(kMob2))
			{
				crash.draw();
				break;
			}
			if(e.crash(kMob3))
			{
				crash.draw();
				break;
			}
			if(e.crash(kMob4))
			{
				crash.draw();
				break;
			}
			if(e.crash(kMob5))
			{
				crash.draw();
				break;
			}
			if(e.crash(kMob6))
			{
				crash.draw();
				break;
			}
			if(e.crash(kMob7))
			{
				crash.draw();
				break;
			}
			if(e.crash(kMob8))
			{
				crash.draw();
				break;
			}
			if(e.crash(kMob9))
			{
				crash.draw();
				break;
			}
			if(e.crash(kMob1a))
			{
				crash.draw();
				break;
			}
			if(e.crash(kMob2a))
			{
				crash.draw();
				break;
			}
			if(e.crash(kMob3a))
			{
				crash.draw();
				break;
			}
			if(e.getY()<25)
			{
				congrats.draw();
				break;
			}		
			
		
		}
		}
		public void onMouseClick(double x, double y)
		{
			
		}
		
		public void keyPress(String s)
		{
			
			if(s.equals("d"))
			{
			e.translate(10,0);
			}
			if(s.equals("a"))
			{
			e.translate(-10,0);
			}
			if(s.equals("w"))
			{
			e.translate(0,-10);
			}
			if(s.equals("s"))
			{
			e.translate(0,10);
			}
			//Hidden GOD MODE
			if(s.equals("l"))
			{
			e.translate(50,0);
			}
			if(s.equals("j"))
			{
			e.translate(-50,0);
			}
			if(s.equals("i"))
			{
			e.translate(0,-50);
			}
			if(s.equals("k"))
			{
			e.translate(0,50);
			}
			
			
	

				
		}
}
