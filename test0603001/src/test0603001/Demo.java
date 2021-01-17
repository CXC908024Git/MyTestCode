package test0603001;

public class Demo {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		try {
			action();
		}
		catch (ClassNotFoundException e) {
			// TODO: handle exception
			System.out.println(e.getMessage());
		}
		catch (NullPointerException e) {
			// TODO: handle exception
			e.printStackTrace();
		}
		catch (Exception e) {
			// TODO: handle exception
			e.printStackTrace();
		}

	}
	
	static public void action() throws ClassNotFoundException{
		int a = 1;
		if(a>0)
		{
			throw new ClassNotFoundException("找不到对应的类");
			
		}
	}

}

/*class ClassNotFoundException extends Exception
{
	/**
	 * 
	 */
	//private static final long serialVersionUID = 3693831164544757301L;

	//ClassNotFoundException(String message)
	//{
		//super(message);
	//}
//}