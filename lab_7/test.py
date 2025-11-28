import time
import cProfile
from original_analyzer import heavy_analysis
from optimized_analyzer import heavy_analysis_optimized


def run_original_with_profile():
    print("=" * 60)
    print("ОРИГИНАЛЬНАЯ ВЕРСИЯ (С ПРОФИЛИРОВАНИЕМ)")
    print("=" * 60)
    cProfile.run('heavy_analysis()', sort='cumulative')


def run_optimized_with_profile():
    print("=" * 60)
    print("ОПТИМИЗИРОВАННАЯ ВЕРСИЯ (С ПРОФИЛИРОВАНИЕМ)")
    print("=" * 60)
    cProfile.run('heavy_analysis_optimized()', sort='cumulative')


def quick_comparison():
    print(" БЫСТРОЕ СРАВНЕНИЕ ПРОИЗВОДИТЕЛЬНОСТИ")
    print("=" * 50)

    # Оригинальная версия
    print("\nЗапуск ОРИГИНАЛЬНОЙ версии...")
    start_orig = time.time()
    heavy_analysis()
    time_orig = time.time() - start_orig

    print("\n" + "=" * 50)

    # Оптимизированная версия
    print("\n⚡ Запуск ОПТИМИЗИРОВАННОЙ версии...")
    start_opt = time.time()
    heavy_analysis_optimized()
    time_opt = time.time() - start_opt

    print("\n" + "=" * 50)
    print(" РЕЗУЛЬТАТЫ СРАВНЕНИЯ:")
    print(f"Оригинальная версия: {time_orig:.3f} сек")
    print(f"Оптимизированная версия: {time_opt:.3f} сек")
    print(f"Ускорение: {time_orig / time_opt:.2f}x")

    if time_orig > time_opt:
        print(f"Оптимизированная версия быстрее на {time_orig - time_opt:.2f} сек")
    else:
        print(" Оптимизированная версия медленнее")


def individual_function_benchmark():
    """Бенчмарк отдельных функций"""
    print("\nБЕНЧМАРК ОТДЕЛЬНЫХ ФУНКЦИЙ")
    print("=" * 50)

    # Импортируем функции для тестирования
    from original_analyzer import generate_dataset, count_words_bad
    from optimized_analyzer import generate_dataset_optimized, count_words_optimized

    # Тест генерации данных
    print("\nГенерация датасета (1000 предложений):")

    start = time.time()
    dataset_orig = generate_dataset(1000)
    time_orig_gen = time.time() - start
    print(f"  Оригинальная: {time_orig_gen:.3f} сек")

    start = time.time()
    dataset_opt = generate_dataset_optimized(1000)
    time_opt_gen = time.time() - start
    print(f"  Оптимизированная: {time_opt_gen:.3f} сек")
    print(f"  Ускорение генерации: {time_orig_gen / time_opt_gen:.2f}x")

    # Тест подсчета слов
    print("\nПодсчет слов (1000 предложений):")

    start = time.time()
    counts_orig = count_words_bad(dataset_orig)
    time_orig_count = time.time() - start
    print(f"  Оригинальная: {time_orig_count:.3f} сек")

    start = time.time()
    counts_opt = count_words_optimized(dataset_opt)
    time_opt_count = time.time() - start
    print(f"  Оптимизированная: {time_opt_count:.3f} сек")
    print(f"  Ускорение подсчета: {time_orig_count / time_opt_count:.2f}x")


def main():
    """Главная функция тестирования"""
    print("ТЕСТИРОВАНИЕ ПРОИЗВОДИТЕЛЬНОСТИ ТЕКСТОВОГО АНАЛИЗАТОРА")
    print("Выберите вариант тестирования:")
    print("1 - Быстрое сравнение (рекомендуется)")
    print("2 - Профилирование оригинальной версии")
    print("3 - Профилирование оптимизированной версии")
    print("4 - Бенчмарк отдельных функций")
    print("5 - Полное тестирование (все варианты)")

    choice = input("\nВведите номер варианта (1-5): ").strip()

    if choice == "1":
        quick_comparison()
    elif choice == "2":
        run_original_with_profile()
    elif choice == "3":
        run_optimized_with_profile()
    elif choice == "4":
        individual_function_benchmark()
    elif choice == "5":
        quick_comparison()
        print("\n" + "=" * 80)
        individual_function_benchmark()
        print("\n" + "=" * 80)
        print("Для детального профилирования запустите отдельно:")
        print("  python performance_test.py (и выберите варианты 2 или 3)")
    else:
        print("Неверный выбор. Запускаю быстрое сравнение...")
        quick_comparison()


if __name__ == "__main__":
    main()