class Date:
    def __init__(self, ngay, thang, nam):
        
        self.ngay = ngay
        self.thang = thang
        self.nam = nam
    def check(self):
        assert isinstance(self.ngay, int) and isinstance(self.thang, int) and isinstance(self.nam, int), "Dinh dang ngay thang nam phai la so"
        if self.nam % 4==0 and self.nam%100!=0 or self.nam%400==0:
            namnhuan = True
        else:
            namnhuan = False
        if self.thang in [4,6,9,11]:
            if self.ngay > 30:
                raise ValueError('sai dinh dNG ngay')
        if self.thang in [1,3,5,7,8,10,12]:
            if self.ngay > 31:
                raise ValueError('sai dinh dNG ngay')
        if namnhuan:
            if self.thang==2 and self.ngay>29:
                raise ValueError('loi')
        else:
            if self.thang==2 and self.ngay>28:
                raise ValueError('sai dinh dang ngay')
    def text(self):
        return f"{self.ngay}-{self.thang}-{self.nam}"

