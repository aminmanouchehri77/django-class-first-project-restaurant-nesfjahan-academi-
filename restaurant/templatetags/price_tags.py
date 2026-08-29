from django import template

register = template.Library()

@register.filter(name='split_price')
def split_price(value):
    """
    این فیلتر عدد را می‌گیرد و سه رقم سه رقم با کاما جدا می‌کند
    """
    try:
        # تبدیل مقدار به عدد صحیح و اعمال فرمت جداسازی با کاما
        return f"{int(value):,}"
    except (ValueError, TypeError):
        # اگر مقداری که پاس داده شده عدد نبود (مثلا None بود)، همان مقدار اصلی را برگردان
        return value



@register.filter(name='fa_num')
def fa_num(value):
    """تبدیل اعداد انگلیسی به فارسی"""
    if value is None:
        return ""
    
    value = str(value)
    # دیکشنری نگاشت اعداد انگلیسی به فارسی
    mapping = str.maketrans('0123456789', '۰۱۲۳۴۵۶۷۸۹')
    
    return value.translate(mapping)
