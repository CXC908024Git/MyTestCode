create or replace procedure loopdelrecnt(cnt in integer) is
begin
declare
  cursor del_cur is select 
	a.*,a.rowid row_id from tbl_online_log_bak a where (a.acqinst,a.fwdinst,a.tran_time,a.tran_seq) in
	(select a.acqinst,a.fwdinst,a.tran_time,a.tran_seq from tbl_online_log_bak a 
	group by a.acqinst,a.fwdinst,a.tran_time,a.tran_seq having count(*)>=cnt)
	and a.rowid not in(select min(rowid) from tbl_online_log_bak group by acqinst,fwdinst,tran_time,tran_seq 
	having count(*)>=cnt);
  begin
    for v_cusor in del_cur
    loop
      delete tbl_online_log_bak where rowid = v_cusor.row_id;
      if mod(del_cur%rowcount,100000)=0 then
      commit;
      end if;
    end loop;
    commit;
  end;
end loopdelrecnt;
/
