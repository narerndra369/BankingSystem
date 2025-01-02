from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from app.models import *
import random
from django.contrib import messages


def loginview(request):
    # If the user is already authenticated, redirect to home
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == "POST":
        u = request.POST.get('usern')  # Username
        p = request.POST.get('pass')   # Password
        user = authenticate(username=u, password=p)
        print(user)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html')
    
    return render(request, 'login.html')
@login_required
def logout1(request):
    logout(request) 
    return redirect('login')
@login_required
def home(request):
    return render(request,'home.html')

def register(request):
    if request.method=="POST":
        u=request.POST.get('usern');
        p=request.POST.get('pass');
        b=500
        ac=str(random.randint(100000,999999))
        user = User(username=u)
        user.set_password(p)  
        user.save()
        userde=UserDetails.objects.create(username=u,balance=b,accountno=ac)
    return render(request,'register.html')

@login_required
def balance(request):
    acount = UserDetails.objects.get(username=request.user.username)
    return render(request, 'balance.html', {'balance': acount.balance, 'accountno': acount.accountno, 'uname': acount.username})

@login_required
def transfer(request):
    if request.method=="POST":
        receiveracno = request.POST.get('receiveracno');
        amount = request.POST.get('amount')
        amount=(int(amount))
        sender = UserDetails.objects.get(username=request.user.username)
        if sender.balance < amount:
            message = "Insufficient amount Balance"
            return render(request,'transfer.html', {"message": message})
        receiver =UserDetails.objects.get(accountno=int(receiveracno))
        sender.balance -= amount
        sender.save()
        receiver.balance += amount
        print('sender',receiver.balance)
        receiver.save()
        TransactionDetails.objects.create(accountno=sender.accountno,amount=-amount,receiveraccountno=receiver.accountno)
        TransactionDetails.objects.create(accountno=receiver.accountno,amount=amount,receiveraccountno=sender.accountno)
        message = "Transaction Succesfull"
        return render(request,'home.html',{"message": message})
    return render(request,'transfer.html')
@login_required
def transactionhistory(request):
    account = UserDetails.objects.get(username=request.user.username)
    transactions = TransactionDetails.objects.filter(accountno=account.accountno)

    # Add extra context for positive/negative amounts
    for transaction in transactions:
        transaction.type = "Credit" if transaction.amount > 0 else "Debit"
    
    return render(request, 'transhistory.html', {
        'transactions': transactions
    })
