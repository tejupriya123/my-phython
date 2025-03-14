class feature1:
  def feature1(self):
    print("feature1")

class feature2:
  def feature2(self):
      print("feature2")


class c(feature1,feature2):
        pass
obj=c()
obj.feature1()
obj.feature2()
