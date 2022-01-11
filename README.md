# fortigate
Fortigate python scripts

###### convert_dhcp_to_forti.py ##########

Sample DHCP file content from Windows DHCP Server

Client IP Address	Name	Lease Expiration	Type	Unique ID	Description	Network Access Protection	Probation Expiration	Filter Profile	Policy
172.16.1.12	test01.test.com	Reservation (active)	DHCP	001122334455	Test Win 10 	Full Access	N/A	None	

Sample file for Fortigate DHCP Server
config reserved-address
edit 1
set ip 172.16.1.12
set mac 00:11:22:33:44:55
set description test01.test.com
next
end

##########################################
