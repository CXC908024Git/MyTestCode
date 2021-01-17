package test0603001;
import java.util.*;

public class RedBag {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		int cnt;
		double amts;
		
		System.out.print("请输入红包金额:");
		amts = sc.nextInt();
		System.out.print("请输入红包个数:");
		cnt = sc.nextInt();
		
		int[] rb = new int[cnt];
		
		Random rd = new Random();
		while(true)
		{
			for(int i=0;i<cnt;i++)
			{
				rb[i] = rd.nextInt(4);
				System.out.println(rb[i]);
			}
			if(RedBag.sum(rb)==amts)
			{
				for(int j = 0;j<rb.length;j++)
				{
					System.out.println(j+"红包金额为:"+rb[j]);
				}
				break;
			}
		}
		
	}
	static int sum(int[] d)
	{
		int sum = 0;
		for(int i = 0;i<d.length;i++)
		{
			sum+=d[i];
		}
		return sum;
	}

}
