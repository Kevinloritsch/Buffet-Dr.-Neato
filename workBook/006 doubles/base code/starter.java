// Kevin Loritsch 9/5/19
// (°F − 32) * 5/9 = °C

import java.util.*;

class starter {
		
        public static void main(String args[])
        {
			System.out.println();
			System.out.println();
			System.out.println();
			double a;
			double b;
			double c;
			double d;
			a = 32;
			b = 5./9;
			c = 32;  //insert Fahrenheit 
			d = (c - a) * b; //d is Celsius
			
			System.out.print("The Fahrenheit value is " + c);
			System.out.print(" and the Celsius value is " + d );

			System.out.println();
			System.out.println();
			System.out.println();
			
        }
        
}
