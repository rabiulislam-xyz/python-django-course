>>> a = 1  # ভ্যারিয়েবলে কিভাবে ভ্যালু বা ডাটা এসাইন করতে হয় সেটা কি ক্লিয়ার হয়েছে ? 
>>> a      # a এর ভিতর 1 রাখলাম
1
>>> type(a)   # a এর টাইপ জানতে চাই মানে a তে থাকা অবজেক্টের টাইপ জানতে চাই
<class 'int'> # 1 তো ইন্টেজারই হবে!

>>> a = bool(1)  # bool() ফাংশন দিয়ে 1 কে কাস্ট/কনভার্ট করে আবার a তে রাখলাম
>>>a             # a তে এখন নতুন ভ্যালু, আগের ভ্যালু মুছে গেছে
True
>>> type(a)      # টাইপ তো বুলিয়ানই হওয়ার কথা, কারন আমরা 1 কে কাস্ট করে boolean টাইপ করে ফেলেছি! 
<class 'bool'>

>>> a = str(1)   # str() ফাংশনটি bool() এর মতই, তবে এটা কোন অবজেক্টকে স্ট্রিং বানিয়ে ফেলে 
>>>a             # str() এর প্যারামিটার হিসেবে ইন্টেজার 1 দিয়েছিলাম
'1'              # এবং সেটা কাস্ট/কনভার্ট হয়ে স্ট্রিং '1' হয়ে গেছে! 
>>> type(a)      # বিশ্বাস না হলে টাইপ চেক করে দেখুন
<class 'str'>    # স্ট্রিং... 

>>> a = float(1)  # float() ফাংশনের কাজ কোন ভ্যালুকে ফ্লোটিং পয়েন্ট নাম্বারে কাস্ট করা
>>>a              # দিয়েছিলাম ইন্টেজার 1 
1.0               # হয়ে গেল ফ্লোট 1.0
>>> type(a)
<class 'float'>


>>> name = "Hello"  # ভ্যারিয়বলে একটা স্ট্রিং এসাইন করলাম
>>> type(name)      # ভ্যারিয়েবলের টাইপটা আরেকবার দেখে নেই
<class 'str'>       # হুম, স্ট্রিং ই আছে

>>>  bool(name)     # আচ্ছা, স্ট্রিং টাকে বুলিয়ানে কনভার্ট করি তো
True                # হ্যা, কনভার্ট হয়েছে, এবং বুলিয়ান ভ্যালু True রিটার্ন করেছে

>>> int(name)       # আচ্ছে, এবার তাহলে স্ট্রিং টাকে ইন্টেজারে কনভার্ট করে দেখি 
Traceback (most recent call last):      # উপস... এরর হল ক্যানো!!!? 
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: 'Hello'

>>> int("33434") # একটা স্ট্রিং টাইপের ভিতর শুধু নাম্বার রেখে সেটাকে কি ইন্টেজারে কনভার্ট করা যাবে?
33434            # যাচ্ছে! তার মানে হল...
