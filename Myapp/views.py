from django.shortcuts import render
import json
from django.views.generic import View
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@method_decorator(csrf_exempt,name='dispatch')
class BMIVIEW(View):
    def post(self,request):
        data = json.loads(request.body)
        
        h = data.get("height")
        w = data.get("weight")
        
        #convert height cm to m
        height = h/100
        bmi = w / (height**2)
        
        result = {
            "Height" : data.get('height'),
            "weight" : w,
            "BMI" : round(bmi,2)
        }
        return JsonResponse(result)
        
        
@method_decorator(csrf_exempt, name='dispatch')
class AgeCalculatorView(View):

    def post(self, request):

        data = json.loads(request.body)

        b = data.get("birth_year")
        c = data.get("current_year")

        age = c - b

        result = {
            "birth_year": b,
            "current_year": c,
            "age": age
        }

        return JsonResponse(result)
    
    
@method_decorator(csrf_exempt, name='dispatch')
class PercentageCalculatorView(View):

    def post(self, request):

        marks = json.loads(request.body)

        ob = marks.get("obtained_marks")
        cm = marks.get("total_marks")

        percentage = (ob/cm) * 100

        result = {
            "obtained_marks": ob,
            "total_marks": cm,
            "percentage": percentage
        }

        return JsonResponse(result)
    

@method_decorator(csrf_exempt, name='dispatch')
class SimpleInterestView(View):

    def post(self, request):

        data = json.loads(request.body)

        principal = data.get("principal")
        rate = data.get("rate")
        time = data.get("time")

        simple_interest = (principal * rate * time) / 100

        result = {
            "principal": principal,
            "rate": rate,
            "time": time,
            "SimpleInterest": simple_interest
        }

        return JsonResponse(result)
    
@method_decorator(csrf_exempt, name='dispatch')
class ElectricityBillView(View):

    def post(self, request):

        data = json.loads(request.body)

        units = data.get("units")
        rate = data.get("rate")

        bill = units * rate

        result = {
            "units": units,
            "rate": rate,
            "Bill": bill
        }

        return JsonResponse(result)
    
@method_decorator(csrf_exempt, name='dispatch')
class DiscountView(View):

    def post(self, request):

        data = json.loads(request.body)

        price = data.get("price")
        discount_percentage = data.get("discount_percentage")

        discount_amount = (price * discount_percentage) / 100
        final_price = price - discount_amount

        result = {
            "price": price,
            "discount_percentage": discount_percentage,
            "discount_amount": discount_amount,
            "final_price": final_price
        }

        return JsonResponse(result)
    
@method_decorator(csrf_exempt, name='dispatch')
class ProfitView(View):

    def post(self, request):

        data = json.loads(request.body)

        cost_price = data.get("cost_price")
        selling_price = data.get("selling_price")

        profit = selling_price - cost_price

        result = {
            "cost_price": cost_price,
            "selling_price": selling_price,
            "Profit": profit
        }

        return JsonResponse(result)
    
@method_decorator(csrf_exempt, name='dispatch')
class SalaryView(View):

    def post(self, request):

        data = json.loads(request.body)

        basic_salary = data.get("basic_salary")
        bonus = data.get("bonus")
        deduction = data.get("deduction")

        net_salary = basic_salary + bonus - deduction

        result = {
            "basic_salary": basic_salary,
            "bonus": bonus,
            "deduction": deduction,
            "net_salary": net_salary
        }

        return JsonResponse(result)
    
@method_decorator(csrf_exempt, name='dispatch')
class TimeView(View):

    def post(self, request):

        data = json.loads(request.body)

        hours = data.get("hours")

        minutes = hours * 60
        seconds = hours * 3600

        result = {
            "hours": hours,
            "minutes": minutes,
            "seconds": seconds
        }

        return JsonResponse(result)
    
@method_decorator(csrf_exempt, name='dispatch')
class FuelCostView(View):

    def post(self, request):

        data = json.loads(request.body)

        distance = data.get("distance")
        mileage = data.get("mileage")
        fuel_price = data.get("fuel_price")

        fuel_required = distance / mileage
        total_cost = fuel_required * fuel_price

        result = {
            "distance": distance,
            "mileage": mileage,
            "fuel_price": fuel_price,
            "fuel_required": fuel_required,
            "total_cost": total_cost
        }

        return JsonResponse(result)
    
@method_decorator(csrf_exempt, name='dispatch')
class ProductProfitView(View):

    def post(self, request):

        data = json.loads(request.body)

        cost_price = data.get("cost_price")
        selling_price = data.get("selling_price")
        quantity = data.get("quantity")

        total_cost = cost_price * quantity
        total_sales = selling_price * quantity

        profit = total_sales - total_cost

        result = {
            "cost_price": cost_price,
            "selling_price": selling_price,
            "quantity": quantity,
            "total_cost": total_cost,
            "total_sales": total_sales,
            "profit": profit
        }

        return JsonResponse(result)
    
@method_decorator(csrf_exempt, name='dispatch')
class WorkSalaryView(View):

    def post(self, request):

        data = json.loads(request.body)

        hours_worked = data.get("hours_worked")
        regular_hours = data.get("regular_hours")
        hourly_rate = data.get("hourly_rate")
        overtime_rate = data.get("overtime_rate")

        regular_pay = regular_hours * hourly_rate

        overtime_hours = hours_worked - regular_hours

        overtime_pay = overtime_hours * overtime_rate

        total_salary = regular_pay + overtime_pay

        result = {
            "hours_worked": hours_worked,
            "regular_hours": regular_hours,
            "hourly_rate": hourly_rate,
            "overtime_rate": overtime_rate,
            "regular_pay": regular_pay,
            "overtime_hours": overtime_hours,
            "overtime_pay": overtime_pay,
            "total_salary": total_salary
        }

        return JsonResponse(result)
    
@method_decorator(csrf_exempt, name='dispatch')
class AgeDetailsView(View):

    def post(self, request):

        data = json.loads(request.body)

        age = data.get("age")

        months = age * 12
        weeks = age * 52
        days = age * 365

        result = {
            "age": age,
            "months": months,
            "weeks": weeks,
            "days": days
        }

        return JsonResponse(result)
        
        
        
    
    
