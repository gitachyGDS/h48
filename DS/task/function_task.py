"""
1. Sum of Sales 
 Write a function total_sales(sales_list) that takes a list of daily sales numbers and returns 
the total sales. 
 Example: total_sales([100, 200, 300])  # Output: 600
"""

# def total_sales(price):
#     sum_=sum(price)
#     return sum_
# list= [10,20,30,40,50]
# # total_sum = total_sales(list)
# total_sum = total_sales([10,20,30,40])+ total_sales([50])
# print(total_sum)
# #150



# def total_sales(price):
#     s = sum(price)
#     return s
# list1 = [10,20,30,40,50]
# list2 = [60,70,80,90,100]
# total_sum = total_sales(list1) + total_sales(list2)
# print(total_sum)


#user define function
# sales_list=[100, 200, 300 ]
# sum = sum(sales_list) 
# def total_sales(a):
#     print(f'Total sales list is:{(a)}')
    
# total_sales(sum)    



# #built in function 
# sales_list=[100, 200, 300 ]
# sum = sum(sales_list)
# print(f'The sales list is :{sum}')

# #loop:
# sales_list=[100, 200, 300 ]
# sum = 0
# for sum in sales_list:
#  sum += sum

# print(f"The value of sales is :{sum}")

"""
2. Maximum Sale Day 
Write a function max_sale_day(sales_dict) that returns the day with the highest sale. 
Example: max_sale_day({'Mon': 100, 'Tue': 500, 'Wed': 300})  # Output: 'Tue'
# """
# sales_dict = {
#     'Mon': 100, 
#     'Tue': 500, 
#     'Wed': 300
# }

# def max_sales_day(sales_dict):
#     highest_day = max(sales_dict, key=sales_dict.get)
#     return highest_day

# # function call
# result = max_sales_day(sales_dict)
# print(f'The highest day is: {result}')

"""
5. Filter High-Value Transactions 
 Write a function high_value_transactions(transactions, threshold) to return transactions 
above a threshold. 
 Example: high_value_transactions([100, 500, 2000], 1000)  # Output: [2000]
# """
# def high_value_transactions(transactions,threshold):
#     high_value = []
#     for i in transactions:
#         if i > threshold:
#             high_value.append(i)
#     return high_value
# transactions = [100, 500, 2000]
# threshold = 1000

# result = high_value_transactions(transactions,threshold)
# print(f"The threshold value is :{result}")

"""
6. Customer Segmentation 
 Write a function segment_customers(customers) that segments customers based on 
purchase amount: 
o 5000 → ‘VIP’ 
o 1000–5000 → ‘Regular’ 
o <1000 → ‘Occasional’ 
 segment_customers([800, 1500, 7000])  # Output: ['Occasional','Regular','VIP']
"""

# def segment_customers(customers):
#     customer_segment =[]
#     for i in customers:
#         if i > 5000:
#             customer_segment.append('VIP')
#         elif i > 1000 and i < 5000:
#             customer_segment.append('Regular')
#         else:
#             customer_segment.append('Occasional')
#     return customer_segment
# customers = [800, 1500, 7000]
# result = segment_customers(customers)

# print(f"The customer segment is :{result}")

"""
7. Moving Average of Sales 
 Write a function moving_average(sales_list, n) that calculates n-day moving average. 
 Example: moving_average([100, 200, 300, 400], 2)  # Output: [150.0, 250.0, 350.0]
"""

# def moving_average(sales_list, n):
#     averages= []
#     for i in range(len(sales_list)-n+1):
#         average = sum(sales_list[i:i+n])/n
#         averages.append(average)
#     return averages
# sales_list = [100, 200, 300, 400]
# n = 2
# result = moving_average(sales_list, n)
# print(f"The moving average is :{result}")

"""
8. Product-wise Total Sales 
 Write a function product_sales(sales_data) that takes a list of tuples (product, amount) 
and returns total sales per product. 
 Example: product_sales([('A',100),('B',200),('A',300)])  # Output: {'A': 400, 'B': 200}
# """
# def product_sales(sales_data):
#     total = {}
#     for product, amount in sales_data:
#         if product in total:
#             total[product]+= amount
#         else:
#             total[product] = amount
#     return total
# sales_data =  [('A',100),('B',200),('A',300)]
# result = product_sales(sales_data)
# print(f"The product sales is :{result}")

"""9. Top-N Products 
Write a function top_products(sales_data, n) to return top n products by sales. 
  
 Example: top_products([('A',500),('B',1000),('C',700)], 2)  # Output: [('B',1000),('C',700)]
# """
# def top_products (sales_data, n):
#     sorted_sales = sorted(sales_data, key=lambda x: x[1], reverse = True)
#     return sorted_sales[:n]
# sales_data = [('A',500),('B',1000),('C',700)]
# n = 2
# result = top_products(sales_data, n)
# print(f"The top products are :{result}")

"""
14. Correlation Between Two Metrics 
 Write a function correlation(x, y) to calculate Pearson correlation coefficient between 
two lists of numbers. 
 Formula
"""
# def correlation(x, y):
#     # x र y दुईवटा list हुनुपर्छ (same length)
    
