from Date import Date
class Person:
    def __init__(self, name, id, ngay, thang, nam):
        d = Date(ngay, thang, nam)
        d.check()
        self.name = name
        self.id = id
        self.date_of_birth = d.text()
    def __str__(self):
        return f"{self.name}\nchung minh thu: {self.id}\nngay thang nam sinh: {self.date_of_birth}"
