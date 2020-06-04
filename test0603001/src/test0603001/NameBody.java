package test0603001;

public class NameBody {

	public static void main (String[] args)
	{
		// TODO Auto-generated method stub
		NameBody nb1 = new NameBody();
		String name[] = {"张三","李四","王五"};
		try {
			for(int i = 0;i<name.length;i++)
			{
				nb1.dM(name[i]);
			}
		} catch (AbrodException e) {
			System.out.println(e.getMessage());
		}
		catch (Exception e) {
			e.printStackTrace();
		}
		

	}
	
	void dM(String name) throws Exception
	{
		if(name == "王五")
		{
			throw new AbrodException("王五迟到");
		}
		else 
		{
			System.out.println(name);
		}
	}

}

class AbrodException extends Exception
{
	AbrodException(String message)
	{
		super(message);
	}
}