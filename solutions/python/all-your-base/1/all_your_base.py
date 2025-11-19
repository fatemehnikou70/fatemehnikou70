def rebase(input_base, digits, output_base):
    # بررسی مبنای ورودی
    if input_base < 2:
        raise ValueError("input base must be >= 2")
    if output_base < 2:
        raise ValueError("output base must be >= 2")
    
    # بررسی اعتبار ارقام
    if any(d < 0 or d >= input_base for d in digits):
        raise ValueError("all digits must satisfy 0 <= d < input base")
    
    # اگر عدد فقط صفر است
    if digits == [] or all(d == 0 for d in digits):
        return [0]
    
    # صفرهای اضافی ابتدای عدد غیر صفر ممنوع
   # if len(digits) > 1 and digits[0] == 0:
     #   raise ValueError("digits may not contain leading zeros")
    
    # تبدیل عدد به ده‌دهی
    value = 0
    for d in digits:
        value = value * input_base + d
    
    # تبدیل از ده‌دهی به مبنای خروجی
    result = []
    while value > 0:
        value, remainder = divmod(value, output_base)
        result.append(remainder)
    
    # برعکس کردن لیست تا ترتیب درست شود
    return result[::-1]
