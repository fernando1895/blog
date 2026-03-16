from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.utils import timezone

from .models import Category, Transaction
from .forms import CategoryForm, TransactionForm


def dashboard(request):
    transactions = Transaction.objects.all()

    total_income = transactions.filter(
        transaction_type=Transaction.INCOME
    ).aggregate(total=Sum('amount'))['total'] or 0

    total_expense = transactions.filter(
        transaction_type=Transaction.EXPENSE
    ).aggregate(total=Sum('amount'))['total'] or 0

    balance = total_income - total_expense

    categories = Category.objects.all()
    category_data = []
    for category in categories:
        cat_transactions = transactions.filter(category=category)
        cat_income = cat_transactions.filter(
            transaction_type=Transaction.INCOME
        ).aggregate(total=Sum('amount'))['total'] or 0
        cat_expense = cat_transactions.filter(
            transaction_type=Transaction.EXPENSE
        ).aggregate(total=Sum('amount'))['total'] or 0
        category_data.append({
            'category': category,
            'income': cat_income,
            'expense': cat_expense,
            'net': cat_income - cat_expense,
        })

    recent_transactions = transactions.order_by('-date', '-id')[:10]

    return render(request, 'budget/dashboard.html', {
        'total_income': total_income,
        'total_expense': total_expense,
        'balance': balance,
        'category_data': category_data,
        'recent_transactions': recent_transactions,
    })


def transaction_list(request):
    transactions = Transaction.objects.select_related('category').all()

    category_id = request.GET.get('category')
    transaction_type = request.GET.get('type')

    if category_id:
        transactions = transactions.filter(category_id=category_id)
    if transaction_type:
        transactions = transactions.filter(transaction_type=transaction_type)

    categories = Category.objects.all()
    return render(request, 'budget/transaction_list.html', {
        'transactions': transactions,
        'categories': categories,
        'selected_category': category_id,
        'selected_type': transaction_type,
    })


@login_required
def transaction_new(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save()
            return redirect('transaction_list')
    else:
        form = TransactionForm(initial={'date': timezone.now().date()})
    return render(request, 'budget/transaction_form.html', {
        'form': form,
        'title': 'Nueva Transacción',
    })


@login_required
def transaction_edit(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk)
    if request.method == 'POST':
        form = TransactionForm(request.POST, instance=transaction)
        if form.is_valid():
            form.save()
            return redirect('transaction_list')
    else:
        form = TransactionForm(instance=transaction)
    return render(request, 'budget/transaction_form.html', {
        'form': form,
        'title': 'Editar Transacción',
        'transaction': transaction,
    })


@login_required
def transaction_delete(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk)
    if request.method == 'POST':
        transaction.delete()
        return redirect('transaction_list')
    return render(request, 'budget/transaction_confirm_delete.html', {
        'object': transaction,
        'object_type': 'la transacción',
    })


def category_list(request):
    categories = Category.objects.all()
    return render(request, 'budget/category_list.html', {
        'categories': categories,
    })


@login_required
def category_new(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm()
    return render(request, 'budget/category_form.html', {
        'form': form,
        'title': 'Nueva Categoría',
    })


@login_required
def category_edit(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'budget/category_form.html', {
        'form': form,
        'title': 'Editar Categoría',
        'category': category,
    })


@login_required
def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        category.delete()
        return redirect('category_list')
    return render(request, 'budget/transaction_confirm_delete.html', {
        'object': category,
        'object_type': 'la categoría',
    })