#     n = len(x)   # कति वटा डाटा छन्
    
#     # Mean (average) निकाल्ने
#     mean_x = sum(x) / n
#     mean_y = sum(y) / n

#     num = 0     # numerator सुरुमा 0
#     den_x = 0   # x को deviation squared को sum
#     den_y = 0   # y को deviation squared को sum

#     # x र y का मानहरू जोडी–जोडीमा निकाल्ने
#     for a, b in zip(x, y):
#         num += (a - mean_x) * (b - mean_y)     # numerator बढाउने
#         den_x += (a - mean_x) ** 2             # x deviation squared
#         den_y += (b - mean_y) ** 2             # y deviation squared

#     # denominator = sqrt(den_x * den_y)
#     den = (den_x * den_y) ** 0.5

#     # यदि denominator 0 भयो भने divide गर्न नसकिने, अन्तिम result 0 दिन्छ
#     if den == 0:
#         return 0

#     # अन्तिम correlation result
#     return num / den


# # Example Run
# # print(correlation([1, 2, 3], [2, 4, 6]))   # Output: 1.0
# from math import sqrt

# def correlation(x, y):
#     """
#     दुई सूची (x र y) बीचको पियर्सन सह-सम्बन्ध गुणाङ्क (r) गणना गर्छ,
#     साथै if-else प्रयोग गरी शून्यले भाग हुने त्रुटीलाई व्यवस्थापन गर्छ।
#     """
#     n = len(x)
    
#     # यदि सूचीहरूको लम्बाइ फरक छ वा ० छ भने, 0 फर्काउने (if)
#     if n != len(y) or n == 0:
#         return 0.0

#     # आवश्यक योगफल (Sums) हरू गणना गर्ने
#     sum_x = sum(x) 
#     sum_y = sum(y) 
#     sum_xy = sum(x_i * y_i for x_i, y_i in zip(x, y))
#     sum_x_sq = sum(x_i**2 for x_i in x)
#     sum_y_sq = sum(y_i**2 for y_i in y)

#     # अंश (Numerator) गणना
#     numerator = (n * sum_xy) - (sum_x * sum_y)
    
#     # हर (Denominator) का भागहरू गणना
#     term1_den = (n * sum_x_sq) - (sum_x ** 2)
#     term2_den = (n * sum_y_sq) - (sum_y ** 2)
#     denominator_product = term1_den * term2_den
    
#     # हर (Denominator) को व्यवस्थापन गर्न if-else प्रयोग गर्ने
#     # यदि हर ० भयो भने, सह-सम्बन्ध 0.0 फर्काउने (if)
#     if denominator_product <= 0:
#         return 0.0  # यदि हर ० वा ऋणात्मक भएमा
#     # अन्यथा (else), सामान्य गणना गर्ने (else)
#     else:
#         denominator = sqrt(denominator_product)
#         r = numerator / denominator
#         return r

# # --- उदाहरण (Example) परीक्षण ---

# # १. बलियो सकारात्मक सम्बन्ध (if-else को 'else' भाग चल्छ)
# x1 = [1, 2, 3]
# y1 = [2, 4, 6]
# print(f"नतिजा १ (r): {correlation(x1, y1)}") 

# # २. हर शून्य हुने अवस्था (if-else को 'if' भाग चल्छ)
# # जब सबै y मानहरू एउटै हुन्छन्, सह-सम्बन्ध परिभाषित हुँदैन (हर ० हुन्छ)।
# x2 = [10, 20, 30]
# y2 = [5, 5, 5] 
# print(f"नतिजा २ (r): {correlation(x2, y2)}")



# def correlation_formula(x, y):
#     n = len(x)
#     sum_x = sum(x)
#     sum_y = sum(y)


# x = [1, 2, 3]   
# y = [2, 4, 6]
# """
# (x,y)=(1,2),(2,4),(3,6)
# 1+2 = 3
# 2 + 4 = 6
# 3 + 6 = 9
# sum = 18




# x-->a 
# y-->b
# sumxy= a*b

# """
#     sum_xy = sum([a*b for a,b in zip(x,y)])
#     sum_x2 = sum([a**2 for a in x])
#     sum_y2 = sum([b**2 for b in y])

#     numerator = n * sum_xy - sum_x * sum_y


#     denominator = ((n * sum_x2 - sum_x**2) * (n * sum_y2 - sum_y**2)) ** 0.5

#     if denominator == 0:
#         return 0

#     return numerator / denominator

# # Example
# x = [1, 2, 3]
# y = [2, 4, 6]
# print(correlation_formula(x, y))  # Output: 1.0



# x  = 1, 2, 3 #6 #36
# y = 2, 4, 6 #12 #144
# sum = sum(x)
# sum1 = sum(y)
# sum_xy= 18


# n= 3
# 3(18)-(6)(12)#num..


# 3(36-(6)**2)
# 3(144-(12)**2)#deno..

# r = num / deno


