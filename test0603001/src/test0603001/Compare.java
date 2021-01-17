package test0603001;

public class Compare {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int a = Integer.parseInt("345");
		
		Integer t1 = new Integer(345);
		
		System.out.println(t1.equals(a));
		
		System.out.println(Integer.toBinaryString(a));
		System.out.println(Integer.toHexString(a));
		System.out.println(Integer.toOctalString(a));
		System.out.println(Integer.toString(a, 15));	
		
		System.out.println(Integer.TYPE);
		
		Integer b = Integer.parseInt("234");
		System.out.println(b.shortValue());
		

	}

}
