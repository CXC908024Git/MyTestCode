package test0603001;


public class Book<T,P> {
	T bookInfo;
	P cnt;
	Book(T bookInfo, P bookcnt){
		this.bookInfo = bookInfo;
		this.cnt = bookcnt;
	}
	T getBookInfo() {
		return bookInfo;
	}
	P getBookNum() {
		return cnt;
	}
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Book<String,Integer> bookname = new Book<String,Integer>("论语",3);
		Book<Double,Integer> bookPrice = new Book<Double,Integer>(45.5,1);
		
		System.out.println("书名:"+bookname.getBookInfo()+ "共有"+bookname.getBookNum()+"本");
		System.out.println("价格:"+bookPrice.getBookInfo()+"共卖出"+bookPrice.getBookNum()+"本");
		
	}
}
