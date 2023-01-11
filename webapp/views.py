from django.shortcuts import render
# from django.http import HttpResponseRedirect

# Create your views here.

def home(request):
	return render(request, 'home.html', {})

def add(request):
	from random import randint

	num_1 = randint(0,10)
	num_2 = randint(0,10)

	if request.method == "POST":
		answer = request.POST['answer']
		old_num_1 = request.POST['old_num_1']
		old_num_2 = request.POST['old_num_2']

		# Error handling if form not filled out
		if not answer:
			my_answer = "Hey, you forgot to provide your answer!"
			color = 'danger'

			return render(request, 'add.html', {
			'color':color,
			'my_answer':my_answer,
			'answer': answer,
			'num_1': num_1,
			'num_2':num_2,
			})

		correct_answer = int(old_num_1) + int(old_num_2)
		if int(answer) == correct_answer:
			# color = "success"
			my_answer = "Correct! " + old_num_1 + " + " + old_num_2 + " = " + answer
			color = "success"
		else:
			# color = "danger"
			my_answer = "Incorrect! " + old_num_1 + " + " + old_num_2 + " is " + str(correct_answer) + " not " + answer
			color = "danger"

		print('IF', request.method)
		return render(request, 'add.html', {
			'answer': answer,
			'my_answer': my_answer,
			'num_1':num_1,
			'num_2':num_2,
			'color':color,
			})
	else:
		print("ELSE ", request.method)
		return render(request, 'add.html', {
			'num_1':num_1,
			'num_2':num_2,
			})

def subtract(request):
	from random import randint

	num_1 = randint(0,10)
	num_2 = randint(0,10)

	if request.method == "POST":
		answer = request.POST['answer']
		old_num_1 = request.POST['old_num_1']
		old_num_2 = request.POST['old_num_2']

		# Error handling if form not filled out
		if not answer:
			my_answer = "Hey, you forgot to provide your answer!"
			color = 'danger'

			return render(request, 'subtract.html', {
			'color':color,
			'my_answer':my_answer,
			'answer': answer,
			'num_1': num_1,
			'num_2':num_2,
			})

		correct_answer = int(old_num_1) - int(old_num_2)
		if int(answer) == correct_answer:
			# color = "success"
			my_answer = "Correct! " + old_num_1 + " - " + old_num_2 + " = " + answer
			color = "success"
		else:
			# color = "danger"
			my_answer = "Incorrect! " + old_num_1 + " - " + old_num_2 + " is " + str(correct_answer) + " not " + answer
			color = "danger"

		print('IF', request.method)
		return render(request, 'subtract.html', {
			'answer': answer,
			'my_answer': my_answer,
			'num_1':num_1,
			'num_2':num_2,
			'color':color,
			})
	else:
		print("ELSE ", request.method)
		return render(request, 'subtract.html', {
			'num_1':num_1,
			'num_2':num_2,
			})

def multiply(request):
	from random import randint

	num_1 = randint(0,10)
	num_2 = randint(0,10)

	if request.method == "POST":
		answer = request.POST['answer']
		old_num_1 = request.POST['old_num_1']
		old_num_2 = request.POST['old_num_2']

		# Error handling if form not filled out
		if not answer:
			my_answer = "Hey, you forgot to provide your answer!"
			color = 'danger'

			return render(request, 'multiply.html', {
			'color':color,
			'my_answer':my_answer,
			'answer': answer,
			'num_1': num_1,
			'num_2':num_2,
			})

		correct_answer = int(old_num_1) * int(old_num_2)
		if int(answer) == correct_answer:
			# color = "success"
			my_answer = "Correct! " + old_num_1 + " x " + old_num_2 + " = " + answer
			color = "success"
		else:
			# color = "danger"
			my_answer = "Incorrect! " + old_num_1 + " x " + old_num_2 + " is " + str(correct_answer) + " not " + answer
			color = "danger"

		print('IF', request.method)
		return render(request, 'multiply.html', {
			'answer': answer,
			'my_answer': my_answer,
			'num_1':num_1,
			'num_2':num_2,
			'color':color,
			})
	else:
		print("ELSE ", request.method)
		return render(request, 'multiply.html', {
			'num_1':num_1,
			'num_2':num_2,
			})

def divide(request):
	from random import randint

	num_1 = randint(0,10)
	num_2 = randint(1,10)

	if request.method == "POST":
		answer = request.POST['answer']
		old_num_1 = request.POST['old_num_1']
		old_num_2 = request.POST['old_num_2']

		# Error handling if form not filled out
		if not answer:
			my_answer = "Hey, you forgot to provide your answer!"
			color = 'danger'

			return render(request, 'divide.html', {
			'color':color,
			'my_answer':my_answer,
			'answer': answer,
			'num_1': num_1,
			'num_2':num_2,
			})

		correct_answer = int(old_num_1) / int(old_num_2)
		if float(answer) == correct_answer:
			my_answer = "Correct! " + old_num_1 + " / " + old_num_2 + " = " + answer
			color = "success"
		else:
			my_answer = "Incorrect! " + old_num_1 + " / " + old_num_2 + " is " + str(correct_answer) + " not " + answer
			color = "danger"

		print('IF', request.method)
		return render(request, 'divide.html', {
			'answer': answer,
			'my_answer': my_answer,
			'num_1':num_1,
			'num_2':num_2,
			'color':color,
			})
	else:
		print("ELSE ", request.method)
		return render(request, 'divide.html', {
			'num_1':num_1,
			'num_2':num_2,
			})