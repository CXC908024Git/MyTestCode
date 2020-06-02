package test0603;

class Car
{
	static String part1 = "油门踏板";
	static String part2 = "刹车踏板";
	static void  oper(Car c)
	{
		System.out.println("右脚踩" + part1 + "!");
		System.out.println("右脚踩" + part2 + "!");
	}
			
}

public class AutoCar extends Car {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		AutoCar ac = new AutoCar();
		System.out.println("自动挡汽车有2块踏板。");
		oper(ac);
	}
	
}
