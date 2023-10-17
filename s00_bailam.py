#region debai
"""
--- ma debai / id
get_24hformat_hour(hour_str)

--- nopbai
00 fork tu bainopmau tren replit tu trang web duoiday 
   https://replit.com/@NamG1/bainopmau2310171120get24hformathourhourstr

01 lam bai vao tep s00_bailam.py, chay Run de co ketqua tatca la 1
02a tao github repo, mo kiemtra tep s00_bailam.py, va lay diachi/url aka githubrepourl

02b dán diachi githubrepourl theo mẫu ở trang web duoiday
    https://forms.gle/dC8BstqvCVCW62FNA

--- debai / problem
Viết hàm 
  get_24hformat_hour(hour_str)
giúp trả về giờ trong ngày theo dạng 24-giờ

Khi chạy với đầuvào / input            | Kếtquả đẩura / output  | Thứtự mẫuthử 
-------------------------------------- | ---------------------- | -----------
get_24hformat_hour(hour_str='6am')     | 6                      | 00

# AM / PM format
get_24hformat_hour('6am')              | 6                      | 01
get_24hformat_hour('7 am')             | 7                      | 02
get_24hformat_hour('8AM')              | 8                      | 03
get_24hformat_hour('9 AM')             | 9                      | 04

get_24hformat_hour('6pm')              | 18                     | 05
get_24hformat_hour('7 pm')             | 19                     | 06
get_24hformat_hour('8PM')              | 20                     | 07
get_24hformat_hour('9 PM')             | 21                     | 08

get_24hformat_hour('10 AM')            | 10                     | 09
get_24hformat_hour('11 AM')            | 11                     | 10
get_24hformat_hour('10 PM')            | 22                     | 11
get_24hformat_hour('11 PM')            | 23                     | 12
"""
#endregion debai

#region bailam
def get_24hformat_hour(hour_str):
    if "am" in hour_str.lower():
      if len(hour_str)==3:
        y=hour_str[0]
        return y
      elif len(hour_str)==4 :
        y=hour_str[0:1]
        return y
      elif len(hour_str)==5 :
        y=hour_str[0:2]
        return y
    elif "pm" in hour_str.lower():
      if len(hour_str)==3:
        y=str(int(hour_str[0])+12)
        return y
      elif len(hour_str)==4 :
        y=str(int(hour_str[0:1])+12)
        return y
      elif len(hour_str)==5 :
        y=str(int(hour_str[0:2])+12)
        return y

    print(get_24hformat_hour('6am'))           
    print(get_24hformat_hour('7 am'))
    print(get_24hformat_hour('8AM'))     
    print(get_24hformat_hour('9 AM'))     

    print(get_24hformat_hour('6pm'))   
    print(get_24hformat_hour('7 pm'))
    print(get_24hformat_hour('8PM'))  
    print(get_24hformat_hour('9 PM'))

    print(get_24hformat_hour('10 AM')) 
    print(get_24hformat_hour('11 AM')) 
    print(get_24hformat_hour('10 PM'))   
    print(get_24hformat_hour('11 PM'))
#endregion bailam
