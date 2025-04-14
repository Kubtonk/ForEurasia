from modif import MODIF, RECOMMENDATIONS
from calculator import calculate_price
from data_storage import save_history
from user import get_user_info

def main():
    print("===Калькулятор стоимости комбайна===\n")

    USER_INFO = get_user_info()

    print("\nДоступные модификации:")
    MODS = list(MODIF)
    for NUM, MOD_NAME in enumerate(MODS, 1):
        PRICE = MODIF[MOD_NAME]
        print(f"{NUM}) {MOD_NAME} - {PRICE} тг")

    RAW_INPUT = input("\nВведите номера выбранных модификаций (через запятую пожалуйста): ")
    CHOICES = RAW_INPUT.split(",")
    SELECT = []

    for ITEM in CHOICES:
        ITEM = ITEM.strip()
        if ITEM.isdigit():
            INDEX = int(ITEM)
            if 0 < INDEX <= len(MODS):
                SELECT.append(MODS[INDEX - 1])

    RECOMM = []
    for MOD in SELECT:
        if MOD in RECOMMENDATIONS:
            REC = RECOMMENDATIONS[MOD]
            if REC not in SELECT:
                RECOMM.append(REC)

    if RECOMM:
        print("\nРекомендуемые модификации:")
        for R in RECOMM:
            print("-", R)
        WANT_ADD = input("Добавить? (да/нет): ").lower()
        if WANT_ADD in ["да", "д", "y", "yes", "d", "da"]:
            for R in RECOMM:
                if R not in SELECT:
                    SELECT.append(R)

    TOTAL = calculate_price(SELECT)

    print("\n===Результат===")
    for KEY in TOTAL:
        VALUE = TOTAL[KEY]
        
        ## intValue = int(value) if isinstance(value, float) and value.is_integer() else value

        if isinstance(VALUE, float) and VALUE.is_integer():
            VALUE = int(VALUE)
        print(f"{KEY}: {VALUE} тг")


    save_history(USER_INFO, TOTAL, SELECT)
    print("\nСохранено в history.json")

if __name__ == "__main__":
    main()