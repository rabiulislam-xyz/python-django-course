>>> 1
1
>>> 2
2
>>> 1+2  # এটা কি বুঝতে পারলেন যে  1 এবং 2 অবজেক্ট দুটিকে পুনরায় লিখতে হল!
3

>>> a = 1 # 1 কে এসাইন করা হল a এর ভিতর
>>> a     # এখন a লিখলে এর ভিতরে থাকা অবজেক্ট (1) রিটার্ন হবে, সরাসরি আর 1 লিখার দরকার নেই 
1         # এখানে যেমন 1 রিটার্ন হয়েছে

>>> b = 2 # b নামে আরেকটা ভ্যারিয়েবল তৈরি করে সেটাতে 2 এসাইন করলাম, ভ্যারিয়েবল যত ইচ্ছা ততই তৈরি করা যায়!
>>> b     # b লিখলে সেটার ভিতরের অবজেক্ট অর্থাৎ 2 দেখাবে
2

>>> a+b   # 1 এবং 2 অবজেক্টদুটিকে আমরা যথাক্রমে a ও b ভ্যারিয়েবলে রেখেছিলাম, তাই a আর b কে যোগ করা মানে হল  
3         # 1 আর 2 যোগ করা, ফলাফল হিসেবে 3 রিটার্ন করবে!

>>> a = 1  #a তে ইন্টেজার 1 এসাইন করা হল
>>> a
1

>>> a = "Hello" # a তে আবার স্ট্রিং "Hello" এসাইন করা হল, এর ফলে a থেকে আগের এসাইন করা 1 মুছে গিয়েছে
>>> a           # এবং a তে এখন শুধুমাত্র "Hello" স্ট্রিং টাই আছে
'Hello'

>>> a = False   #ভ্যারিয়েবলে যেকোন টাইপের অবজেক্ট রাখা যায়, বুলিয়ান টাইপের অবজেক্টও
>>> a           #এখন a ভ্যারিয়েবলে আছে False, ভ্যারিয়েবলে কোন ভ্যালু এসাইন করলে আগের এসাইন করা ভ্যালুগুল আর থাকেনা
False

>>> msg = "Hi! this is my message, and I can write anything in my message, because its my message"
>>> msg
'Hi! this is my message, and I can write anything in my message, because its my message'

>>> len(msg)
86

>>> type(msg)
<class 'str'>

>>> msg.upper()
'HI! THIS IS MY MESSAGE, AND I CAN WRITE ANYTHING IN MY MESSAGE, BECAUSE ITS MY MESSAGE'

>>> msg.lower()
'hi! this is my message, and i can write anything in my message, because its my message
'
>>> msg.title()  # title() মেথডটি স্ট্রিং এর প্রতিটি শব্দের শুরুর অক্ষর বড় হাতের করে দেয়
'Hi! This Is My Message, And I Can Write Anything In My Message, Because Its My Message'
