# پروژه ذخیره اطلاعات موبایل

درصورت تمیایل میتوان
نید از محیف مجازی پایتون استفاده کنید

## پیشنیاز ها
ابتدا پیشنیاز‌های فایل production.txt را نصب میکنیم

```shell
pip install -r requirements/production.txt
```
میتوانید برای کار روی پروژه از فایل dev.txt هم استفاده کنید

## یک کاربر امدین ایجاد میکنیم

```shell
python manage.py createsuperuser
```

میتوانید از محصولات پیشفرض استفاده کنید
```shell
python manage.py loaddata phone
```

## توضیحات

در پروژه از فرم ها و ویو عادی جنگو استفاده شده  و خیلی از تسک های گفته شده به راحتی با django admin قابل انجام هست (مدل ها به django admin اضافه شدند و میتوان با آنها کار کرد)

فیلتر های خاسته شده در url های زیر در دسترس هستند

- nationality_filter/
- brand_filter/
- brand_nationality_filter/
