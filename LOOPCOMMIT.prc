create or replace procedure LOOPCOMMIT(cnt number) is
begin
  declare
	cursor cur is
	select * from tbl_online_log;
	type rec is table of tbl_online_log%rowtype;
	recs rec;
	begin
	  open cur;
	  while(true)
	  loop
	  fetch cur bulk collect
	    into recs limit cnt;
	  forall i in 1 .. recs.count
	    insert into tbl_online_log_bak values recs(i);
		  commit;
		  exit when cur%notfound;
	  end loop;
	  close cur;
	end;
end LOOPCOMMIT;
/
