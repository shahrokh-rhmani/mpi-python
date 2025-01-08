 installation instructions, MPI [mpi4py/INSTALL.rst](https://github.com/mpi4py/mpi4py/blob/master/INSTALL.rst).
## Running the Scripts

To run the non-MPI version of the calculation, use the following command:
```sh
python.exe .\src\non_mpi.py
```
To run the MPI version of the calculation, use the following command:
```sh
mpiexec.exe -np 4 python .\src\mpi.py
```
 ## What is MPI and its Benefits?
<p dir="rtl"> MPI (Message Passing Interface) یک استاندارد برای ارتباطات میان فرآیندها در سیستم‌های توزیع شده است که مزایایی مانند بهینه‌سازی زمان اجرا و توزیع بار محاسباتی را به ارمغان می‌آورد. </p>

## What is MPI.COMM_WORLD?

<p dir="rtl">
یک ارتباط‌دهنده پیش‌فرض است که شامل تمام فرآیندهایی است که در برنامه MPI شما اجرا می‌شوند. با این ارتباط‌دهنده، تمام فرآیندها می‌توانند با یکدیگر ارتباط برقرار کنند، داده‌ها را ارسال و دریافت کنند و هماهنگی‌های لازم را انجام دهند.
</p>

<p dir="rtl">گرفتن رتبه فرآیند جاری با comm.Get_rank.</p>
<p dir="rtl">گرفتن تعداد کل فرآیندها با comm.Get_size.</p>
<p dir="rtl">کاهش و جمع‌آوری نتایج محاسبات از تمام فرآیندها به فرآیند ریشه با comm.reduce.</p>

## What is comm.Get_rank?
<p dir="rtl">
فرض کنید ما ۴ فرآیند داریم (اندازه `size` برابر با ۴ است) و ۱,۰۰۰,۰۰۰,۰۰۰ تکرار داریم که می‌خواهیم بین این ۴ فرآیند تقسیم کنیم. هر فرآیند باید ۲۵۰,۰۰۰,۰۰۰ تکرار را انجام دهد.

با استفاده از `comm.Get_rank` می‌دانیم که هر فرآیند چه شماره‌ای دارد:

- فرآیند ۰ (`rank` = 0)
- فرآیند ۱ (`rank` = 1)
- فرآیند ۲ (`rank` = 2)
- فرآیند ۳ (`rank` = 3)

حالا می‌خواهیم تعیین کنیم که هر فرآیند کدام بخش از ۱,۰۰۰,۰۰۰,۰۰۰ تکرار را انجام دهد. برای این کار، حلقه را به محدوده‌های مختلف تقسیم می‌کنیم:

- فرآیند ۰ (`rank` = 0): تکرار ۰ تا ۲۴۹,۹۹۹,۹۹۹
- فرآیند ۱ (`rank` = 1): تکرار ۲۵۰,۰۰۰,۰۰۰ تا ۴۹۹,۹۹۹,۹۹۹
- فرآیند ۲ (`rank` = 2): تکرار ۵۰۰,۰۰۰,۰۰۰ تا ۷۴۹,۹۹۹,۹۹۹
- فرآیند ۳ (`rank` = 3): تکرار ۷۵۰,۰۰۰,۰۰۰ تا ۹۹۹,۹۹۹,۹۹۹

</p>
