关联查询sql:
更新a表dns_records, b表zoneinfo
a，b表共同的字段data, host, zone


批量修改A03的comment字段:
update dns_records a, zoneinfo b set b.comment  = 'A03_VIP', a.user = 'nimei',b.user = 'nimei' where a.data = 'www.google.com.' and a.host = 'www' and a.zone = b.zone;

SELECT * from dns_records a, zoneinfo b where a.data = 'www.google.com.' and a.host = 'm' and a.zone = b.zone;

SELECT * from dns_records a,zoneinfo b where a.host = 'm' and b.product = 'E03' and a.zone = b.zone;


批量将E03的主机头为m的域名, type改成CNAME, data改成m.google.com.:
SELECT * from cdn_view.zoneinfo where product = 'E03';

SELECT * from dns_records a, zoneinfo b where a.host = 'm' and b.product = 'E03' and a.zone = b.zone;

UPDATE dns_records a, zoneinfo b set a.type = 'CNAME', a.data = 'm.google.com.' where a.host = 'm' and b.product = 'E03' and a.zone = b.zone;

UPDATE貌似不支持limit更新
UPDATE dns_records a, zoneinfo b set a.type = 'CNAME', a.data = 'm.google.com.' where a.host = 'm' and b.product = 'E03' and a.zone = b.zone limit 90;
[Err] 1221 - Incorrect usage of UPDATE and LIMIT


批量将E03所有域名添加一个主机头为game的记录, 即, game.123.com cname game.google.com(此域名固定):
select zone from cdn_view.zoneInfo where product='E03';

SELECT * from dns_records a,zoneinfo b where a.host = 'game' and b.product = 'E03' and a.zone = b.zone;

insert into cdn_view.dns_records (zone,host,type,data) (select a.zone,'game','CNAME','game.google.com.' from (select zone from cdn_view.zoneInfo where product='E03') a);
