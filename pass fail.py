class student:
  def __init__(self,name,marks):
    self.name=name
    self.marks=marks
  def result(self,marks):
    if self.marks>=35:
      print(f"{self.name} passed with marks {self.marks}")
    else:
      print(f"{self.name} failed with marks {self.marks}")
obj=student("teju",45)
obj.result(45)
