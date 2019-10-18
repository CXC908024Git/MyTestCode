create or replace procedure showcnt(tabname varchar2) is
begin
  declare
	sum_cnt number;
	sql_str varchar2(200);
	begin
	sql_str:='select count(1) from '||tabname;
	execute immediate sql_str into sum_cnt;
	dbms_output.put_line(sum_cnt);
	end;
end showcnt;
/
