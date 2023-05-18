from django.shortcuts import render, redirect

# Create your views here.
from students.models import student
from students.form import PostForm

def listone(request):
	try:
		unit = student.objects.get(stdName="Amy")
	except:
		errormessage = "(讀取錯誤！)"
	return render(request, "students/listone.html", locals())

def listall(request):
	allStudents = student.objects.all().order_by('id')
	return render(request, "students/listall.html", locals())

def post(request):
	#判斷表單資料傳送方式
	if request.method == "POST":
		#接收傳送資料
		messName = request.POST['stdName']
		messID = request.POST['stdID']
		
		messSex = request.POST['stdSex']
		messBirth = request.POST['stdBirth']
		messEmail = request.POST['stdEmail']
		messPhone = request.POST['stdPhone']
		messAddress = request.POST['stdAddress']
		#新增一筆紀錄
		unit = student.objects.create(stdName=messName, stdID=messID, stdSex=messSex, stdBirth=messBirth, stdEmail=messEmail, stdPhone=messPhone, stdAddress=messAddress) 
		unit.save()
		return redirect('/listall')
	else:
		mess = '請輸入資料（資料不作驗證）'
		
	return render(request, "students/addstd.html", locals())

def postform(request):
	#新增PostForm表單物件
	stdform = PostForm()
	return render(request, "students/stdform.html", locals())

def delete(request, stdName=None):
	if stdName != None:
		if request.method == "POST":
			stdName = request.POST["stdName"]
		#嘗試抓取此ID之學生資料
		#嘗試try區塊的程式碼, 如果發生錯誤或例外情形執行except區塊的程式碼
		try:
			unit = student.objects.get(stdName=stdName)
			#刪除該資料
			unit.delete()
			return redirect('/listall')
		except:
			mess = "查無該學號"
	return render(request,"students/delete.html",locals())

def edit(request, stdID=None, mode=None):
	if mode == "edit":
		unit = student.objects.get(stdID=stdID)
		unit.stdName = request.GET["stdName"]
		unit.stdID = request.GET["stdID"]
		unit.stdSex = request.GET["stdSex"]
		unit.stdBirth = request.GET["stdBirth"]
		unit.stdEmail = request.GET["stdEmail"]
		unit.stdPhone = request.GET["stdPhone"]
		unit.stdAddress = request.GET["stdAddress"]
		unit.save()
		mess = "已修改完成"
		return redirect('/listall')
	else:
		try:
			unit = student.objects.get(stdID=stdID)
			strDate = str(unit.stdBirth)
			strDate2 = strDate.replace(" 年 ", "-")
			strDate2 = strDate.replace(" 月 ", "-")
			strDate2 = strDate.replace(" 日 ", "-")
		except:
			mess = "此學號不存在"
		return render(request, "students/edit.html", locals())
