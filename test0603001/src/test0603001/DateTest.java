package test0603001;
import java.util.*;
import java.text.*;

/*interface Contest{
	final int Constants_A =1;
	final int Constants_B =1;
}*/
public class DateTest {
	final int Constants_A =1;
	final int Constants_B =10;
	public enum Constants
	{
		Constants_A,
		Constants_B
    }

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		Date date = new Date();
		long value = date.getTime();
		System.out.println(date);
		System.out.println(value);
		
		DateFormat df = DateFormat.getDateInstance();
		SimpleDateFormat df2 = new SimpleDateFormat();
		SimpleDateFormat df3 = new SimpleDateFormat("YYYYMMdd hh:mm:ss.SSS",Locale.US);
		System.out.println(df2.format(date));
		System.out.println(df3.format(date));
		String cc = df.format(date);
		System.out.println(cc);
		try {
			Date dd = df.parse("2020年6月17日");
			System.out.println(dd.getTime());
		} catch (Exception e) {
			// TODO: handle exception
            System.out.println(e.getMessage());
		}
		finally {
			System.out.println("nothing");
		}
		Constants s = Constants.Constants_A;
		switch(s)
		{
		    case Constants_A:
		    {
		    	System.out.println(Constants.Constants_A);
		    	break;
		    }
		    case Constants_B:
		    {
		    	System.out.println(Constants.Constants_B);
		    	break;
		    }
		    default:
		    	break;
		}
        
		

	}

}
