import math
import argparse

"""Программа рассчитывает условия кредита по введенным значениям параметров"""

parser = argparse.ArgumentParser()

# Аргументы командной строки
parser.add_argument("--type")  # Тип начисления процентов: простой или сложный
parser.add_argument("--principal")  # Сумма кредита
parser.add_argument("--interest")  # Процент переплаты
parser.add_argument("--payment")  # Платеж в месяц
parser.add_argument("--periods")  # Число месяцев платежа

args = parser.parse_args()

# Простой платеж
if args.type == "annuity":

    if args.principal and args.payment and args.interest:

        loan_principal = int(args.principal)
        monthly_payment = int(args.payment)
        loan_interest = float(args.interest)

        nominal_interest = loan_interest / (12 * 100)
        months = math.log((monthly_payment / (monthly_payment - nominal_interest * loan_principal)),
                          1 + nominal_interest)
        months = math.ceil(months)

        overpay = math.ceil(months * monthly_payment - loan_principal)

        if months == 1:
            print(f"Потребуется {months} месяцев, чтобы выплатить кредит.\nПереплата = {overpay}")
        elif 12 > months > 1:
            print(f"Потребуется {months} месяцев, чтобы выплатить кредит.\nПереплата = {overpay}")
        elif months % 12 == 0:
            years = months / 12
            print(f"Потребуется {round(years)} месяцев, чтобы выплатить кредит.\nПереплата = {overpay}")
        else:
            years = months // 12
            num_month = months % 12
            print(f"Потребуется {round(years)} лет и {num_month} месяцев, чтобы выплатить кредит."
                  f"\nПереплата = {overpay}")

    elif args.principal and args.periods and args.interest:

        loan_principal = int(args.principal)
        num_periods = int(args.periods)
        loan_interest = float(args.interest)

        nominal_interest = loan_interest / (12 * 100)
        monthly_payment = math.ceil(loan_principal * (nominal_interest * (1 + nominal_interest) ** num_periods) /
                                    ((1 + nominal_interest) ** num_periods - 1))
        overpay = math.ceil((monthly_payment * num_periods) - loan_principal)

        print(f"Ежемесячный платеж = {monthly_payment}!\nПереплата = {overpay}")


    elif args.payment and args.periods and args.interest:

        annuity_payment = float(args.payment)
        periods_num = int(args.periods)
        loan_interest = float(args.interest)

        nominal_interest = loan_interest / (12 * 100)
        loan_principal = math.ceil(annuity_payment / (nominal_interest * ((1 + nominal_interest) ** periods_num) /
                                                      (((1 + nominal_interest) ** periods_num) - 1)))
        overpayment = math.ceil(periods_num * annuity_payment - loan_principal)
        print(f"Величина кредита = {loan_principal}!\nПереплата = {overpayment}")

    else:
        print("Введены неверные параметры")

# Сложный платеж
elif args.type == "diff":

    if args.interest and args.principal and args.periods:

        loan_principal = int(args.principal)
        num_months = int(args.periods)
        interest = float(args.interest)
        sum_payment = 0

        for x in range(1, num_months + 1):

            diff_payment = math.ceil(loan_principal / num_months + interest / (12 * 100) *
                                     (loan_principal - loan_principal * (x - 1) / num_months))
            print(f"{x} месяц: платеж {diff_payment}")
            sum_payment += diff_payment

        overpayment = sum_payment - loan_principal
        print(f"\nПереплата = {overpayment}")

    else:
        print("Введены неверные параметры")

else:
    print("Введены неверные параметры")
